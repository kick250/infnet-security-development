from routes.base_router import BaseRouter
from typing import Annotated, List
from fastapi import Body
from models.events.new_event_model import NewEvent
from models.events.response_model import ResponseModel
from repositories.events_repository import EventsRepository

class EventsRouter(BaseRouter):
    def __init__(self):
        super().__init__("/events", ["Events"])
        self._add_api_route("/", self.get_all_handler, methods=["GET"])
        self._add_api_route("/{id}", self.get_by_id_handler, methods=["GET"])
        self._add_api_route("/", self.create_handler, methods=["post"])

        self.__events_repository = EventsRepository.build()

    def get_all_handler(self) -> List[ResponseModel]:
        events = self.__events_repository.get_all()
        return events

    def get_by_id_handler(self, id: int) -> ResponseModel:
        event = self.__events_repository.get_by_id(int(id))

        if not event:
            self._render_http_exception(404, "This event couldn't be found.")

        return { "result": event }

    def create_handler(self, event: Annotated[NewEvent, Body(embed=True)]) -> ResponseModel:
        created_event = self.__events_repository.save(
            event.name,
            event.host,
            event.date,
            event.size
        )

        return created_event