class User:
    def __init__(self, id, username, hashed_password):
        self.__id = id
        self.__username = username
        self.__hashed_password = hashed_password

    @property
    def id(self):
        return self.__id

    @property
    def username(self):
        return self.__username

    @property
    def hashed_password(self):
        return self.__hashed_password
