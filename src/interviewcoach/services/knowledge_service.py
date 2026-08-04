from pathlib import Path

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

    knowledge_path = Path("knowledge") / folder

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

        if line == "Core Skills":
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