from interviewcoach.services.knowledge_service import load_role_knowledge, extract_questions


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

    # --- Role-specific questions (from the "## Interview Questions" list in the role's .md file) ---
    role_questions = extract_questions(knowledge)

    # Fallback if no knowledge file exists for this role
    if not role_questions:
        role_questions = [
            f"What is your experience with {role}?",
            f"What challenges have you solved as a {role}?",
        ]

    # --- Level-specific questions (from "Junior/Mid/Senior Questions" in the role's .md file) ---
    level_questions = extract_questions(knowledge, f"{level.capitalize()} Questions")

    # Fallback if the role file has no list for this level
    if not level_questions:
        level_questions = _LEVEL_QUESTIONS.get(level, _LEVEL_QUESTIONS[_DEFAULT_LEVEL])

    # Combine: up to 3 role questions + 2 level questions = 5 total
    combined = role_questions[:3] + level_questions

    return combined[:5]