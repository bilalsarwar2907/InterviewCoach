"""
Unit tests for InterviewCoach services.
Run with: pytest tests/
"""
import sys
from pathlib import Path

# Make sure the src package is on the path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from interviewcoach.services.knowledge_service import (
    load_role_knowledge,
    extract_skills,
)
from interviewcoach.services.skill_gap_service import analyze_skill_gap
from interviewcoach.services.study_plan_service import (
    generate_study_plan,
    generate_study_plan_from_skills,
)
from interviewcoach.services.interview_service import generate_questions
from interviewcoach.services.interview_prep_service import generate_interview_prep


# ─────────────────────────────────────────────
# knowledge_service
# ─────────────────────────────────────────────

def test_load_ai_engineer_knowledge_returns_content():
    knowledge = load_role_knowledge("AI Engineer")
    assert len(knowledge) > 0, "AI Engineer knowledge should not be empty"


def test_load_unknown_role_returns_empty_string():
    knowledge = load_role_knowledge("Unknown Role XYZ")
    assert knowledge == "", "Unknown role should return empty string"


def test_extract_skills_returns_correct_list():
    knowledge = load_role_knowledge("AI Engineer")
    skills = extract_skills(knowledge)
    assert "Python" in skills
    assert "FastAPI" in skills
    assert len(skills) > 0


def test_extract_skills_handles_hash_heading():
    """extract_skills must work whether heading has # or not."""
    knowledge_with_hash = "# Core Skills\n- Python\n- Docker\n\nOther section"
    knowledge_without_hash = "Core Skills\n- Python\n- Docker\n\nOther section"
    assert extract_skills(knowledge_with_hash) == ["Python", "Docker"]
    assert extract_skills(knowledge_without_hash) == ["Python", "Docker"]


def test_extract_skills_empty_knowledge():
    assert extract_skills("") == []


# ─────────────────────────────────────────────
# skill_gap_service
# ─────────────────────────────────────────────

def test_skill_gap_matched_and_missing():
    result = analyze_skill_gap("AI Engineer", ["Python", "FastAPI"])
    assert "Python" in result["matched_skills"]
    assert "FastAPI" in result["matched_skills"]
    assert "Docker" in result["missing_skills"]


def test_skill_gap_no_skills_returns_all_missing():
    result = analyze_skill_gap("AI Engineer", [])
    assert len(result["matched_skills"]) == 0
    assert len(result["missing_skills"]) > 0


def test_skill_gap_all_skills_returns_no_missing():
    all_skills = extract_skills(load_role_knowledge("AI Engineer"))
    result = analyze_skill_gap("AI Engineer", all_skills)
    assert len(result["missing_skills"]) == 0
    assert len(result["matched_skills"]) == len(all_skills)


def test_skill_gap_case_insensitive():
    """Skills comparison should be case-insensitive."""
    result = analyze_skill_gap("AI Engineer", ["python", "fastapi"])
    assert "Python" in result["matched_skills"]
    assert "FastAPI" in result["matched_skills"]


# ─────────────────────────────────────────────
# study_plan_service
# ─────────────────────────────────────────────

def test_study_plan_max_7_days():
    """Plan must never exceed 7 days, even with many missing skills."""
    many_skills = [f"Skill{i}" for i in range(15)]
    result = generate_study_plan("Test Role", many_skills)
    assert len(result["plan"]) == 7


def test_study_plan_rich_format():
    """Each day must have day, focus, objective, and estimated_hours."""
    result = generate_study_plan("Test Role", ["Docker", "Git"])
    day = result["plan"][0]
    assert "day" in day
    assert "focus" in day
    assert "objective" in day
    assert "estimated_hours" in day


def test_study_plan_empty_missing_skills():
    result = generate_study_plan("AI Engineer", [])
    assert result["plan"] == []


def test_study_plan_days_are_sequential():
    result = generate_study_plan("Test Role", ["A", "B", "C"])
    days = [item["day"] for item in result["plan"]]
    assert days == [1, 2, 3]


def test_study_plan_from_skills_max_7_days():
    result = generate_study_plan_from_skills("AI Engineer", [])
    assert len(result["plan"]) <= 7


def test_study_plan_from_skills_has_matched_and_missing():
    result = generate_study_plan_from_skills("AI Engineer", ["Python"])
    assert "matched_skills" in result
    assert "missing_skills" in result
    assert "Python" in result["matched_skills"]


# ─────────────────────────────────────────────
# interview_service
# ─────────────────────────────────────────────

def test_questions_never_exceed_5():
    questions = generate_questions("AI Engineer", "Junior")
    assert len(questions) <= 5


def test_junior_and_senior_get_different_questions():
    junior = generate_questions("AI Engineer", "Junior")
    senior = generate_questions("AI Engineer", "Senior")
    assert junior != senior, "Junior and Senior should get different questions"


def test_unknown_role_returns_fallback_questions():
    questions = generate_questions("Unknown Role XYZ", "Junior")
    assert len(questions) > 0, "Should always return at least one question"


def test_experience_level_case_insensitive():
    """junior / JUNIOR / Junior should all produce same questions."""
    q1 = generate_questions("AI Engineer", "junior")
    q2 = generate_questions("AI Engineer", "JUNIOR")
    q3 = generate_questions("AI Engineer", "Junior")
    assert q1 == q2 == q3


# ─────────────────────────────────────────────
# interview_prep_service (integration)
# ─────────────────────────────────────────────

def test_full_prep_returns_all_sections():
    result = generate_interview_prep("AI Engineer", "Junior", ["Python"])
    assert "role" in result
    assert "questions" in result
    assert "skill_gap" in result
    assert "study_plan" in result


def test_full_prep_role_is_correct():
    result = generate_interview_prep("AI Engineer", "Junior", ["Python"])
    assert result["role"] == "AI Engineer"


def test_full_prep_study_plan_max_7_days():
    result = generate_interview_prep("AI Engineer", "Junior", [])
    assert len(result["study_plan"]["plan"]) <= 7
