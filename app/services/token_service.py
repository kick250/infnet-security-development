from datetime import datetime, timedelta
from jose import jwt, JWTError
from entities.user import User
from config import SECRET_KEY, ACCESS_TOKEN_EXPIRE_MINUTES, ALGORITHM
from errors.invalid_access_token_error import InvalidAccessTokenError

class TokenService():
    __DECODE_CONFIG = {
        "verify_exp": True,
        "require_exp": True
    }

    @classmethod
    def build(cls):
        return cls()

    def create_access_token(self, user: User):
        now = datetime.now()
        expiration_datetime = now + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        encode_data = {
            "sub": str(user.id),
            "exp": int(expiration_datetime.timestamp()),
            "access_type": user.access_type,
            "allowed_resources": user.allowed_resources,
            "created_at": now.timestamp()
        }
        return jwt.encode(encode_data, SECRET_KEY, algorithm=ALGORITHM)

    def decode(self, token: str):
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM], options=self.__DECODE_CONFIG)

            return payload
        except JWTError:
            raise InvalidAccessTokenError()
