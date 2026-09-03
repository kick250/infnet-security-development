from pydantic import BaseModel
from datetime import date

class NewEvent(BaseModel):
    name: str
    host: str
    date: date
    size: int