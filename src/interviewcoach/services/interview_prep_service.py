from interviewcoach.services.interview_service import generate_questions
from interviewcoach.services.skill_gap_service import analyze_skill_gap
from interviewcoach.services.study_plan_service import generate_study_plan


def generate_interview_prep(
    role: str,
    experience_level: str,
    skills: list[str]
):
    skill_gap = analyze_skill_gap(role, skills)

    study_plan = generate_study_plan(
        role,
        skill_gap["missing_skills"]
    )

    return {
        "role": role,
        "questions": generate_questions(
            role,
            experience_level
        ),
        "skill_gap": skill_gap,
        "study_plan": study_plan
    }