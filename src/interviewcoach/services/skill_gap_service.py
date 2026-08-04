from interviewcoach.services.knowledge_service import (
    load_role_knowledge,
    extract_skills
)


def analyze_skill_gap(role: str, skills: list[str]):

    knowledge = load_role_knowledge(role)

    expected_skills = extract_skills(knowledge)

    matched = []
    missing = []

    for skill in expected_skills:

        if skill.lower() in [s.lower() for s in skills]:
            matched.append(skill)
        else:
            missing.append(skill)

    return {
        "role": role,
        "matched_skills": matched,
        "missing_skills": missing
    }