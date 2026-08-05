import sys
from pathlib import Path

from fastapi import FastAPI

sys.path.append(str(Path(__file__).resolve().parent / "src"))

from interviewcoach.models.interview_request import InterviewRequest
from interviewcoach.services.interview_service import generate_questions
from interviewcoach.services.knowledge_service import load_role_knowledge
from interviewcoach.models.skill_gap_request import SkillGapRequest
from interviewcoach.services.skill_gap_service import analyze_skill_gap
from interviewcoach.models.study_plan_request import StudyPlanRequest
from interviewcoach.services.study_plan_service import generate_study_plan
from interviewcoach.models.interview_prep_request import InterviewPrepRequest
from interviewcoach.services.interview_prep_service import generate_interview_prep
from interviewcoach.models.study_plan_from_skills_request import (
    StudyPlanFromSkillsRequest
)

from interviewcoach.services.study_plan_service import (
    generate_study_plan_from_skills
)
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="InterviewCoach",
    version="0.1.0",
    servers=[
        {
            "url": "https://protozoan-ripcord-flying.ngrok-free.dev"
        }
    ]
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get("/")
def root():
    return {
        "status": "ok",
        "service": "InterviewCoach",
        "version": "0.1.0"
    }


@app.get("/health")
def health():
    return {
        "healthy": True
    }


@app.post("/interview/questions")
def interview_questions(request: InterviewRequest):
    return {
        "role": request.role,
        "questions": generate_questions(
            request.role,
            request.experience_level
        )
    }


@app.get("/knowledge/{role}")
def get_knowledge(role: str):
    role_name = role.replace("-", " ").title()

    return {
        "role": role_name,
        "content": load_role_knowledge(role_name)
    }

@app.post("/skill-gap")
def skill_gap(request: SkillGapRequest):

    return analyze_skill_gap(
        request.role,
        request.skills
    )

@app.post("/study-plan")
def study_plan(request: StudyPlanRequest):

    return generate_study_plan(
        request.role,
        request.missing_skills
    )

@app.post("/interview-prep")
def interview_prep(request: InterviewPrepRequest):

    return generate_interview_prep(
        request.role,
        request.experience_level,
        request.skills
    )

@app.post("/study-plan-from-skills")
def study_plan_from_skills(
    request: StudyPlanFromSkillsRequest
):

    return generate_study_plan_from_skills(
        request.role,
        request.skills
    )

@app.get("/api-info")
def api_info():
    return {
        "name": "InterviewCoach",
        "version": "0.1.0",
        "status": "ready",
        "endpoint": "/interview-prep"
    }