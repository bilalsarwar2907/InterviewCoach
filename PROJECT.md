# Interview Coach Roadmap

Current Phase: 7 (complete)

---

## Phase 0 — Project Scaffold ✅
- FastAPI backend with service-layer architecture
- `src/interviewcoach/` package structure
- `main.py` entry point with all endpoints

## Phase 1 — SharePoint Knowledge Base ✅
- `knowledge/ai-engineer/` — 3 markdown files
- Uploaded to SharePoint library "LearningCopilot"

## Phase 2 — Create Copilot Studio Agent ✅
- Agent created in zealand.dk Power Platform environment
- Model: GPT-4.1

## Phase 3 — Ground Agent with SharePoint ✅
- "LearningCopilot" connected as knowledge source
- Status: Ready and verified

## Phase 4 — Interview Question Generator ✅
- `/interview/questions` endpoint
- Role-specific questions from knowledge files
- Experience level (junior / mid / senior) correctly applied

## Phase 5 — Skill Gap Analyzer ✅
- `/skill-gap` endpoint
- Compares candidate skills against role's Core Skills section
- Returns matched_skills and missing_skills

## Phase 6 — 7-Day Study Planner ✅
- `/study-plan` and `/study-plan-from-skills` endpoints
- Capped at 7 days
- Each day has: day, focus, objective, estimated_hours

## Phase 7 — Power Automate Integration ✅
- "Review Interview Plan" flow — Published
- "Test Flow" — Published
- ngrok static domain: protozoan-ripcord-flying.ngrok-free.dev
- OpenAPI contract: `interview-prep-openapi.json` (hand-crafted, minimal)
- Copilot Studio REST API tool connected and tested

---

## Bugs Fixed (Session — Aug 2026)
1. `knowledge_service.py` — relative path (broke when uvicorn started outside project root)
2. `study_plan_service.py` — no 7-day cap
3. `study_plan_service.py` — inconsistent response format
4. `interview_service.py` — experience_level was ignored
5. `knowledge_service.py` — fragile heading parser (failed on `#` prefix)
6. `interview-prep-openapi.json` — missing response schema
7. `src/interviewcoach/openapi.json` — corrupted (contained ngrok HTML error page)
8. `requirements.txt` — unpinned versions
9. `main.py` — no error handling on any endpoint
10. `tests/` — no tests existed

## CI
- GitHub Actions: `.github/workflows/python.yml`
- Steps: compile check → pytest (22 tests, all passing)

---

## Pending

### Phase 8 — Microsoft Teams Deployment
- Deploy Copilot Studio agent to Teams channel

### Phase 9 — Architecture Documentation
- Update `architecture/architecture.md` to reflect current state

### Phase 10 — Portfolio Packaging
- Clean README, screenshots, demo video

### Knowledge Gaps (not bugs)
- `knowledge/python/` — empty
- `knowledge/data-engineer/` — empty
- `knowledge/behavioral/` — empty

---

---

# Session Summary — 2026-08-18 — InterviewCoach

## Session Identity
- **Date:** 18 August 2026
- **Project:** InterviewCoach
- **Repository:** https://github.com/bilalsarwar2907/InterviewCoach
- **Local path:** `C:\Users\biges\InterviewCoach`
- **Session type:** Bug fix + code review + CI setup + minor improvements

---

## Context Coming Into This Session

The project had been built in a previous series of sessions using AI-assisted programming. The goals at the start of this session were:

1. Find missing session summaries from earlier sessions
2. Do a full code review
3. Fix all bugs so the project could be run and tested
4. Work in baby steps — one problem at a time, no information overload

Earlier sessions had wasted significant time troubleshooting Copilot Studio connection failures by focusing on the backend code, when the real cause was a missing response schema in the OpenAPI contract. This was documented and corrected this session.

---

## Project Architecture (as of session end)

```
InterviewCoach/
├── main.py                          # FastAPI app, all endpoints, error handling
├── requirements.txt                 # Pinned: fastapi, uvicorn, pydantic, pytest
├── pytest.ini                       # testpaths = tests
├── export_openapi.py                # Generates schema from app object (safe)
├── interview-prep-openapi.json      # Hand-crafted OpenAPI 3.0.1 for Copilot Studio
├── knowledge/
│   ├── UPLOAD_CHECKLIST.md          # SharePoint upload status (updated this session)
│   └── ai-engineer/
│       ├── ai_engineer_interview_guide.md
│       ├── azure_ai_search.md
│       └── copilot_studio.md
├── src/interviewcoach/
│   ├── models/                      # Pydantic request models
│   └── services/
│       ├── knowledge_service.py     # Loads .md files, extracts Core Skills
│       ├── skill_gap_service.py     # Compares candidate skills vs role skills
│       ├── study_plan_service.py    # Generates 7-day plan from missing skills
│       ├── interview_service.py     # Generates questions by role + level
│       └── interview_prep_service.py # Combines all services into one response
├── tests/
│   ├── __init__.py
│   └── test_services.py            # 22 unit tests — all passing
└── .github/workflows/python.yml    # CI: compile check + pytest
```

