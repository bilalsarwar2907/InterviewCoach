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
| 8 | Microsoft Teams deployment | ❌ Not done yet | No licence block (answered 26 Nov) — publish + Teams test chat still to do |
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
| 3 | ✅ **ANSWERED 26 Nov** — Phase 8 check: Teams is available, no licence needed. Agent opens in Classic experience. Publish + test chat still to do | 5-min task, settles the licence question | 1 test chat works |
| 4 | **Architecture hardening** — see 4a–4d (order: evidence first, then schema) | protect the design before the first data is stored | all parts done, tests pass |
| 4a | ✅ **DONE 26 Nov** — Knowledge contract: every **active** role folder (has at least 1 `.md` file) must have a `## Core Skills` section + a test that checks them. Empty placeholder folders are skipped until filled | makes "new role = new files" a checked rule, without breaking CI on empty folders | test passes now; fails if an active role breaks the rule |
| 4b | ✅ **DONE 26 Nov** — **Scoring proof** — run 1 real question, answer it, get: score 1–5, **at least 1 strength, at least 1 weakness, max 3 feedback points** | nothing makes a score today; the schema must come from real output; fixed limits = clean Power BI data | 1 real scored answer saved as an example |
| 4c | ✅ **DONE 26 Nov** — **Session schema from 4b's real output** — date, role, experience_level, score, strengths, weaknesses, duration (adjust to what 4b shows). **One source of truth: the SharePoint list columns**, documented in `architecture.md`. No Pydantic copy (Pydantic only if B is ever built) | avoid two schemas that drift apart | list created; columns = documented schema |
| 4d | ✅ Decided 26 Nov: **option A** (Power Automate saves directly) | the design depends on it | done |
| 5 | ✅ **DONE 26 Nov** — Azure App Service instead of ngrok | stable URL before anything depends on it | agent works with your PC off |
| 6 | ✅ **DONE 27 Nov** — Phase 11: save sessions (SharePoint list first, Dataverse later). **If the save fails:** interview continues, error is logged (flow "run after: failed" branch → `SessionErrors` list), flow run history shows details | Gap #3; resilience + demo/interview talking point | 3 real sessions saved + 1 forced failure logged |
| 7 | ✅ **DONE 27 Nov** — Phase 12: Power BI — sessions done, average score, weakest skills, progress over time (`powerbi/InterviewCoach.pbix`) | Gap #3 | report runs, you can demo it |
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

## Part D — Steps 5–6 in simple words (no code, only Microsoft websites)

### 1. The 4 places

They are all Microsoft websites. One login: zealand.dk. Not 4 separate systems.

- **Copilot Studio = the Agent / the Boss**
  It talks to you. It asks the question. It gives the score.
  It can decide, but it cannot write anything down.

- **Power Automate = the Helper**
  It does the same steps every time.
  It is the hands. It writes for the boss.

- **SharePoint = the Notebook**
  It is just a list. Like a table in Excel, but in the cloud.
  This is where the notes live.

- **Azure = the Computer in the Cloud**
  It runs my Python code.
  Before, the code ran on my PC (ngrok). Now it runs here, so my PC can be off.

### 2. Why do we need all of them?

The Agent can talk and score, but it **cannot write a row in a table on its own.**

> **Agent decides → Helper does → Notebook keeps.**

Agent says: *"Save this score."*
Helper writes it.
Notebook keeps it.

Without the Helper, the score is said once in the chat and then lost.

### 3. How are they linked?

**Agent → Helper**
The flow starts with *"When an agent calls the flow"* and ends with *"Respond to the agent"*.
That is how the boss calls the helper, and how the helper answers back.

**Helper → Notebook**
The flow action is *"Create item"*.
Create item = write one new row in the list `PracticeSessions`.

**Agent → Computer in the Cloud**
The link is called a *custom connector*.
Its **Host** is just my Azure URL = the address of the computer.

---

