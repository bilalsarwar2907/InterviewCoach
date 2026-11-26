# InterviewCoach — Factual Roadmap
Rebuilt 26 Nov 2026 from: git history (16 local commits + 1 on GitHub), PROJECT.md,
session summaries (12 Aug, 18 Aug), COPILOT_STUDIO_SETUP_SUMMARY.md, Gap_Roadmap_NOV26_2026.md.
Only facts from those sources. "Suggested" items are new.

## Part A — What actually happened

| Phase | What | Status | When (evidence) |
|---|---|---|---|
| 0 | Project scaffold (FastAPI, service layers) | ✅ Done | 3 Aug — commit "Phase 0 project scaffold" |
| 1 | Knowledge base (markdown per role) + SharePoint "LearningCopilot" | ✅ Done | 3 Aug — commit "Phase 3 knowledge base created" |
| 2 | Copilot Studio agent (zealand.dk environment) | ✅ Done | Aug — setup summary |
| 3 | Ground agent with SharePoint | ✅ Done | Aug — status "Ready" |
| 4 | Interview question generator | ✅ Done | 4 Aug — commits |
| 5 | Skill gap analyzer | ✅ Done | 4 Aug — commits |
| 6 | 7-day study planner | ✅ Done | 4 Aug built, 18 Aug fixed (7-day cap) |
| — | ngrok tunnel + CORS | ✅ Done | 4–5 Aug — commits |
| — | REST API tool in Copilot Studio (hand-written OpenAPI) | ✅ Done | 5 Aug — "complete end-to-end Copilot Studio REST API integration" |
| 7 | Power Automate (2 flows: Review Interview Plan, Test Flow) | ✅ Done | Aug — both Published |
| — | Code review: 8 bugs + 6 missing items found | ✅ Done | 12 Aug — SESSION_SUMMARY.md |
| — | 10 bugs fixed, 22 tests, CI runs pytest | ✅ Done | 18 Aug — commit "fix: all bugs fixed..." |
| — | README expanded | ✅ Done | 23 Sep — GitHub only (not pulled locally) |
| 8 | Microsoft Teams deployment | ❌ Not done | Notes disagree: "one publish step" vs "needs Copilot Studio licence" |
| 9 | Update architecture.md | ❌ Not done | listed as pending |
| 10 | Portfolio packaging (README, screenshots, demo video) | ⚠️ Partly | README done; screenshots exist locally only; no video |
| — | Knowledge for python / data-engineer / behavioral | ❌ Empty folders | still empty 26 Nov |

## Part B — State found on 26 Nov 2026 (before step 1; see Progress log for what was fixed)
- Local folder is 1 commit behind GitHub (missing the 23 Sep README commit).
- Local git shows 32 "modified" files, but +1866 / −1866 lines → line endings only (Windows CRLF), no real changes.
- `screenshots/` is on your PC only, not on GitHub.
- `knowledge/ai-engineer/AI_Engineer_Interview_Guide.docx` is byte-identical to the `.md` next to it → it is a renamed text file, not a real Word file.
- 3 OpenAPI files: `interview-prep-openapi.json` (the one Copilot Studio uses — keep), `openapi-export.json` and `interviewcoach-minimal.json` (probably not used).

## Part C — Plan (v3 FINAL, 26 Nov 2026 — after 3 external reviews. No more reviews: execute.)