---

## How to Run the Project

### 1. Start the backend
```powershell
cd C:\Users\biges\InterviewCoach
python -m uvicorn main:app --reload --port 8000
```

### 2. Start ngrok tunnel
```powershell
ngrok http --domain=protozoan-ripcord-flying.ngrok-free.dev 8000
```
> ngrok binary is at `C:\Users\biges\Downloads\ngrok-v3-stable-windows-amd64\ngrok.exe`
> It was added to User PATH this session — should work directly as `ngrok`

### 3. Test locally
```powershell
Invoke-RestMethod -Uri "http://localhost:8000/health" -Method GET
Invoke-RestMethod -Uri "http://localhost:8000/interview-prep" -Method POST `
  -ContentType "application/json" `
  -Body '{"role":"AI Engineer","experience_level":"Junior","skills":["Python"]}'
```

### 4. Run tests
```powershell
cd C:\Users\biges\InterviewCoach
python -m pytest
```

---

## Endpoints

| Method | Path | Description |
|--------|------|-------------|
| GET | `/` | Health root |
| GET | `/health` | Health check |
| POST | `/interview/questions` | Generate interview questions |
| GET | `/knowledge/{role}` | Load raw knowledge for a role |
| POST | `/skill-gap` | Analyze matched/missing skills |
| POST | `/study-plan` | Generate 7-day plan from missing skills |
| POST | `/study-plan-from-skills` | Analyze gap + generate plan in one call |
| POST | `/interview-prep` | Full prep: questions + skill gap + study plan |
| GET | `/api-info` | API metadata |

---

## Copilot Studio Setup

- **Environment:** zealand.dk (Power Platform)
- **Agent model:** GPT-4.1
- **Knowledge source:** "LearningCopilot" SharePoint library — Status: Ready
- **REST API tool:** InterviewCoach, connected via `interview-prep-openapi.json`
- **Flows:** "Review Interview Plan" and "Test Flow" — both Published
- **Public URL:** `https://protozoan-ripcord-flying.ngrok-free.dev`

### IMPORTANT — Re-import required
If `interview-prep-openapi.json` is ever updated, it must be manually re-imported into Copilot Studio:
> Tools → InterviewCoach REST API → Edit tool → re-upload the file

### How the agent works
1. User tells the agent their role and skills in natural language
2. Agent extracts role, skills, and asks for experience_level if not provided
3. Agent calls `POST /interview-prep` on the FastAPI backend via ngrok
4. Backend returns questions, skill gap, and 7-day study plan
5. Agent presents results to the user in natural language

---

## All 10 Bugs Fixed This Session

### BUG 1 — `knowledge_service.py` relative path
**File:** `src/interviewcoach/services/knowledge_service.py`
**Problem:** `Path("knowledge")` only resolved correctly if uvicorn was started from project root.
**Fix:** `_KNOWLEDGE_ROOT = Path(__file__).resolve().parents[3] / "knowledge"`

### BUG 2 — `study_plan_service.py` no 7-day cap
**File:** `src/interviewcoach/services/study_plan_service.py`
**Problem:** Plan could generate unlimited days if many skills were missing.
**Fix:** `missing_skills[:MAX_PLAN_DAYS]` where `MAX_PLAN_DAYS = 7`

### BUG 3 — `study_plan_service.py` inconsistent format
**File:** `src/interviewcoach/services/study_plan_service.py`
**Problem:** Each day item was a flat string, not a structured object.
**Fix:** Each item now returns `{day, focus, objective, estimated_hours}`

### BUG 4 — `interview_service.py` experience_level ignored
**File:** `src/interviewcoach/services/interview_service.py`
**Problem:** experience_level parameter was accepted but never used — all users got junior questions.
**Fix:** Added `_normalise_level()` function, level-specific question bank, and combined role + level questions (max 5 total)

### BUG 5 — `knowledge_service.py` fragile heading parser
**File:** `src/interviewcoach/services/knowledge_service.py`
**Problem:** `extract_skills()` failed if the `## Core Skills` heading had `#` prefixes.
**Fix:** `line.lstrip("#").strip() == "Core Skills"` — works with any number of `#` characters

