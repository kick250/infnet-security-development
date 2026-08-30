from entities.user import User


class UsersRepository:
    __users_records = [
        [
            1010,
            "breno.nova@al.infnet.edu.br",
            "$2b$12$lcLRKh8qb95WtfVOMtfAPeilWCb8QrfUaQXmrGKyDge1YbvB9hTWm"
        ],
        [
            1212,
            "infnet@events.infnet.edu.br",
            "$2b$12$lcLRKh8qb95WtfVOMtfAPeilWCb8QrfUaQXmrGKyDge1YbvB9hTWm"
        ]
    ]

    @classmethod
    def build(cls):
        repository = cls()
        return repository

    def get_by_sub(self, sub):
        for user in self.__users_records:
            if user[0] == int(sub): return User(*user)

        return None

    def get_by_username(self, username):
        for user in self.__users_records:
            if user[1] == str(username).strip().lower(): return User(*user)

        return None
