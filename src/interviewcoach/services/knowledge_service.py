from pathlib import Path

# Absolute path to the knowledge/ folder, anchored to this file's location.
# Works regardless of which directory uvicorn is started from.
_KNOWLEDGE_ROOT = Path(__file__).resolve().parents[3] / "knowledge"


def get_role_folder(role: str) -> str:
    return (
        role.lower()
        .replace("_", "-")
        .replace(" ", "-")
    )


def load_role_knowledge(role: str) -> str:

    folder = get_role_folder(role)
    if not folder:
        return ""

    knowledge_path = _KNOWLEDGE_ROOT / folder

    content = []

    if not knowledge_path.exists():
        return ""

    for file in knowledge_path.glob("*.md"):
        try:
            content.append(file.read_text(encoding="utf-8"))
        except Exception as ex:
            content.append(f"ERROR: {file.name} - {str(ex)}")

    return "\n\n".join(content)


def extract_skills(knowledge: str) -> list:
    skills = []

    in_core_skills = False

    for line in knowledge.splitlines():

        line = line.strip()

        # Match "Core Skills" with or without any number of leading # characters
        if line.lstrip("#").strip() == "Core Skills":
            in_core_skills = True
            continue

        if (
            in_core_skills
            and line
            and not line.startswith("- ")
        ):
            break

        if in_core_skills and line.startswith("- "):
            skills.append(line[2:].strip())

    return skills