### BUG 6 — `interview-prep-openapi.json` missing response schema
**File:** `interview-prep-openapi.json`
**Problem:** No `responses` schema defined — Copilot Studio could not parse the API response and was returning errors or empty results.
**Fix:** Added full response schema with role, questions, skill_gap (matched_skills, missing_skills), study_plan (plan array with day, focus, objective, estimated_hours)
**NOTE:** This was the root cause of the Copilot Studio integration failures in previous sessions.

### BUG 7 — `src/interviewcoach/openapi.json` corrupted
**File:** `src/interviewcoach/openapi.json`
**Problem:** `export_openapi.py` had been run while ngrok was down — saved the ngrok HTML error page instead of JSON.
**Fix:** File overwritten with valid OpenAPI JSON. `export_openapi.py` updated with safety checks.

### BUG 8 — `requirements.txt` unpinned versions
**File:** `requirements.txt`
**Problem:** All packages were unpinned (`fastapi`, `uvicorn`, etc.) — any future install could break the project silently.
**Fix:** All versions pinned to what was installed and working. `pytest==8.3.5` added.

### BUG 9 — `main.py` no error handling
**File:** `main.py`
**Problem:** All endpoints had no try/except — any service error would return an unhandled 500 with no useful message.
**Fix:** All endpoints wrapped in try/except returning `JSONResponse(status_code=500, content={"error": "...", "detail": str(e)})`

### BUG 10 — No unit tests
**Files:** `tests/test_services.py`, `pytest.ini`, `tests/__init__.py`, `.github/workflows/python.yml`
**Problem:** No tests existed — no way to verify the code worked without running the full stack.
**Fix:** 22 unit tests written covering all 5 services. CI updated to run pytest. All 22 passing.

---

## Minor Improvements This Session

1. **`export_openapi.py`** — Added try/except on import, JSON validation, and informative output. Prevents silent corruption if app fails to load.
2. **`knowledge/UPLOAD_CHECKLIST.md`** — Updated to reflect actual state: AI Engineer fully connected, 3 empty roles listed with instructions.
3. **`tests/__init__.py`** — Created (empty) to make tests a proper Python package.
4. **`pytest.ini`** — Added with `testpaths = tests` so `pytest` works from any directory.
5. **`PROJECT.md`** — Fully rewritten to reflect completed phases, bugs fixed, CI status, and pending work.
6. **CI folder name** — Verified `.github/workflows/` (correct, plural) — was showing as `workflow` in an earlier ls but confirmed correct on disk.

---

## CI Status

- **File:** `.github/workflows/python.yml`
- **Trigger:** push and pull_request to master
- **Steps:** checkout → setup Python 3.12 → pip install -r requirements.txt → compileall → pytest tests/ -v
- **Last run:** 18 August 2026 — ✅ 22 passed in 15s

---

## What to Do Next Session

### If continuing improvements:
1. Update `architecture/architecture.md` — it doesn't reflect current state (Phase 9)
2. Add knowledge files for missing roles: python, data-engineer, behavioral
   - Each file needs a `## Core Skills` section with bullet list
   - Upload to SharePoint "LearningCopilot" library after creating
3. Clean up README for portfolio (Phase 10)

### If starting Phase 8 (Teams deployment):
1. Open Copilot Studio → Channels → Microsoft Teams → Enable
2. Test the agent directly in Teams
3. Note: ngrok must be running for the backend to respond

### If adding a new role to the knowledge base:
1. Create `knowledge/<role-name>/<role>_guide.md`
2. Include `## Core Skills` section with `- Skill` bullet points
3. Upload to SharePoint "LearningCopilot"
4. Verify by asking the Copilot agent: "Prepare me for a [role] interview"
5. Run `python -m pytest` to confirm `test_load_ai_engineer_knowledge_returns_content` equivalent passes

---

## Key Decisions Made This Session

- **Single OpenAPI contract** (`interview-prep-openapi.json`) is hand-crafted and minimal — do not replace with auto-generated version from `export_openapi.py` (that generates a different schema format)
- **ngrok static domain** is free tier — if it ever changes, update the `servers` URL in both `main.py` and `interview-prep-openapi.json`, then re-import into Copilot Studio
- **Knowledge files are the source of truth** for role-specific questions — adding a new role only requires adding `.md` files, no code changes needed
- **Baby steps rule** maintained throughout — one bug at a time, verified before moving to next
