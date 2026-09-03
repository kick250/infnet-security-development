class EventNotFoundError(RuntimeError):
    def __init__(self, message="Evento não encontrado."):
        super().__init__(message)