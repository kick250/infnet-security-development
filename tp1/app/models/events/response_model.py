from pydantic import BaseModel
from datetime import date

class ResponseModel(BaseModel):
    id: int
    name: str
    host: str
    date: date
    size: int

    @classmethod
    def from_dict(cls, event_dict):
        return cls(
            id= event_dict['id'],
            name= event_dict['name'],
            host= event_dict['host'],
            date= event_dict['date'],
            size= event_dict['size']
        )

    def formatted_date(self):
        return self.date.strftime("%d/%m/%Y")

    def event_detail_path(self):
        return f"/view/events/{self.id}"