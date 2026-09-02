from fastapi.security import OAuth2PasswordBearer
from services.token_service import TokenService
from errors.invalid_access_token_error import InvalidAccessTokenError
from fastapi import Depends, HTTPException, Request, status
from typing import Annotated
from repositories.users_repository import UsersRepository
from entities.user import User

@staticmethod
def oauth2_scheme():
    return OAuth2PasswordBearer(tokenUrl="/login")

class AuthService:
    @staticmethod
    def get_active_user(token: Annotated[str, Depends(oauth2_scheme())], request: Request) -> User:
        try:
            users_repository = UsersRepository.build()
            token_service = TokenService.build()

            token_data = token_service.decode(token)

            if not AuthService.__is_allowed(token_data["access_type"], token_data["allowed_resources"], request):
                AuthService.__reject_request()


            active_user = users_repository.get_by_sub(token_data["sub"])

            if active_user == None: AuthService.__reject_request()

            return active_user
        except InvalidAccessTokenError:
            AuthService.__reject_request()

    # resource: str(ex: "users", "events", "comments")
    # action: str(ex: "read", "write", "delete")
    @staticmethod
    def __is_allowed(access_type, allowed_resources, request):
        if (access_type != User.RESOURCES_ACCESS_TYPE) \
            or allowed_resources.get("all"):
            return True
        resource = AuthService.__resource_from_path(request.url.path)
        action = AuthService.__action_by_method(request.method)

        return allowed_resources.get(resource, {}).get(action, False)

    @staticmethod
    def __resource_from_path(path):
        path_parts = path.strip("/").split("/")
        if len(path_parts) > 0:
            return path_parts[0]
        return None

    @staticmethod
    def __action_by_method(method):
        if method.upper() == "GET":
            return "read"
        elif method.upper() == "POST":
            return "write"
        elif method.upper() == "PUT":
            return "write"
        elif method.upper() == "PATCH":
            return "write"
        elif method.upper() == "DELETE":
            return "delete"
        else:
            return None

    @staticmethod
    def __reject_request():
        raise HTTPException(status.HTTP_403_FORBIDDEN, "Token de Acesso inválido")