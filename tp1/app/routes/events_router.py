from routes.base_router import BaseRouter
from typing import Annotated
from fastapi import Body

class EventsRouter(BaseRouter):
    def __init__(self):
        super().__init__("/events", ["Events"])
        self._add_api_route("/", self.get_all_handler, methods=["GET"])
        self._add_api_route("/{id}", self.get_by_id_handler, methods=["GET"])
        self._add_api_route("/", self.create_handler, methods=["post"])

        self.__events = {}

    def get_all_handler(self):
        return { "result": self.__events }

    def get_by_id_handler(self, id: int):
        event = self.__events.get(int(id))

        if not event:
            self._render_http_exception(404, "This event couldn't be found.")

        return { "result": event }

    def create_handler(self, event: Annotated[dict, Body(embed=True)]):
        new_event = {
            "id": self.__generate_id(),
            "name": event.get("name"),
            "size": event.get("size")
        }

        self.__events[new_event["id"]] = new_event

        return { "result": new_event }


    def __generate_id(self):
        return len(self.__events.keys()) + 1