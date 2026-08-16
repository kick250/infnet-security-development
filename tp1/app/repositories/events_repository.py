import uuid


class EventsRepository:
    __events_records = {}

    @classmethod
    def build(cls):
        repository = cls()
        repository.save(
            "Evento doogle",
            "doogle",
            "2026-12-01",
            10,
            id=1
        )
        return repository

    def get_all(self):
        return tuple(self.__events_records.values())

    def get_by_id(self, id):
        return self.__events_records.get(id)

    def save(self, name, host, date, size, id=None):
        if not id:
            id = self.__generate_id()

        event = {
            "id": id,
            "name": name,
            "host": host,
            "date": date,
            "size": size,
            "audit_token": self.__generate_audit_token()
        }
        self.__events_records[event["id"]] = event
        return event

    def __generate_id(self):
        return len(self.__events_records.keys()) + 1

    def __generate_audit_token(self):
        return str(uuid.uuid4())