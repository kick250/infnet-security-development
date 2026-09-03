from routes.base_router import BaseRouter
from typing import Annotated, List, Required
from fastapi import Body, Depends
from models.events.new_event_model import NewEvent
from models.events.response_model import ResponseModel
from repositories.events_repository import EventsRepository
from models.events.update_event import UpdateEvent
from fastapi import HTTPException, status
from entities.user import User
from auth import get_active_user


class EventsRouter(BaseRouter):
    def __init__(self):
        super().__init__("/events", ["Events"])
        self._add_api_route("/", self.get_all_handler, methods=["GET"])
        self._add_api_route("/{id}", self.get_by_id_handler, methods=["GET"])
        self._add_api_route("/", self.create_handler, methods=["POST"])
        self._add_api_route("/{id}", self.update_handler, methods=["PUT"])

        self.__events_repository = EventsRepository.build()

    def get_all_handler(self) -> List[ResponseModel]:
        events = self.__events_repository.get_all()
        return events

    def get_by_id_handler(self, id: int) -> ResponseModel:
        event = self.__events_repository.get_by_id(int(id))

        if not event:
            self._render_http_exception(404, "This event couldn't be found.")

        return event

    def create_handler(
            self,
            event: Annotated[NewEvent, Body(embed=True)],
            user: Annotated[User, Depends(get_active_user)]
        ) -> ResponseModel:
        created_event = self.__events_repository.save(
            event.name,
            event.host,
            event.date,
            event.size,
            user.id
        )

        return created_event

    def update_handler(
            self,
            id: Annotated[int, Required],
            event: Annotated[UpdateEvent, Body(embed=True)],
            user: Annotated[User, Depends(get_active_user)]
        ) -> ResponseModel:
        self.__check_ownership(id, user.id)

        updated_event = self.__events_repository.save(
            event.name,
            event.host,
            event.date,
            event.size,
            user.id,
            id=id
        )

        return updated_event

    def __check_ownership(self, id: int, owner_id: int):
        if not self.__events_repository.exists_by_id_and_owner_id(id, owner_id):
            raise HTTPException(status.HTTP_404_NOT_FOUND, "Evento não encontrado nos seus eventos.")

        return True