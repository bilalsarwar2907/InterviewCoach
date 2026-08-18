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
