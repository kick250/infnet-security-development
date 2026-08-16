from pydantic import BaseModel

class ResponseModel(BaseModel):
    id: int
    name: str
    host: str
    size: int

    @classmethod
    def from_dict(cls, event_dict):
        return cls(
            id= event_dict['id'],
            name= event_dict['name'],
            host= event_dict['host'],
            size= event_dict['size']
        )