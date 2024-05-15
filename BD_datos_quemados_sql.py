from BD_conexionsql import Conexion
from BD_tablas_sql import crearTablaCategoria
#INSERTAR DATOS QUEMADOS
def insertarCategoria(datos):
    conexion, cursor = Conexion.conectar()
    sql = """
    INSERT INTO categoria(nombre_categoria) VALUES(?)
    """
    if cursor.execute(sql, datos):
        print("Datos guardados")
    else:
        print("No se pudieron guardar los datos  del usuario")
    conexion.commit()
    conexion.close()

nombre_categoria = "OTROS"
#crearTablaCategoria()
insertarCategoria((nombre_categoria,))


""" nombreUser = "ewfwfe"
apellido = "regverg"
correo = "admin"
contrasena = "admin"
direccion = "admwefwfewin"
crearTablaUsuarios()
insertarUsuario((nombreUser,apellido,correo,contrasena,direccion)) """

def borrarContactoAll():
    conexion, cursor = Conexion.conectar()
    sql = """
    DELETE FROM  contacto
    """
    if cursor.execute(sql):
        print("Datos guardados")
    else:
        print("No se pudieron guardar los datos  del usuario")
    conexion.commit()
    conexion.close()
    
borrarContactoAll()