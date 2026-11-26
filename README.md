# InterviewCoach

A Microsoft Copilot Studio agent connected to a Python FastAPI backend that generates personalised interview preparation plans — including role-specific questions, skill gap analysis, and a 7-day study plan.

InterviewCoach — Microsoft Copilot Studio Agent

I built InterviewCoach by using only the built-in mechanisms of Microsoft Copilot Studio in sequence, connected to a Python FastAPI backend.

Sequence of built-in mechanisms I used:

Knowledge Base Grounding: Uploaded role-specific guides as DOCX files to SharePoint. Copilot Studio's built-in grounding engine handles chunking, embedding and retrieval automatically. I found DOCX works reliably with citations, while Markdown does not.
AI Parameter Filling: Configured the agent to extract role, experience_level, and skills from natural language without any rigid forms. This is Copilot's built-in NLU, not custom code.
REST API Tool with OpenAPI 3.0.1: Created a hand-crafted minimal OpenAPI contract (interview-prep-openapi.json) and connected it via Copilot's built-in REST API tool. The tool calls my backend through an InterviewCoach Connection.
FastAPI Backend on Azure App Service: The backend itself is simple Python FastAPI exposing /interview-prep, hosted on Azure App Service (Linux, Python 3.12, free F1) and deployed automatically from GitHub Actions on every push to master. It has 3 services — Questions, Skill Gap, and Study Plan — that read from the same knowledge base.
Flows: Used Copilot's built-in Power Automate flows.
Review Interview Plan Flow: Agent > Flow > Human Review > Output > Agent Response
Test Flow: Lightweight flow to verify agent-flow connection.
Publish: Tested in Copilot Studio test panel and published to channels. Publishing requires a Copilot Studio user licence.
I did NOT do: Custom LLM training, fine-tuning, or manual vector database creation. Everything related to LLM, RAG, chunking and embedding was handled by Copilot Studio's built-in mechanisms. I only orchestrated them in the right sequence and provided a clean API and clean DOCX knowledge.

Tech Stack: Microsoft Copilot Studio, Power Automate, FastAPI, Python, Azure App Service, GitHub Actions, OpenAPI 3.0.1, SharePoint. (ngrok only for local testing.)

---

## What It Does

You describe a role and your current skills. The agent calls the backend and returns:

- Interview questions tailored to the role and experience level (technical, behavioural, and follow-up)
- Skill gap analysis showing matched skills vs. missing skills, prioritised by importance
- A 7-day study plan to close the gaps before the interview

---

## Architecture

```
User
  |
Microsoft Copilot Studio (Interview Coach Agent)
  |
REST API Tool (OpenAPI 3.0.1 contract)
  |
InterviewCoach Connection
  |
Python FastAPI Backend (Azure App Service)
  |
Services: Questions, Skill Gap, Study Plan
  |
Knowledge Base (role-specific DOCX guides)
```

The agent uses AI parameter filling — it extracts `role`, `experience_level`, and `skills` from natural language without rigid forms.

---

## Project Structure

```
InterviewCoach/
|
|-- main.py                        # FastAPI app entry point
|-- requirements.txt
|-- README.md
|-- interview-prep-openapi.json    # OpenAPI contract used by Copilot Studio
|
|-- src/
|   |-- interviewcoach/
|       |-- models/
|       |   |-- interview_prep_request.py
|       |   |-- interview_request.py
|       |   |-- skill_gap_request.py
|       |   |-- study_plan_request.py
|       |   |-- study_plan_from_skills_request.py
|       |
|       |-- services/
|           |-- interview_prep_service.py
|           |-- interview_service.py
|           |-- skill_gap_service.py
|           |-- study_plan_service.py
|           |-- knowledge_service.py
|
|-- knowledge/
|   |-- ai-engineer/
|   |   |-- AI_Engineer_Interview_Guide.docx
|   |   |-- copilot_studio.md
|   |   |-- azure_ai_search.md
|   |-- cloud-engineer/
|   |-- python/
|   |-- behavioral/
|   |-- data-engineer/
|
|-- tests/
|-- docs/
|-- architecture/
```

