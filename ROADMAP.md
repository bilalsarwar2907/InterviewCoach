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
| 3 | ✅ **ANSWERED 26 Nov** — Phase 8 check: Teams channel **is available, no licence block**. Only condition: agent must be **published** first. Actual publish + test chat moved to after step 5 (backend must be reachable) | settles the licence question | answered; test chat after step 5 |
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
| 4a | ✅ **DONE 26 Nov** — Knowledge contract: every **active** role folder (has at least 1 `.md` file) must have a `## Core Skills` section + a test that checks them. Empty placeholder folders are skipped until filled | makes "new role = new files" a checked rule, without breaking CI on empty folders | test passes now; fails if an active role breaks the rule |
| 4b | ✅ **DONE 26 Nov** — **Scoring proof** — run 1 real question, answer it, get: score 1–5, **at least 1 strength, at least 1 weakness, max 3 feedback points** | nothing makes a score today; the schema must come from real output; fixed limits = clean Power BI data | 1 real scored answer saved as an example |
| 4c | ✅ **DONE 26 Nov** — **Session schema from 4b's real output** — date, role, experience_level, score, strengths, weaknesses, duration (adjust to what 4b shows). **One source of truth: the SharePoint list columns**, documented in `architecture.md`. No Pydantic copy (Pydantic only if B is ever built) | avoid two schemas that drift apart | list created; columns = documented schema |
| 4d | ✅ Decided 26 Nov: **option A** (Power Automate saves directly) | the design depends on it | done |
| 5 | ✅ **DONE 26 Nov** — Azure App Service instead of ngrok | stable URL before anything depends on it | agent works with your PC off |
| 6 | ✅ **DONE 27 Nov** — Phase 11: save sessions (SharePoint list first, Dataverse later). **If the save fails:** interview continues, error is logged (flow "run after: failed" branch → `SessionErrors` list), flow run history shows details | Gap #3; resilience + demo/interview talking point | 3 real sessions saved + 1 forced failure logged |
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

- **✅ Blocker solved:** the agent is a **Standard harness** (classic) agent. The new Copilot Studio (Aug 2026, "GitHub Copilot harness") cannot open it. Fix: Home → **…** (bottom of sidebar) → **Open classic experience** → Skip feedback → new tab → Agents → Interview Coach. Classic mode lasts for that browser session only — repeat each time. Agent opened 26 Nov: model "GPT Chat Latest (Oct 2026)", status **1 Warning** (probably ngrok not running — check in step 3).
- **Step 3 result:** Channels → "Microsoft 365 and Microsoft Teams" shows no licence message, only: *"You need to publish your agent before you can make it available to others."* The notes saying "needs a licence" were wrong; "one publish step" was right. Teams users may also need admin approval for wider sharing (Copilot Studio text).
- **Step 4a ✅:** Bilal wrote `tests/test_knowledge_contract.py` (loops role folders, skips empty ones, asserts `extract_skills()` is not empty). 23 tests pass. Proven to fail with a fake `python/guide.md` without Core Skills → `AssertionError: python has no Core Skills`. Commit `99cd4c9` (Bilal).
- **Step 4b ✅:** agent Instructions rewritten with TWO modes (1 = plan → uses tool; 2 = practice → no tool, scores itself). First test called the tool by mistake; fixed by the modes text + a new test session. Real result: question "supervised vs unsupervised learning", score **4/5**, 2 strengths, 1 weakness, Role + Question lines present. Small issue: lines run together in the chat (format) — fix in 4c.
- **Contributors:** all 20 commits on GitHub verified clean (no Claude author / co-author). GitHub's contributor list is cached and updates later.
- **Rule set by Bilal:** Claude may edit **text only** (docs, markdown, config notes) — **no code**. No Claude co-author line in commits. The 2 earlier commits were reworded to remove the `Co-Authored-By: Claude` line (force-push needed); file contents unchanged.

- **Step 4c ✅ (schema = single source of truth):** SharePoint site **Learning Copilot** → list **`PracticeSessions`**. Columns: `Title` (= the question), `Role` (single line of text), `Score` (number), `Strengths` (multiple lines), `Weaknesses` (multiple lines), `Created` (date, automatic). `experience_level` and `duration` left out for now — not in the agent's real output yet.

