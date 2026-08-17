from routes.base_router import BaseRouter
from typing import Annotated
from fastapi import Body
from models.events.new_event_model import NewEvent
from repositories.events_repository import EventsRepository

class EventsAlternativeRouter(BaseRouter):
    def __init__(self):
        super().__init__("/events_alternative", ["EventsAlternative"])
        self._add_api_route("/", self.create_handler, methods=["post"])

        self.__events_repository = EventsRepository.build()

    def create_handler(self, event: Annotated[NewEvent, Body(embed=True)]):
        created_event = self.__events_repository.save(
            event.name,
            event.host,
            event.date,
            event.size
        )

        return created_event