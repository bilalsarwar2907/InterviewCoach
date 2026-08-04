from interviewcoach.services.skill_gap_service import analyze_skill_gap


def generate_study_plan(role: str, missing_skills: list[str]):

    plan = []

    day = 1

    for skill in missing_skills:
        plan.append(
            {
                "day": day,
                "focus": skill
            }
        )
        day += 1

    return {
        "role": role,
        "plan": plan
    }


def generate_study_plan_from_skills(
    role: str,
    skills: list[str]
):

    gap = analyze_skill_gap(role, skills)

    plan = []

    day = 1

    for skill in gap["missing_skills"]:
        plan.append(
            {
                "day": day,
                "focus": skill,
                "objective": f"Study and practice {skill}",
                "estimated_hours": 2
            }
        )
        day += 1

    return {
        "role": role,
        "matched_skills": gap["matched_skills"],
        "missing_skills": gap["missing_skills"],
        "plan": plan
    }