| # | Step | Why | Done when |
|---|---|---|---|
| 1 | ✅ **DONE 26 Nov** — Git sync: `git pull` + `.gitattributes` (`* text=auto`) | clean start | `git status` shows nothing |
| 2 | ⚠️ **MOSTLY DONE 26 Nov** — Cleanup: verify which OpenAPI file Copilot Studio uses, remove unused ones, replace fake `.docx`. Left: `interviewcoach-minimal.json` (Test tool still uses it) + upload the real .docx to SharePoint | less confusion; SharePoint needs real DOCX | verified + 1 contract left + real .docx uploaded |
| 3 | 🚫 **BLOCKED 26 Nov** — Phase 8 check: Teams or demo website channel. Agent will not open (see Progress log) | 5-min task, settles the licence question | 1 test chat works |
| 4 | **Architecture hardening** — see 4a–4d (order: evidence first, then schema) | protect the design before the first data is stored | all parts done, tests pass |
| 4a | Knowledge contract: every **active** role folder (has at least 1 `.md` file) must have a `## Core Skills` section + a test that checks them. Empty placeholder folders are skipped until filled | makes "new role = new files" a checked rule, without breaking CI on empty folders | test passes now; fails if an active role breaks the rule |
| 4b | **Scoring proof** — run 1 real question, answer it, get: score 1–5, **at least 1 strength, at least 1 weakness, max 3 feedback points** | nothing makes a score today; the schema must come from real output; fixed limits = clean Power BI data | 1 real scored answer saved as an example |
| 4c | **Session schema from 4b's real output** — date, role, experience_level, score, strengths, weaknesses, duration (adjust to what 4b shows). **One source of truth: the SharePoint list columns**, documented in `architecture.md`. No Pydantic copy (Pydantic only if B is ever built) | avoid two schemas that drift apart | list created; columns = documented schema |
| 4d | ✅ Decided 26 Nov: **option A** (Power Automate saves directly) | the design depends on it | done |
| 5 | Azure App Service instead of ngrok | stable URL before anything depends on it | agent works with your PC off |
| 6 | Phase 11: save sessions (SharePoint list first, Dataverse later). **If the save fails:** interview continues, error is logged (flow "run after: failed" branch → `SessionErrors` list), flow run history shows details | Gap #3; resilience + demo/interview talking point | 3 real sessions saved + 1 forced failure logged |
| 7 | Phase 12: Power BI — sessions done, average score, weakest skills, progress over time | Gap #3 | report runs, you can demo it |
| 8 | Behavioral role — knowledge files only | proves the rule | works with **zero** Python changes. If code changes seem needed → find out why the role breaks the knowledge contract (4a) |
| 9 | Update `architecture.md` | Phase 9 | diagram matches the code |
| 10 | Packaging: screenshots, 2-min video, README | Phase 10 | README shows flow + report |
| 11 | 1-page sheet: system flow + patterns: **Facade (used today)**, Adapter (only if 12b) | Gap #1 | you explain it in 2 min, no notes |
| 12a | **Architecture comparison A vs B (no code)** — complexity, maintainability, SOLID impact, when B is worth it | architecture talk without building twice | 1-page comparison in `architecture.md` |
| 12b | *Optional learning exercise — not a success criterion.* Build B on a separate git branch (`SessionStore` + `SharePointSessionStore` Adapter). `main` keeps A | course practice (Advanced Software Construction) | — |

