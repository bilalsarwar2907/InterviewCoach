from pathlib import Path


def load_role_knowledge(role: str) -> str:

    role_map = {
        "Ai Engineer": "ai-engineer",
        "AI Engineer": "ai-engineer",
        "Cloud Engineer": "cloud-engineer",
        "Data Engineer": "data-engineer",
        "Python Developer": "python",
    }

    folder = role_map.get(role)

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