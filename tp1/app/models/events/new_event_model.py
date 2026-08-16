from pydantic import BaseModel

class NewEvent(BaseModel):
    name: str
    host: str
    size: int