### 4. What I did, in order — practical clicks

#### Part A — Move the code to the Computer in the Cloud (step 5)

1. **Azure portal → Subscriptions**
   Checked: *Azure for Students*, Active, I am Owner.

2. **Azure → Create → Web App**
   - Name: `interviewcoach-bilal`
   - Code, **Python 3.12**, **Linux**, **Sweden Central**
   - Plan: the free one (**F1**), shared with an older app
   - Folder (resource group): `rg-interviewcoach`

3. **Web App → Configuration → Stack settings → Startup command**
   ```
   python -m uvicorn main:app --host 0.0.0.0 --port 8000
   ```
   = "how to start my app". `main:app` = the `app` in `main.py`.

4. **Web App → Deployment Center → GitHub**
   - Repo `InterviewCoach`, branch `master`
   - Azure added a file `.github/workflows/...yml` to my repo → I did `git pull`.
   - Now every `git push` = new version on Azure automatically.
   - First run failed: *"No subscriptions found"* → clicked **Re-run failed jobs** → OK.

5. **Browser test**
   Opened `<Azure URL>/api-info` → got `{"status": "ready"}` ✅

6. **My code (I did it myself)**
   Changed the URL from ngrok to Azure in 3 files. Tests: `python -m pytest` → 23 passed. Pushed.

7. **Power Automate → Custom connectors → InterviewCoach → Edit**
   - Changed **Host** to the Azure host → Update → **Test** → **200** ✅

8. **Copilot Studio → the agent**
   It asked to reconnect → *Open connection manager* → InterviewCoach → **Connect**.

9. **Final test**
   ngrok **off**, PC code **off** → asked the agent for a plan → full 7-day plan ✅

#### Part B — Make the Notebook (SharePoint)

10. **SharePoint → site Learning Copilot → New → List → Blank list** → name `PracticeSessions`
11. **Add columns:**
    - `Title` (already there) = the question
    - `Role` = single line of text
    - `Score` = number
    - `Strengths` = multiple lines of text
    - `Weaknesses` = multiple lines of text
    - `Created` = automatic date (already there)

#### Part C — Make the Helper (Power Automate)

12. **Copilot Studio** → open the agent (classic experience) → **Tools → + Add a tool → Agent flow**
    → this opens the Power Automate editor.
    *(Agent flow, not the plain SharePoint tool — a flow can also have a "what if it fails" path.)*

13. **First box: "When an agent calls the flow"** → add 5 inputs:
    | Input | Type |
    |---|---|
    | Question | Text |
    | Role | Text |
    | Score | Number |
    | Strengths | Text |
    | Weaknesses | Text |
    = the empty fields on the form the boss fills in.

14. **+ New step → SharePoint → Create item**
    - Site: **Learning Copilot**
    - List: **PracticeSessions**
    - Fill each column with the ⚡ input of the same name:
      Title ← Question, Role ← Role, Score ← Score, Strengths ← Strengths, Weaknesses ← Weaknesses

15. **+ New step → Respond to the agent**
    = the helper says "done" back to the boss.

16. Name the flow **Save Practice Session** + short description → **Save draft** → **Publish**.

#### Part D — Tell the Boss to use the Helper (Copilot Studio)

17. **Agent → Tools → Add a tool → Flow → Save Practice Session → Add and configure**

18. **Tool description** (the boss reads this to know WHEN to use it):
    *"Call once after you score an answer in practice mode. Never in plan mode."*

19. **Each input → Customize** → give a real name + a description.
    Without this the AI only sees "Text 1, Text 2" and puts the wrong values in.

20. **Completion → Don't respond** (the user already got the score in the chat).

21. **Instructions → MODE 2 (practice)**
    - Old line: "do NOT call any tool" → that **blocked** the save.
    - New line: "do NOT call the *Generate interview preparation plan* tool".
    - Added: "After the score, call *Save Practice Session* once. Tell the user only if it fails."

