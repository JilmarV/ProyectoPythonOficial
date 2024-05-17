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
            email VARCHAR(20) UNIQUE NOT NULL,
            telefonoUno VARCHAR(10)  UNIQUE NOT NULL,
            telefonoDos VARCHAR(10),
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
#crearTablaCategoria()
#crearTablaContactos()
#crearTablaUsuarios()
#--------------------------------------------------------------------------------------------------------------------------
def BORRAR():
    conexion, cursor = Conexion.conectar()
    sql = """    
        DROP  TABLE contacto
        
    """
    if cursor.execute(sql):
        print("Tabla BORRADA  Creada")
    else:
        print("No se pudo crear la tabla ")
    conexion.close()
#BORRAR()
def llenarCategorias():
    # Lista de categorías en el orden especificado
    categorias = ["Todos", "Favoritos", "Amigos", "Trabajo", "Familia", "Otros"]
    
    # Conexión a la base de datos
    conexion, cursor = Conexion.conectar()
    try:
        # Insertar las categorías
        sql_insert = "INSERT INTO categoria (nombre_categoria) VALUES (?)"
        for categoria in categorias:
            cursor.execute(sql_insert, (categoria,))  # Asegurarse de que es una tupla de un solo elemento
        
        # Confirmar los cambios
        conexion.commit()
        print("Categorías insertadas correctamente")
    except Exception as e:
        # Revertir los cambios en caso de error
        conexion.rollback()
        print("No se pudieron insertar las categorías:", e)
    finally:
        # Cerrar la conexión
        conexion.close()

# Llamada a la función para insertar las categorías
llenarCategorias()