from BD_conexionsql import Conexion

#INICIO DE SESION w
def iniciarSesion(correo, contrasena):
    conexion, cursor = Conexion.conectar()
    sql = "SELECT id_usuario FROM usuario WHERE correo_electronico = ? AND contrasena = ?"
    cursor.execute(sql, (correo, contrasena))
    usuario = cursor.fetchone()  # Obtiene el primer resultado

    if usuario:
        id_usuario = usuario[0]  # El ID está en la primera columna
        print("Inicio de sesión exitoso")
        return id_usuario
    else:
        print("Correo electrónico o contraseña incorrectos")
        return None
##QUEMAR ARCHIVOS 
""" nombre_categoria = "FAVORITOS"
crearTablaCategoria()
insertarCategoria((nombre_categoria,))
 """

""" nombreUser = "ewfwfe"
apellido = "regverg"
correo = "admin"
contrasena = "admin"
direccion = "admwefwfewin"
crearTablaUsuarios()
insertarUsuario((nombreUser,apellido,correo,contrasena,direccion)) """