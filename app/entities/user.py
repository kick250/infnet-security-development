class User:
    STANDARD_ACCESS_TYPE = "standard"
    RESOURCES_ACCESS_TYPE = "by_resources"
    FULL_RESOURCES = { "all": True }

    def __init__(self, id, username, hashed_password, access_type=STANDARD_ACCESS_TYPE, allowed_resources=FULL_RESOURCES):
        self.__id = id
        self.__username = username
        self.__hashed_password = hashed_password
        self.__access_type = access_type
        self.__allowed_resources = allowed_resources

    @property
    def id(self):
        return self.__id

    @property
    def username(self):
        return self.__username

    @property
    def hashed_password(self):
        return self.__hashed_password

    @property
    def access_type(self):
        return self.__access_type

    @property
    def allowed_resources(self):
        return self.__allowed_resources

