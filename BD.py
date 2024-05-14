import sqlite3

def conectar():
    conexion = sqlite3.connect("agendaBD.sqlite3")
    cursor = conexion.cursor()
    return conexion, cursor
#-------------------------------------------------------------------------------------------------------------------------------------
def crearTablaContactos():
    conexion, cursor = conectar()
    sql = """    
        CREATE TABLE IF NOT EXISTS contacto(
            id_contacto INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            id_usuario int NOT NULL,
            nombre_contacto VARCHAR(60) NOT NULL,
            apellido_contacto VARCHAR(60) NOT NULL,
            email VARCHAR(20) NOT NULL,
            CONSTRAINT id_de_usuario FOREIGN KEY (id_usuario) REFERENCES usuario(id_usuario)
        )
    """
    if cursor.execute(sql):
        print("Tabla De Contacto Creada")
    else:
        print("No se pudo crear la tabla ")
    conexion.close()

def crearTablaUsuarios():
    conexion, cursor = conectar()
    sql = """    
        CREATE TABLE IF NOT EXISTS usuario(
            id_usuario INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            nombre_usuario NOT NULL,
            apellido_usuario VARCHAR(60) NOT NULL,
            correo_electronico VARCHAR(20) UNIQUE NOT NULL,
            contrasena VARCHAR(20) NOT NULL,
            direccion VARCHAR(20) NOT NULL
        )
    """
    if cursor.execute(sql):
        print("Tabla De Usuario  Creada")
    else:
        print("No se pudo crear la tabla ")
    conexion.close()

def crearTablaCategoriaPorContacto():
    conexion, cursor = conectar()
    sql = """    
        CREATE TABLE IF NOT EXISTS categorias_por_contacto(
            id_categoria int NOT NULL,
            id_contacto int NOT NULL,
            CONSTRAINT id_de_categoria FOREIGN KEY (id_categoria) REFERENCES categoria(id_categoria),
            CONSTRAINT id_de_contacto FOREIGN KEY (id_contacto) REFERENCES contacto(id_contacto)
        
        )
    """
    if cursor.execute(sql):
        print("Tabla De Usuario  Creada")
    else:
        print("No se pudo crear la tabla ")
    conexion.close()


def crearTablaCategoria():
    conexion, cursor = conectar()
    sql = """    
        CREATE TABLE IF NOT EXISTS categoria(
            id_categoria INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            nombre_categoria VARCHAR(20) NOT NULL
        )
    """
    if cursor.execute(sql):
        print("Tabla De Usuario  Creada")
    else:
        print("No se pudo crear la tabla ")
    conexion.close()
def crearTablaCategoria():
    conexion, cursor = conectar()
    sql = """    
        CREATE TABLE IF NOT EXISTS categoria(
            id_categoria INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            nombre_categoria VARCHAR(20) NOT NULL
        )
    """
    if cursor.execute(sql):
        print("Tabla De Usuario  Creada")
    else:
        print("No se pudo crear la tabla ")
    conexion.close()

def crearTablaCategoriaPorContacto():
    conexion, cursor = conectar()
    sql = """    
        CREATE TABLE IF NOT EXISTS categorias_por_contacto(
            id_categoria int NOT NULL,
            id_contacto int NOT NULL,
            CONSTRAINT id_de_categoria FOREIGN KEY (id_categoria) REFERENCES categoria(id_categoria),
            CONSTRAINT id_de_contacto FOREIGN KEY (id_contacto) REFERENCES contacto(id_contacto)
        )
    """
    if cursor.execute(sql):
        print("Tabla De Categorias_por_contacto Creada")
    else:
        print("No se pudo crear la tabla de categorias_por_contacto")
    conexion.close()

##--------------------------------------------------------------------------------------------------------------------
# CRUD DEL CONTACTO
def insertarContacto(datos):
    conexion, cursor = conectar()
    sql = """
    INSERT INTO Contactos(nombre,apellido,telefono,email) VALUES(?,?,?,?)
    """
    if cursor.execute(sql, datos):
        print("Datos guardados")
    else:
        print("No se pudieron guardar los datos ")
    conexion.commit()
    conexion.close()

def consultarContacto():
    conexion, cursor = conectar()
    sql = "SELECT id,nombre,apellido,telefono,email FROM Contactos"
    cursor.execute(sql)
    listado = []
    for fila in cursor:
        listado.append(fila)    
    conexion.close()
    return listado

def modificarContacto(id, nombre, apellido, telefono, email):
    conexion, cursor = conectar()
    sql = """UPDATE agenda 
             SET nombre=?, apellido=?, telefono=?, email=? 
             WHERE id=?"""
    cursor.execute(sql, (nombre, apellido, telefono, email, id))
    conexion.commit()
    conexion.close()

def borrarContacto(id):
    conexion, cursor = conectar()
    sql = "DELETE FROM agenda WHERE id = ?"
    cursor.execute(sql, (id,))
    conexion.commit()
    conexion.close()
##--------------------------------------------------------------------------------------------------------------------
## LOGIN CREAR USUARIO
def insertarUsuario(datos):
    conexion, cursor = conectar()
    sql = """
    INSERT INTO usuario(nombre_usuario, apellido_usuario, correo_electronico, contrasena, direccion) VALUES(?, ?, ?, ?, ?)
    """
    if cursor.execute(sql, datos):
        print("Datos guardados")
    else:
        print("No se pudieron guardar los datos  del usuario")
    conexion.commit()
    conexion.close()
def borrarUsuario(id):
    conexion, cursor = conectar()
    sql = "DELETE FROM usuario WHERE id_usuario = ?"
    cursor.execute(sql, (id))
    conexion.commit()
    conexion.close()


#--------------------------------------------------------------------------------------------------------------------------
#INSERTAR DATOS QUEMADOS
def insertarCategoria(datos):
    conexion, cursor = conectar()
    sql = """
    INSERT INTO categoria(nombre_categoria) VALUES(?)
    """
    if cursor.execute(sql, datos):
        print("Datos guardados")
    else:
        print("No se pudieron guardar los datos  del usuario")
    conexion.commit()
    conexion.close()
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
    conexion, cursor = conectar()
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
def consultarCategoria():
    conexion, cursor = conectar()
    sql = "SELECT   nombre_categoria FROM categoria"
    cursor.execute(sql)
    listado = []
    for fila in cursor:
        listado.append(fila)    
    conexion.close()
    return listado

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