from interviewcoach.services.knowledge_service import load_role_knowledge


def analyze_skill_gap(role: str, skills: list[str]):

    knowledge = load_role_knowledge(role)

    matched = []
    missing = []

    expected_skills = [
        "Python",
        "FastAPI",
        "Docker",
        "Git",
        "Azure AI Search",
        "Copilot Studio",
        "Semantic Kernel",
        "Azure AI Foundry"
    ]

    for skill in expected_skills:

        if skill.lower() in [s.lower() for s in skills]:
            matched.append(skill)
        else:
            if skill in knowledge:
                missing.append(skill)

    return {
        "role": role,
        "matched_skills": matched,
        "missing_skills": missing
    }