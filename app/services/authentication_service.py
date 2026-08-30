from repositories.users_repository import UsersRepository
from passlib.context import CryptContext
from services.token_service import TokenService
from errors.invalid_credential_error import InvalidCredentialError


class AuthenticationService():
    @classmethod
    def build(cls):
        encryption = CryptContext(schemes=["bcrypt"], deprecated="auto", bcrypt__rounds=12)
        return cls(
            UsersRepository.build(),
            TokenService.build(),
            encryption
        )

    def __init__(self, users_repository, token_service, encryption):
        self.__users_repository = users_repository
        self.__token_service = token_service
        self.__encryption = encryption

    def authenticate(self, username, password):
        user = self.__get_user(username)
        self.__check_password(user, password)

        return self.__generate_token(user)

    def __get_user(self, username):
        user = self.__users_repository.get_by_username(username)

        if not user: self.__raise_invalid_credential_error()

        return user

    def __check_password(self, user, password):
        if self.__encryption.verify(password, user.hashed_password):
            return True

        self.__raise_invalid_credential_error()

    def __generate_token(self, user):
        return self.__token_service.create_access_token(user)

    def __raise_invalid_credential_error(self):
        raise InvalidCredentialError()