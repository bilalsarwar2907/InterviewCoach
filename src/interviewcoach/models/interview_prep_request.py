from pydantic import BaseModel


class InterviewPrepRequest(BaseModel):
    role: str
    experience_level: str
    skills: list[str]