import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from interviewcoach.services.knowledge_service import (
    load_role_knowledge,
    extract_skills,
)

KNOWLEDGE = ROOT / "knowledge"


def test_every_active_role_has_core_skills():
    for folder in KNOWLEDGE.iterdir():
        if not folder.is_dir():
            continue

        md_files = list(folder.glob("*.md"))
        if not md_files:          # skip empty folders
            continue

        text = load_role_knowledge( folder.name)
        skills = extract_skills(text)

        assert skills, f"{folder.name} has no Core Skills"