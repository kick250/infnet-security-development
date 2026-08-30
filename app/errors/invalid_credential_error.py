class InvalidCredentialError(RuntimeError):
    def __init__(self, message="Usuario ou senha invalidos."):
        super().__init__(message)