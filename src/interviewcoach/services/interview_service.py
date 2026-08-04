from interviewcoach.services.knowledge_service import load_role_knowledge


def generate_questions(role: str, experience_level: str):

    knowledge = load_role_knowledge(role)

    if knowledge:
        return [
            f"Based on the {role} guide, what are the most important skills for this role?",
            f"What project experience demonstrates capability as a {role}?",
            f"What gaps would prevent success in a {experience_level} {role} position?"
        ]

    return [
        f"What is your experience with {role}?",
        f"What challenges have you solved as a {role}?",
        f"What would you expect from a {experience_level} {role} position?"
    ]