22. **Test:** answered a practice question → score 4/5 → **new row in PracticeSessions** ✅

#### Part E — What if writing fails? (second notebook)

23. **SharePoint → new list `SessionErrors`**
    - `Title` = the question
    - `ErrorDetails` = multiple lines of text

24. **Power Automate → open Save Practice Session → + New step → Create item** (it is called *Create item 1*)
    - List: **SessionErrors**
    - **… → Settings → Run after** → tick only **has failed** + **has timed out**
    = "only write here if the first write broke".

25. **Respond to the agent → Run after** → tick **is successful** + **is skipped**
    = the boss always gets an answer.
    (When all is OK, the error step is *skipped* → without "is skipped" the boss would wait forever.)

26. **Break it on purpose** — manual flow test with a **298-letter** question (the notebook Title takes max **255**):
    - Run 1: the error write **also** failed (same too-long Title)
      → fix in Create item 1, Title = **fx** `take(triggerBody()?['text'], 250)` = first 250 letters.
    - Run 2: error row was there, but **ErrorDetails was empty**
      → fix, ErrorDetails = **fx** `string(actions('Create_item')?['error'])` = the error of the first step, as text.
    - Run 3: flow OK, error row with the full error ✅

27. **Main Create item** → Title also = **fx** `take(triggerBody()?['text'], 255)`
    → long real questions are cut and still saved.

28. **3 real sessions** through the agent (2× ai-engineer, 1× data-engineer) → all 3 rows saved ✅ = step 6 done.

> ⚠️ Formulas must show as a **purple fx pill**. Typed as plain text = saved as words, not calculated.

---

### 5. What if it fails?

If the Helper cannot write in the first notebook, it writes in the second notebook, `SessionErrors`.

The interview does **not** stop. The Agent still talks to you.

That is why I tested the fail on purpose — and found 2 bugs that the normal test never shows.

### 6. The order to use next time

1. **Notebook first** (SharePoint list) — decide the columns from 1 real output.
2. **Computer in the cloud** (Azure) — if there is code the agent calls.
3. **Helper** (Power Automate flow) — inputs → Create item → Respond to the agent → Publish.
4. **Tell the boss** (Copilot Studio) — add tool, describe it + every input, fix the Instructions.
5. **Test** — 1 real row.
6. **Second notebook + fail path** — run after: has failed.
7. **Break it on purpose** — test, fix, test again.
8. **Clean the data** — then Power BI.

Why this order: each step needs the one before. The helper cannot pick a notebook that does not exist. The boss cannot call a helper that is not published.

### In one sentence

> **First the notebook (SharePoint), then the helper (Power Automate), then you tell the boss (Agent) to use the helper.**

## Step 7 ✅ DONE — Power BI report in simple words (27 Nov)

### What is Power BI, in simple words?

Power BI is just a **window that looks at the Notebook.**

It does not decide. It does not save. It just shows what is already in SharePoint.

> **Boss scores → Helper saves → Notebook keeps → Power BI shows**

If the Notebook changes, Power BI changes. Nothing else.

### What I did, in order — practical clicks

**1. Clean the Notebook first — this was important**
- Row 1 said `"Junior AI Engineer"`, the others said `"ai-engineer"`.
- Same role, two spellings = Power BI thinks they are 2 different roles.
- Fix: in SharePoint → PracticeSessions → Row 1 → Role = `ai-engineer` → Save. (Done **before** opening Power BI.)
- Now there are only 2 roles: `ai-engineer` and `data-engineer`.

> Lesson: Clean the Notebook first, then build the report. If the Notebook is dirty, the report is dirty.

**2. Open Power BI Desktop and connect to the Notebook**
- Sign in with my **zealand.dk** account (same login as SharePoint).
- **Home → Get data ▾ → More… →** search **SharePoint Online List → Connect**
- Site URL: `https://zealanddk.sharepoint.com/sites/LearningCopilot`
  (only up to the site name — cut off `/SitePages/...`)
