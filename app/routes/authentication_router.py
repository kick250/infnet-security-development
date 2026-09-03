from routes.base_router import BaseRouter
from fastapi import Depends, HTTPException, status
from typing import Annotated
from fastapi.security import OAuth2PasswordRequestForm
from services.authentication_service import AuthenticationService
from errors.invalid_credential_error import InvalidCredentialError
from models.authentication.token_model import TokenModel


class AuthenticationRouter(BaseRouter):
    def __init__(self):
        super().__init__("/login", ["Login"])

        self._add_api_route("/", self.login_handler, methods=["post"], authenticated=False)

    def login_handler(self, form_data: Annotated[OAuth2PasswordRequestForm, Depends()]) -> TokenModel:
        try:
            service = AuthenticationService.build()
            access_token = service.authenticate(form_data.username, form_data.password)
            return { "access_token": access_token }
        except InvalidCredentialError as error:
            raise HTTPException(status.HTTP_401_UNAUTHORIZED, str(error))