---

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Root |
| GET | `/health` | Health check |
| GET | `/api-info` | API metadata |
| GET | `/knowledge/{role}` | Knowledge base for a role |
| POST | `/interview/questions` | Generate interview questions |
| POST | `/skill-gap` | Skill gap analysis |
| POST | `/study-plan` | Generate study plan |
| POST | `/study-plan-from-skills` | Study plan from skills list |
| POST | `/interview-prep` | Full preparation plan (primary endpoint) |

### Primary Endpoint

`POST /interview-prep`

Request:
```json
{
  "role": "Junior AI Engineer",
  "experience_level": "Junior",
  "skills": ["Python", "Azure"]
}
```

Response:
```json
{
  "role": "Junior AI Engineer",
  "questions": ["..."],
  "skill_gap": {
    "matched_skills": [],
    "missing_skills": []
  },
  "study_plan": {
    "role": "Junior AI Engineer",
    "plan": []
  }
}
```

---

## Local Setup

### Prerequisites

- Python 3.10+
- ngrok account (free tier works)
- Microsoft Copilot Studio access

### Run the Backend

```bash
git clone https://github.com/bilalsarwar2907/InterviewCoach.git
cd InterviewCoach

pip install -r requirements.txt

uvicorn main:app --reload --port 8000
```

Expose locally via ngrok:

```bash
ngrok http 8000
```

Swagger UI: `http://localhost:8000/docs`

### Test the API

```bash
curl -X POST http://localhost:8000/interview-prep \
  -H "Content-Type: application/json" \
  -d '{"role": "Python Developer", "experience_level": "Mid", "skills": ["Python", "FastAPI"]}'
```

---

## Copilot Studio Setup

### OpenAPI Contract

Use the hand-crafted minimal contract (`interview-prep-openapi.json`) — not the auto-generated FastAPI schema. The generated schema does not work reliably with Copilot Studio's REST API tool importer.

The contract must have a meaningful `operationId`, clear field descriptions, and a simple request/response structure.

### REST API Tool

1. Go to Tools > New tool > REST API
2. Upload `interview-prep-openapi.json`
3. Complete the API Plugin Details and Authentication steps
4. Select the `GenerateInterviewPrep` operation
5. Enable "Dynamically fill with AI" for all parameters
6. Publish

### Knowledge Base

Knowledge files must be in DOCX format. Markdown files uploaded to SharePoint do not reliably trigger retrieval — the agent answers from general knowledge with no citation. Converting to `.docx` fixes this.

---

## Agent Flows

Two flows are published:

**Review Interview Plan** — routes generated plans through a human review step before delivery. Uses the pattern: Agent > Flow > Request Information > Human Review > Flow Output > Agent Response.

**Test Flow** — lightweight flow used to verify the agent-flow connection during development.

---

## Key Findings

**Minimal OpenAPI contract** — start with a single endpoint and a hand-crafted contract. Add complexity only after the base case works. The failure point is almost always the contract, not the backend.

**DOCX for knowledge files** — Markdown is not reliably retrieved by Copilot Studio's grounding engine. Always use `.docx` and verify citations appear in responses.

**Hosting** — the backend runs on Azure App Service (stable URL, works with the PC off). The free F1 plan has no "Always on", so the app sleeps after ~20 min idle and the first request after that is slow (~30 s). ngrok is only needed for local testing; its URL changes on restart.

**Publish** — checked 26 Nov 2026: the Teams channel shows no licence block in the zealand.dk environment, only "publish your agent first". Wider sharing in Teams may need admin approval.

---

## Author

H.M. Bilal Sarwar  
Copenhagen, Denmark  
[github.com/bilalsarwar2907](https://github.com/bilalsarwar2907)
