from auth import AuthService
from entities.user import User
from routes.base_router import BaseRouter
from typing import Annotated
from fastapi import Body, Depends
from models.events.new_event_model import NewEvent
from repositories.events_repository import EventsRepository

class EventsAlternativeRouter(BaseRouter):
    def __init__(self):
        super().__init__("/events_alternative", ["EventsAlternative"])
        self._add_api_route("/", self.create_handler, methods=["POST"])

        self.__events_repository = EventsRepository.build()

    def create_handler(
            self,
            event: Annotated[NewEvent, Body(embed=True)],
            user: Annotated[User, Depends(AuthService.get_active_user)]
        ):
        created_event = self.__events_repository.save(
            event.name,
            event.host,
            event.date,
            event.size,
            user.id
        )

        return created_event