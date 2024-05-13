from conexionsql import Conexion

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
