class TelefonoExistenteException(Exception):
    def __init__(self, message="Ya tiene un contacto con este Numero"):
        self.message = message
        super().__init__(self.message)