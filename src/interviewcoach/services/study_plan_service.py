from interviewcoach.services.skill_gap_service import analyze_skill_gap

MAX_PLAN_DAYS = 7


def generate_study_plan(role: str, missing_skills: list[str]):
    """
    Builds a study plan from a list of missing skills.
    Capped at 7 days. Returns consistent rich format.
    """
    plan = []

    for day, skill in enumerate(missing_skills[:MAX_PLAN_DAYS], start=1):
        plan.append(
            {
                "day": day,
                "focus": skill,
                "objective": f"Study and practice {skill}",
                "estimated_hours": 2
            }
        )

    return {
        "role": role,
        "plan": plan
    }


def generate_study_plan_from_skills(
    role: str,
    skills: list[str]
):
    """
    Builds a study plan from the user's skill list by first
    running a skill gap analysis, then planning for missing skills.
    Capped at 7 days.
    """
    gap = analyze_skill_gap(role, skills)

    plan = []

    for day, skill in enumerate(gap["missing_skills"][:MAX_PLAN_DAYS], start=1):
        plan.append(
            {
                "day": day,
                "focus": skill,
                "objective": f"Study and practice {skill}",
                "estimated_hours": 2
            }
        )

    return {
        "role": role,
        "matched_skills": gap["matched_skills"],
        "missing_skills": gap["missing_skills"],
        "plan": plan
    }