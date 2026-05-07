from pydantic import BaseModel

class ResumeResponse(BaseModel):
    filename: str
    match_result: dict