- Implementation: **2.0 → OK**
- Sign-in window: left side **Microsoft account → Sign in → Connect** (not Anonymous)
- Navigator: tick **PracticeSessions** only → **Transform Data** (not Load)

**3. Clean the columns in Power Query (the cleaning room)**
- SharePoint brings many hidden extra columns (ID, Version, Author …).
- **Choose Columns** → untick *(Select All Columns)* → tick only `Title, Role, Score, Strengths, Weaknesses, Created` → OK
- `Score` showed **ABC** = text. Text cannot be averaged.
  → click **ABC** on the Score header → **Whole Number** → now **123**.
- Trap I hit: I changed **Role** to a number by mistake → Role became errors → deleted that step (X in Applied Steps).
- Trap 2: *Remove Errors* deletes whole **rows** — check you still have all rows after.
- **Close & Apply** → the table appears in the **Data** pane.

**4. Make the cards — this was the difficult part**

A Card is just one big number. But Power BI does not know *which* number you want.

You must tell it, by dragging the right column into **Value**, and setting the right maths.

Card 1 — **Count of Title** (sessions done)
- Click an empty spot → Visual: **Card** (⚡123 icon, under the pie)
- Drag: `Title` into **Value** (not Categories — there it shows no Count)
- Click **⌄** next to Title → **Count** (not Count Distinct)
- Why Title? Every row has a Title = every row is one session.
- Result then: **4**

Card 2 — **Average of Score**
- Click an empty spot → Visual: **Card**
- Drag: `Score` into **Value**
- It says **Sum** by default → **⌄ → Average**
- If you leave it on Sum, you get 16 (4+4+4+4), not 4,00. That was the trap.
- Result then: **4,00**

> Why it was difficult: The Card does not match the column by itself. You have to drag the column AND tell Power BI: Average or Count or Sum. If the maths is wrong, the Card is wrong, even if the Notebook is right.

**5. Make the bar chart — Average Score by Role**
- Visual: **Clustered bar chart** (1st icon, top left)
- Y-axis: `Role`
- X-axis: `Score` → **Average of Score**
- Shortest bar = weakest role.

**6. Make the Weaknesses table**
- Visual: **Table** (plain grid icon)
- Drag: `Role` + `Weaknesses` into **Columns**
- Weaknesses is free text — Power BI cannot count sentences, so I read them here.

**7. Make the line chart — Average Score by Created**
- Visual: **Line chart** (row 2, 1st icon)
- X-axis: `Created` → **⌄ → Created** (not *Date Hierarchy* — that shows "by Year" = 1 dot)
- Y-axis: `Score` → **Average of Score**
- Result then: flat line at 4.

**8. Save**
- **Ctrl + S** → *Browse this device* → `C:\Users\biges\InterviewCoach\powerbi\InterviewCoach.pbix`
- No need to *Upload to OneDrive*.

### The test — 1 new answer changed every chart

Before the test:
- Sessions: 4
- Average: 4,00

I answered 1 more practice question (data-engineer, weak answer on purpose). I got score **2**.
Then in Power BI: **Home → Refresh**.

| Chart | Before | After |
|---|---|---|
| Sessions done (Count of Title) | 4 | **5** ✅ |
| Average score | 4,00 | **3,60** ✅ |
| Data-engineer bar | 4 | **3** ✅ |
| Line chart | flat at 4 | **drops to 2** ✅ |
| Weaknesses table | 4 rows | **5 rows** ✅ |

Maths: 4 + 4 + 4 + 4 = 16. 16 + 2 = 18. 18 ÷ 5 = **3,60**.

I did not type any number in Power BI. I just answered, the Boss scored, the Helper saved, the Notebook kept, and Power BI showed it.

Note: Power BI Desktop only updates when I click **Refresh**. Auto refresh needs Publish to Power BI Service — later, optional.