- **Step 5 ✅ (Azure App Service, 26 Nov evening):**
  - Web app **`interviewcoach-bilal`** — resource group `rg-interviewcoach`, Sweden Central, Linux, Python 3.12, plan `ASP-MoveMusic-a649` (**Free F1**, shared with an older app).
  - URL: `https://interviewcoach-bilal-efdvdcead9d8c8bw.swedencentral-01.azurewebsites.net`
  - Startup command (Configuration → Stack settings): `python -m uvicorn main:app --host 0.0.0.0 --port 8000`
  - Deploy: Deployment Center → GitHub (`master`) → Azure added `.github/workflows/master_interviewcoach-bilal.yml` (commit `03a0620`). Every push to `master` = new deploy. Auth = user-assigned identity (OIDC). First run failed with *"No subscriptions found"* (role not active yet) → **re-run** fixed it.
  - Test: `/api-info` answers from Azure ✅.
  - Bilal changed the URL ngrok → Azure in `main.py`, `interview-prep-openapi.json`, `src/interviewcoach/openapi.json` — commit `13d513c` (Bilal). 23 tests pass (`python -m pytest`).
  - Power Automate → Custom connectors → InterviewCoach → **Host** changed to the Azure host → Test: **200**, schema validation succeeded.
  - Copilot Studio: connection had to be reconnected (Open connection manager → InterviewCoach → Connect). Then the agent gave a full 7-day plan + 5 questions **with ngrok off** ✅ = done criterion met.
  - Known limit: Free F1 has no **Always on** → app sleeps after ~20 min idle, first call slow (~30 s). Upgrade to B1 only if the demo needs it (costs money).
  - Text updated by Claude: README + PROJECT.md (ngrok → Azure). `interviewcoach-minimal.json` still points to ngrok — it goes away with the Test tool.

- **Step 6 — part 1 ✅ (27 Nov, happy path):**
  - Agent flow **`Save Practice Session`** (Copilot Studio → Add a tool → Agent flow). Trigger *When an agent calls the flow* with 5 inputs: `Question` (text), `Role` (text), `Score` (number), `Strengths` (text), `Weaknesses` (text) → **SharePoint Create item** (site Learning Copilot, list `PracticeSessions`; Title←Question, Role, Score, Strengths, Weaknesses) → *Respond to the agent*. Published.
  - Added as a tool to Interview Coach. Tool description + every input got a clear name/description (otherwise the AI sees only "Text 1, Text 2…"). Completion: *Don't respond*.
  - Instructions, MODE 2: "do NOT call any tool" changed to "do NOT call the *Generate interview preparation plan* tool" + new line: after the score, call *Save Practice Session* once; tell the user only if it fails. (The old line would have blocked the save.)
  - Test: practice question on production RAG → score 4/5 → **new row in `PracticeSessions`** ✅ (1 of 3 real sessions).
  - Found: Role values differ ("Junior AI Engineer" in the old row vs "ai-engineer") → clean this before Power BI (e.g. fixed role list in the input description).
  - Warning seen: "environment has insufficient Copilot Credits" — test runs are free; check again when published.

- **Step 6 — part 2 ✅ (27 Nov, failure branch):**
  - New SharePoint list **`SessionErrors`**: `Title` (the question, cut to 250 chars), `ErrorDetails` (multiple lines), `Created` (automatic).
  - Flow `Save Practice Session` now: Create item (PracticeSessions) → **Create item 1** (SessionErrors), *run after* = **has failed + has timed out** only → **Respond to the agent**, *run after* Create item 1 = **is successful + is skipped** (so the agent always gets an answer).
  - Create item 1: Title = `take(triggerBody()?['text'], 250)`, ErrorDetails = `string(actions('Create_item')?['error'])`.
  - Forced failure test (manual flow test, 298-char question → SharePoint Title max 255): run 1 → the error branch failed too (same long Title) → fixed with `take(...)`. Run 2 → ErrorDetails empty: `outputs('Create_item')?['body']` is empty when the request is stopped before SharePoint → fixed with `actions('Create_item')?['error']`. Run 3 → **flow "ran successfully", row in SessionErrors with the full error** ✅.
  - Lesson (interview talking point): test the error path — it had 2 bugs the happy path never shows.
  - Known risk: a real question over 255 chars is **not saved** in PracticeSessions (only logged in SessionErrors). Decide: cut Title to 255 in the main Create item too?
  - Test row 1 in SessionErrors (empty ErrorDetails) is test noise — Bilal can delete it.

- **Step 6 ✅ DONE (27 Nov, 09:55):**
  - Main Create item Title changed to `take(triggerBody()?['text'], 255)` → long questions are cut and still saved (decision by Bilal). Error branch kept for all other errors.
  - 3 real practice sessions through the agent, all saved in `PracticeSessions`: 2× ai-engineer (production RAG design / RAG design + evaluation), 1× data-engineer (reliable ETL pipeline), all score 4. Plus 1 forced failure logged in `SessionErrors` = done criterion met.
  - Noticed: the strengths/weaknesses saved are the AI's own short rewording of the chat text (not word for word). Fine for Power BI.

### ▶ RESUME HERE (27 Nov, 09:55)
- Next: **step 7** — Power BI report on `PracticeSessions`: sessions done, average score, weakest skills, progress over time.
- Before Power BI: same Role spelling (row 1 says "Junior AI Engineer", others "ai-engineer") — fix row 1 by hand or filter it out.
- Still open: run-together lines in the score reply; remove the **Test** tool + `interviewcoach-minimal.json`; real .docx in SharePoint (check); **publish** agent + Teams test chat.

## Rules kept from earlier sessions
- Claude edits text only, never code. Commits have Bilal as the only author.
- Hand-written, minimal OpenAPI contract. Never the FastAPI auto-generated one.
- If Copilot Studio fails to connect → check the contract first, not the Python.
- Knowledge files = source of truth. A new role = new files, no code changes.
- Baby steps: one change, test, then the next.
