class CorreoExistenteException(Exception):
    def __init__(self, message="Ya tiene un contacto con este correo"):
        self.message = message
        super().__init__(self.message)