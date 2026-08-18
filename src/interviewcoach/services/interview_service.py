from interviewcoach.services.knowledge_service import load_role_knowledge

# Level-specific questions added to every role.
# 3 role-specific questions (from knowledge) + 2 level questions = 5 total.
_LEVEL_QUESTIONS = {
    "junior": [
        "Can you explain what version control is and how you use Git in your daily work?",
        "How do you approach debugging when something is not working as expected?",
    ],
    "mid": [
        "Describe a technical problem you solved independently and walk us through your process.",
        "How do you decide between two different technical approaches when both could work?",
    ],
    "senior": [
        "How would you design a scalable architecture for this role's core responsibilities?",
        "How do you balance technical debt against delivering new features in a team setting?",
    ],
}

_DEFAULT_LEVEL = "junior"


def _normalise_level(experience_level: str) -> str:
    """Map any experience_level string to junior / mid / senior."""
    level = experience_level.lower().strip()
    if level in ("mid", "mid-level", "middle", "intermediate"):
        return "mid"
    if level in ("senior", "lead", "principal", "staff"):
        return "senior"
    return "junior"


def generate_questions(role: str, experience_level: str):

    knowledge = load_role_knowledge(role)
    level = _normalise_level(experience_level)

    # --- Role-specific questions (from knowledge keywords) ---
    role_questions = []

    if "Azure AI Search" in knowledge:
        role_questions.append(
            "Explain the difference between keyword, vector, and hybrid search."
        )

    if "Copilot Studio" in knowledge:
        role_questions.append(
            "How would you ground a Copilot Studio agent using SharePoint?"
        )

    if "Semantic Kernel" in knowledge:
        role_questions.append(
            "What problem does Semantic Kernel solve in AI applications?"
        )

    if "MCP" in knowledge:
        role_questions.append(
            "What is MCP and when would you use it?"
        )

    if "RAG" in knowledge:
        role_questions.append(
            "Describe a Retrieval-Augmented Generation architecture."
        )

    # Fallback if no knowledge file exists for this role
    if not role_questions:
        role_questions = [
            f"What is your experience with {role}?",
            f"What challenges have you solved as a {role}?",
        ]

    # --- Level-specific questions ---
    level_questions = _LEVEL_QUESTIONS.get(level, _LEVEL_QUESTIONS[_DEFAULT_LEVEL])

    # Combine: up to 3 role questions + 2 level questions = 5 total
    combined = role_questions[:3] + level_questions

    return combined[:5]