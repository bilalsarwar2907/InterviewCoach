from pydantic import BaseModel


class StudyPlanFromSkillsRequest(BaseModel):
    role: str
    skills: list[str]