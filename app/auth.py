from fastapi.security import OAuth2PasswordBearer
from services.token_service import TokenService
from errors.invalid_access_token_error import InvalidAccessTokenError
from fastapi import Depends, HTTPException, status
from typing import Annotated
from repositories.users_repository import UsersRepository
from entities.user import User


def oauth2_scheme():
    return OAuth2PasswordBearer(tokenUrl="token")

def get_active_user(token: Annotated[str, Depends(oauth2_scheme())]) -> User:
    def reject_request():
        raise HTTPException(status.HTTP_403_FORBIDDEN, "Token de Acesso inválido")

    try:
        users_repository = UsersRepository.build()
        token_service = TokenService.build()

        token_data = token_service.decode(token)
        active_user = users_repository.get_by_sub(token_data["sub"])

        if active_user == None: reject_request()

        return active_user
    except InvalidAccessTokenError:
        reject_request()