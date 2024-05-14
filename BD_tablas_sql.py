from BD_conexionsql import Conexion

#-------------------------------------------------------------------------------------------------------------------------------------
def crearTablaContactos():
    conexion, cursor = Conexion.conectar()
    sql = """    
        CREATE TABLE IF NOT EXISTS contacto(
            id_contacto INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            id_categoria int,
            id_usuario int NOT NULL,
            nombre_contacto VARCHAR(60) NOT NULL,
            apellido_contacto VARCHAR(60) NOT NULL,
            email VARCHAR(20) NOT NULL,
            CONSTRAINT id_de_usuario FOREIGN KEY (id_usuario) REFERENCES usuario(id_usuario),
            CONSTRAINT id_de_categoria FOREIGN KEY (id_categoria) REFERENCES categoria(id_categoria)
        )
    """
    if cursor.execute(sql):
        print("Tabla De Contacto Creada")
    else:
        print("No se pudo crear la tabla ")
    conexion.close()

def crearTablaUsuarios():
    conexion, cursor = Conexion.conectar()
    sql = """    
        CREATE TABLE IF NOT EXISTS usuario(
            id_usuario INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            nombre_usuario  VARCHAR (20)NOT NULL,
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
    conexion, cursor = Conexion.conectar()
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
    conexion, cursor = Conexion.conectar()
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
    conexion, cursor = Conexion.conectar()
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

crearTablaContactos()
crearTablaUsuarios()
#--------------------------------------------------------------------------------------------------------------------------
