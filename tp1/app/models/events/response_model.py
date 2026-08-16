from pydantic import BaseModel

class ResponseModel(BaseModel):
    id: int
    name: str
    size: int