### In one sentence

> **One new answer changed every chart — so the whole chain works, from end to end.**

### Interview line 🎤

> "Every practice answer is scored by the agent, saved by a Power Automate flow into SharePoint, and shown in a Power BI report. I tested it end to end: one new answer changed every chart. The hardest part was the Cards — I had to match each Card to the right SharePoint column and set Average vs Count by hand, otherwise Power BI shows the wrong number."

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

### 27 Nov 2026 (10:15)
- **Docs:** added **Part D** — steps 5–6 in simple words (boss / helper / notebook), with every practical click in order, the fail path, and the order to use next time. Text only (Claude).

### 27 Nov 2026 (11:02)
- **Data cleaned:** row 1 in `PracticeSessions` Role changed "Junior AI Engineer" → `ai-engineer` (by Bilal). All 4 rows now use `ai-engineer` / `data-engineer`. Ready for Power BI.
- **Roadmap:** 2 stale lines fixed (Part A row 8, Part C step 3) — no longer say "blocked" / "notes disagree".

### 27 Nov 2026 (11:45) — Step 7 started (Power BI)
- **Connected:** Power BI Desktop → Get data → More… → **SharePoint Online List** → site `https://zealanddk.sharepoint.com/sites/LearningCopilot` (cut off `/SitePages/...`) → implementation **2.0** → sign in with **Microsoft account** → Navigator → tick **PracticeSessions** → **Transform Data**.
- **Cleaned in Power Query:** Choose Columns → kept only Title, Role, Score, Strengths, Weaknesses, Created. Score type **ABC → Whole Number (123)** so it can be averaged. Close & Apply.
  - Mistake + lesson: first changed **Role** to a number by accident → Role became errors → removed that step. "Remove Errors" deletes whole **rows** — check the row count after.
- **Card 1 — Sessions done = 4:** Card visual → Title in **Value** (not Categories) → ⌄ → **Count** (not Count Distinct).
- Saved: `powerbi/InterviewCoach.pbix`.

### 27 Nov 2026 (13:15) — Step 7: all 4 visuals built
- **Card 2 — Average score = 4,00:** Card → drag Score into **Value** → ⌄ → **Average** (default was Sum = 16).
- **Weakest skills (2 visuals):** Weaknesses is free text → Power BI cannot count it. So: (a) **Clustered bar chart** Role (Y-axis) × Average of Score (X-axis) → shortest bar = weakest role; (b) **Table** Role + Weaknesses → read what to improve.
- **Progress over time:** **Line chart** Created (X-axis) × Average of Score (Y-axis). X-axis ⌄ → **Created** instead of *Date Hierarchy* (otherwise "by Year" = 1 dot). Flat line at 4 today — it moves when more sessions are saved.
- Lesson: Power BI guesses the summary (Sum, First, Date Hierarchy). Always check the ⌄ menu.

### 27 Nov 2026 (13:20) — Step 7 ✅ DONE
- All concrete steps (clicks, traps, test table): see section **"Step 7 ✅ DONE — Power BI report in simple words"** above.
- Test result: 1 new answer (score 2) → Sessions 4 → 5, Average 4,00 → 3,60 → whole chain works.

### ▶ RESUME HERE (27 Nov, 13:20)
- Next: **step 8** — Behavioral role, knowledge files only (zero Python changes). Or first clear the open items below.
- Still open: run-together lines in the score reply; remove the **Test** tool + `interviewcoach-minimal.json`; real .docx in SharePoint (check); **publish** agent + Teams test chat.

## Rules kept from earlier sessions
- Claude edits text only, never code. Commits have Bilal as the only author.
- Hand-written, minimal OpenAPI contract. Never the FastAPI auto-generated one.
- If Copilot Studio fails to connect → check the contract first, not the Python.
- Knowledge files = source of truth. A new role = new files, no code changes.
- Baby steps: one change, test, then the next.