### Decision (step 4d) — ✅ A chosen 26 Nov; B = comparison (12a), build optional (12b)
- **A — Power Automate saves directly** (Copilot → flow → SharePoint list). No Python change. Shows Power Platform (the Gap #3 goal). No `SessionStore` needed.
- **B — Python saves** (Copilot → new `/sessions` endpoint → `SessionStore` → SharePoint). More code. Then `SessionStore` (interface) + `SharePointSessionStore` (Adapter) make sense.
- Suggested: **A first**. Choose B only if you also want the SOLID/Adapter story for Advanced Software Construction.

### GoF patterns — what fits this code
| Pattern | Verdict | Reason (from the real code, 272 lines) |
|---|---|---|
| Facade | ✅ **used today** | `interview_prep_service.generate_interview_prep()` hides 3 services (questions, skill gap, study plan) behind 1 call; the OpenAPI contract exposes only that 1 endpoint (`/interview-prep`) to Copilot Studio |
| Adapter | ✅ only if 12b | wraps SharePoint/Dataverse so only the adapter changes |
| Strategy | ❌ not now | roles differ in **data** (.md files), not in classes = *data-driven variation*, not Strategy. Strategy only if you later add real interchangeable scoring classes |
| Factory | ❌ not now | only useful together with Strategy |
| Observer, Repository + Event Bus + DTO layers | ❌ skip | too much for a portfolio project |

### Review notes
**v3 final (3rd review):** 4a skips empty placeholder folders; 4b fixed feedback limits; Facade added (already in code); 12b marked optional, not a success criterion.

**v3 (26 Nov, 2nd review):** step 4 reordered (scoring proof → schema); one schema source (SharePoint columns); step 2 verify-first; save-failure handling in Phase 11; step 8 wording fixed; Strategy renamed "data-driven variation"; step 12 split into comparison (12a) + optional branch build (12b).

**v2 (what changed from v1):**
- Accepted: architecture step before saving data; stable session schema; knowledge contract; Azure before Phase 11; Phase 8 moved early; fix fake .docx; no Observer.
- Changed: Strategy/Factory put on hold (code is already data-driven); `SessionStore` only if Python does the saving; added the missing **scoring step**.

## Progress log (newest at the bottom — check here what was done)

### 26 Nov 2026
- **Cleanup of folders:** 58 duplicate/junk files moved from `C:\Users\biges\Claude`, `...\OneDrive\Desktop\session summeries` and this repo into `_to_delete\` (list + original paths in `_to_delete\MANIFEST.md`). `_to_delete/` is ignored by git (`.git/info/exclude`). Delete it by hand when happy.
- **Roadmap:** this file created from git history + session summaries; reviewed 3 times → v3 FINAL. Old versions in `_to_delete\InterviewCoach\`.
- **Step 4d decided:** option A (Power Automate saves sessions).
- **Step 1 ✅:** added `.gitattributes`; the 32 "modified" files were only CRLF line endings → now clean. Pulled the 23 Sep README commit. Commit `9f71c6e`, pushed by Bilal.
- **Step 2 — verification (Power Automate → Custom connectors, viewed only, nothing saved):**
  | Connector / tool | Action | File |
  |---|---|---|
  | InterviewCoach | `GenerateInterviewPrep` (POST /interview-prep) | `interview-prep-openapi.json` ✅ |
  | Test | `ApiInfo` (GET /api-info) | `interviewcoach-minimal.json` (still in use) |
  | — | — | `openapi-export.json` → used by nothing |
- **Step 2 — actions:** `openapi-export.json` removed from git (copy in `_to_delete`) and added to `.gitignore` (it is regenerated by `export_openapi.py`). Fake `AI_Engineer_Interview_Guide.docx` (was plain text) replaced with a real Word file made from the `.md` (pandoc). Fake copy in `_to_delete`.
- **Step 2 — still open:** (a) upload the new real .docx to SharePoint "LearningCopilot" if the copy there is not a real Word file; (b) remove the Test tool + `interviewcoach-minimal.json` together, once the agent opens.
- **🚫 Blocker found:** Copilot Studio agent "Interview Coach" shows "Something went wrong — we couldn't load Copilot Studio" when opened. New agents and the 2 workflows (Review Interview Plan, Test Flow — both Published) load fine. Agent status = **Draft** (never published). Copilot Studio has a new UI ("agent harness: Standard"); the agent was built in the old UI in Aug — possible cause, not confirmed. This blocks step 3 and all Copilot Studio work.

- **Rule set by Bilal:** Claude may edit **text only** (docs, markdown, config notes) — **no code**. No Claude co-author line in commits. The 2 earlier commits were reworded to remove the `Co-Authored-By: Claude` line (force-push needed); file contents unchanged.

## Rules kept from earlier sessions
- Claude edits text only, never code. Commits have Bilal as the only author.
- Hand-written, minimal OpenAPI contract. Never the FastAPI auto-generated one.
- If Copilot Studio fails to connect → check the contract first, not the Python.
- Knowledge files = source of truth. A new role = new files, no code changes.
- Baby steps: one change, test, then the next.
