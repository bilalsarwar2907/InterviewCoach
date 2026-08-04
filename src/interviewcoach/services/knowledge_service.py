from pathlib import Path


def load_role_knowledge(role: str) -> str:
    role_map = {
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

    if knowledge_path.exists():
        for file in knowledge_path.glob("*.*"):
            try:
                content.append(file.read_text(encoding="utf-8"))
            except Exception:
                pass

    return "\n".join(content)