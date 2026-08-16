from pydantic import BaseModel

class NewEvent(BaseModel):
    name: str
    size: int