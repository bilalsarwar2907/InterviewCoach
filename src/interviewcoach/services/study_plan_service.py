def generate_study_plan(role: str, missing_skills: list[str]):

    plan = []

    day = 1

    for skill in missing_skills:
        plan.append({
            "day": day,
            "focus": skill
        })
        day += 1

    return {
        "role": role,
        "plan": plan
    }