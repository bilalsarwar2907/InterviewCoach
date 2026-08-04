from pydantic import BaseModel


class SkillGapRequest(BaseModel):
    role: str
    skills: list[str]