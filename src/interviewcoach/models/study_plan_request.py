from pydantic import BaseModel


class StudyPlanRequest(BaseModel):
    role: str
    missing_skills: list[str]