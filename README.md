# InterviewCoach

A Microsoft Copilot Studio agent connected to a Python FastAPI backend that generates personalised interview preparation plans — including role-specific questions, skill gap analysis, and a 7-day study plan.

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
Python FastAPI Backend (via ngrok)
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

**ngrok URL changes on restart** — the OpenAPI contract and Copilot Studio connection must be updated each time ngrok restarts. For persistent use, deploy the backend to a stable URL.

**Publish requires a licence** — publishing an agent to channels such as Teams requires a Copilot Studio user licence. Building, testing, and running the agent in the test panel works without it.

---

## Author

H.M. Bilal Sarwar  
Copenhagen, Denmark  
[github.com/bilalsarwar2907](https://github.com/bilalsarwar2907)
