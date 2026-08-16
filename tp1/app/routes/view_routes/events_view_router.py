from fastapi import Request
from routes.view_routes.base_view_router import BaseViewRouter
from repositories.events_repository import EventsRepository
from models.events.response_model import ResponseModel


class EventsViewRouter(BaseViewRouter):
    def __init__(self):
        super().__init__("/events", ["ViewEvents"])
        self._add_route("/", self.render_index, methods=["GET"])
        self._add_route("/{id}", self.render_detail, methods=["GET"])
        self.__events_repository = EventsRepository.build()

    def render_index(self, request: Request):
        events = self.__events_repository.get_all()
        events = list(map(lambda event: ResponseModel.from_dict(event), events))
        context = {
            "events": events,
            "events_count": len(events)
        }
        return self._render_template(request, "index.html", context=context)

    def render_detail(self, request: Request, id: int):
        event = self.__events_repository.get_by_id(id)
        context = { "event": event }
        return self._render_template(request, "show.html", context=context)