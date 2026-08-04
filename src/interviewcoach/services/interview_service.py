from interviewcoach.services.knowledge_service import load_role_knowledge


def generate_questions(role: str, experience_level: str):

    knowledge = load_role_knowledge(role)

    questions = []

    if "Azure AI Search" in knowledge:
        questions.append(
            "Explain the difference between keyword, vector, and hybrid search."
        )

    if "Copilot Studio" in knowledge:
        questions.append(
            "How would you ground a Copilot Studio agent using SharePoint?"
        )

    if "Semantic Kernel" in knowledge:
        questions.append(
            "What problem does Semantic Kernel solve in AI applications?"
        )

    if "MCP" in knowledge:
        questions.append(
            "What is MCP and when would you use it?"
        )

    if "RAG" in knowledge:
        questions.append(
            "Describe a Retrieval-Augmented Generation architecture."
        )

    if not questions:
        questions = [
            f"What is your experience with {role}?",
            f"What challenges have you solved as a {role}?",
            f"What would you expect from a {experience_level} {role} position?"
        ]

    return questions[:5]