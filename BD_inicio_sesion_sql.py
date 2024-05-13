from conexionsql import Conexion

#INICIO DE SESION 
""" # public int selectLogin(String email, String password) {
        int resultado = 0;
        // We prepare the consultation SQL for select data
        String selectSQL = "SELECT * FROM users Where email=? AND password_user=?";
        try (PreparedStatement pstmt = connection.prepareStatement(selectSQL)) {
            pstmt.setString(2, password);
            pstmt.setString(1, email);
"""
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