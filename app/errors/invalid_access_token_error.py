class InvalidAccessTokenError(RuntimeError):
    def __init__(self, message="Token de Acesso inválido"):
        super().__init__(message)