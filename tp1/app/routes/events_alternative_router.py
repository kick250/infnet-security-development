from routes.base_router import BaseRouter
from typing import Annotated
from fastapi import Body
import uuid
from models.events.new_event_model import NewEvent

class EventsAlternativeRouter(BaseRouter):
    def __init__(self):
        super().__init__("/events_alternative", ["EventsAlternative"])
        self._add_api_route("/", self.create_handler, methods=["post"])

        self.__events = {}

    def create_handler(self, event: Annotated[NewEvent, Body(embed=True)]):
        created_event = self.__create_event(event)

        return created_event

    def __create_event(self, new_event):
        event = {
            "id": self.__generate_id(),
            "name": new_event.name,
            "size": new_event.size,
            "audit_token": self.__generate_audit_token()
        }
        self.__events[event["id"]] = event
        return event

    def __generate_id(self):
        return len(self.__events.keys()) + 1

    def __generate_audit_token(self):
        return str(uuid.uuid4())