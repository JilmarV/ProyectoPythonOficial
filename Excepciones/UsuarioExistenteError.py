class UsuarioExistenteError(Exception):
    def __init__(self, message="El correo ya está registrado"):
        self.message = message
        super().__init__(self.message)