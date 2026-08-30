import uuid
from errors.event_not_found_error import EventNotFoundError


class EventsRepository:
    __events_records = {}

    @classmethod
    def build(cls):
        return cls()

    def get_all(self):
        return tuple(self.__events_records.values())

    def get_by_id(self, id):
        return self.__events_records.get(id)

    def exists_by_id_and_owner_id(self, id, owner_id):
        event = self.get_by_id(id)

        return event != None and event["owner_id"] == owner_id

    def save(self, name, host, date, size, owner_id, id=None):
        if id != None and not self.exists_by_id_and_owner_id(id, owner_id):
            raise EventNotFoundError()

        if not id: id = self.__generate_id()

        event = {
            "id": id,
            "name": name,
            "host": host,
            "date": date,
            "size": size,
            "owner_id": owner_id,
            "audit_token": self.__generate_audit_token()
        }
        self.__events_records[event["id"]] = event
        return event

    def __generate_id(self):
        return len(self.__events_records.keys()) + 1

    def __generate_audit_token(self):
        return str(uuid.uuid4())