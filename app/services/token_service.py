from datetime import datetime, timedelta
from jose import jwt, JWTError
from entities.user import User
from config import SECRET_KEY, ACCESS_TOKEN_EXPIRE_MINUTES, ALGORITHM
from errors.invalid_access_token_error import InvalidAccessTokenError

class TokenService():
    __EXPIRATION_KEY = "expiration_timestamp"

    @classmethod
    def build(cls):
        return cls()

    def create_access_token(self, user: User):
        expiration_datetime = datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        encode_data = {
            "sub": str(user.id),
            self.__EXPIRATION_KEY: int(expiration_datetime.timestamp())
        }
        return jwt.encode(encode_data, SECRET_KEY, algorithm=ALGORITHM)

    def decode(self, token: str):
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

            self.__validate(payload)

            return payload
        except JWTError as error:
            raise InvalidAccessTokenError()

    def __validate(self, payload):
        expiration_datetime = datetime.fromtimestamp(payload[self.__EXPIRATION_KEY])
        if datetime.now() > expiration_datetime:
            raise InvalidAccessTokenError()
