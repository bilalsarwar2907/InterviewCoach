# InterviewCoach — Architecture

Updated 27 Nov 2026. Matches the code on `master`.

## 1. The big picture

```
            You (Copilot Studio test chat / Teams)
                          │
                          ▼
             ┌──────────────────────────┐
             │  Copilot Studio agent    │   = the Boss
             │  asks, scores, decides   │
             └──────────┬───────────────┘
        ┌───────────────┴─────────────────┐
        │ (A) "make a prep plan"          │ (B) "save this practice score"
        ▼                                 ▼
┌──────────────────────────┐   ┌──────────────────────────────┐
│ Custom connector         │   │ Power Automate agent flow    │ = the Helper
│ interview-prep-openapi   │   │ "Save Practice Session"      │
└──────────┬───────────────┘   └──────────┬───────────────────┘
           ▼                              ▼  ok            ▼  failed / timed out
┌──────────────────────────┐   ┌────────────────────┐ ┌────────────────────┐
│ FastAPI on Azure         │   │ SharePoint list    │ │ SharePoint list    │
│ App Service (Free F1)    │   │ PracticeSessions   │ │ SessionErrors      │
│ = Computer in the Cloud  │   │ = the Notebook     │ │ = second notebook  │
└──────────┬───────────────┘   └─────────┬──────────┘ └────────────────────┘
           ▼                             ▼
┌──────────────────────────┐   ┌────────────────────┐
│ knowledge/<role>/*.md    │   │ Power BI report    │ = the Window
│ = the recipe books       │   │ InterviewCoach.pbix│
└──────────────────────────┘   └────────────────────┘
```

> **Boss decides → Helper does → Notebook keeps → Window shows.**

## 2. The parts

| Part | Tool | Job |
|---|---|---|
| Boss | Copilot Studio agent | Talks to the user, asks questions, scores answers 1–5 |
| Computer in the Cloud | FastAPI on Azure App Service `interviewcoach-bilal` | Builds the prep plan from the knowledge files |
| Contract | `interview-prep-openapi.json` (hand-written, OpenAPI 3.0.1) | Tells Copilot Studio what the API looks like. Only `POST /interview-prep` |
| Helper | Power Automate agent flow `Save Practice Session` | Writes one row per practice answer |
| Notebook | SharePoint list `PracticeSessions` (site *Learning Copilot*) | Stores the sessions |
| Second notebook | SharePoint list `SessionErrors` | Stores save failures |
| Window | Power BI Desktop `powerbi/InterviewCoach.pbix` | Sessions done, average score, average by role, weaknesses, score over time |
| Deploy | GitHub Actions (`.github/workflows/master_interviewcoach-bilal.yml`) | Every push to `master` deploys to Azure (OIDC login, no secrets in repo) |

## 3. Path A — the prep plan (Python)

```
POST /interview-prep  { role, experience_level, skills }
        │
        ▼
interview_prep_service.generate_interview_prep()      ← Facade (1 call)
        ├── interview_service.generate_questions()    → 5 questions
        ├── skill_gap_service.analyze_skill_gap()     → matched / missing skills
        └── study_plan_service.generate_study_plan()  → max 7 days, 1 missing skill per day
                     │
                     ▼ all three read
        knowledge_service.load_role_knowledge(role)   → all .md files in knowledge/<role>/
```

- `role` → folder name: lower case, spaces and `_` become `-` (`"AI Engineer"` → `ai-engineer`).
- **Facade pattern:** one endpoint hides 3 services. Copilot Studio only sees `/interview-prep`.

## 4. The knowledge file format (the contract)

Rule: **a new role = a new folder with a .md file. Zero Python changes.**
This needed one code change, once (step 8: added `extract_questions()`). After that, every new role = zero Python changes. Proven with `behavioral`.

```
Core Skills

- Skill 1
- Skill 2

Interview Questions

- Role question 1
- Role question 2

Junior Questions        (optional)

- ...

Mid Questions           (optional)

- ...

Senior Questions        (optional)

- ...
```

| Section | Read by | Used for | If missing |
|---|---|---|---|
| `Core Skills` | `extract_skills()` | skill gap + study plan | test fails (knowledge contract) |
| `Interview Questions` | `extract_questions()` | first 3 questions | backup: "What is your experience with {role}?" |
| `Junior / Mid / Senior Questions` | `extract_questions(knowledge, "<Level> Questions")` | last 2 questions | backup: built-in **technical** questions (Git, debugging …) |

Format rules:
- The level backup is technical. **A non-technical role (like `behavioral`) MUST have Junior / Mid / Senior lists**, or it gets Git/debugging questions.
- Heading with or without `#`. Each item starts with `- `.
- A list stops at the first line that does not start with `- `.
- Put all sections of a role in **one** file (the reader stops at the first list it finds).
- Questions must match the role's skills.

Checked by `tests/test_knowledge_contract.py`: every role folder with at least one `.md` file must have `Core Skills`. Empty folders are skipped.

| Role folder | Status |
|---|---|
| `ai-engineer` | active |
| `cloud-engineer` | active (no question lists yet → backups) |
| `behavioral` | active (all lists) |
| `data-engineer`, `python` | empty placeholders |

## 5. Path B — saving a practice session (no Python)

Flow `Save Practice Session`:

1. **When an agent calls the flow**. Inputs: `Question`, `Role`, `Score`, `Strengths`, `Weaknesses`
2. **Create item** → `PracticeSessions`. Title = `take(triggerBody()?['text'], 255)` (SharePoint Title max 255)
3. **Create item 1** → `SessionErrors`. *Run after:* has failed + has timed out
4. **Respond to the agent**. *Run after:* Create item 1 is successful + is skipped. **The agent always gets an answer, and the interview never stops.**

### Session schema: one source of truth = the SharePoint columns

`PracticeSessions`

| Column | Type | From |
|---|---|---|
| `Title` | single line | the question |
| `Role` | single line | role folder name, e.g. `ai-engineer` |
| `Score` | number (1–5) | agent's score |
| `Strengths` | multiple lines | at least 1 |
| `Weaknesses` | multiple lines | at least 1 |
| `Created` | date (automatic) | SharePoint |

`SessionErrors`: `Title` (question, cut to 250 chars), `ErrorDetails` (multiple lines), `Created` (automatic).

Not stored yet: `experience_level`, `duration` (not in the agent's real output).

## 6. Power BI (the Window)

SharePoint Online List connector (2.0) → `PracticeSessions` → keep `Title, Role, Score, Strengths, Weaknesses, Created` → `Score` as Whole Number.
Visuals: Sessions done (Count), Average score (Average), Average score by role (bar), Role + Weaknesses (table), Average score over time (line).
Refresh by hand in Power BI Desktop (Power BI Service auto-refresh = later).

## 7. Design decisions

| Decision | Why |
|---|---|
| Power Automate saves, not Python (option A) | No extra Python. Shows Power Platform. |
| Hand-written minimal OpenAPI contract | Project rule: never the FastAPI auto-generated file. If connecting fails → check the contract first |
| Roles differ in **data**, not classes | Data-driven variation, not Strategy. No Factory needed |
| Facade (`/interview-prep`) | One simple call for the agent |
| Adapter (`SessionStore`) | Only if option B is ever built (step 12b, optional) |

## 8. Known limits

- Question longer than 255 chars → cut to 255 and still saved. The `SessionErrors` branch is for all other errors.
- `cloud-engineer` has no question lists yet → backup questions.
- Azure Free F1 → first call after idle can be slow (cold start).
