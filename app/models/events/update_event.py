from pydantic import BaseModel
from datetime import date


class UpdateEvent(BaseModel):
    name: str
    host: str
    date: date
    size: int