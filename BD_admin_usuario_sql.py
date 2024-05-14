from BD_conexionsql import Conexion

## LOGIN CREAR USUARIO
def insertarUsuario(datos):
    conexion, cursor = Conexion.conectar()
    sql = """
    INSERT INTO usuario(nombre_usuario, apellido_usuario, correo_electronico, contrasena, direccion) VALUES(?, ?, ?, ?, ?)
    """
    if cursor.execute(sql, datos):
        print("Datos guardados")
        conexion.commit()
        conexion.close()
        return True
    else:
        print("No se pudieron guardar los datos  del usuario")
        conexion.commit()
        conexion.close()
        return False
    
def borrarUsuario(id):
    try:
        conexion, cursor = Conexion.conectar()
        sql = "DELETE FROM usuario WHERE id_usuario = ?"
        cursor.execute(sql, (id,))
        conexion.commit()
        conexion.close()
        return True
    except Exception as e:
        print("Error al borrar usuario", e)
        return False

def modificarUsuario(id_usuario, nombre, apellido, correo, contrasena, direccion):
    try:
        conexion, cursor = Conexion.conectar()
        sql = """
            UPDATE usuario 
            SET nombre_usuario = ?, 
                apellido_usuario = ?, 
                correo_electronico = ?, 
                contrasena = ?, 
                direccion = ? 
            WHERE id_usuario = ?
        """
        cursor.execute(sql, (nombre, apellido, correo, contrasena, direccion, id_usuario))
        conexion.commit()
        conexion.close()
        return True  # La modificación se realizó correctamente
    except Exception as e:
        print("Error al modificar usuario", e)
        return False  # Ocurrió un error al intentar modificar el usuario


def consultarUsuarios():
    conexion, cursor = Conexion.conectar()
    sql = "SELECT * FROM usuario"
    cursor.execute(sql)
    listado = []
    for fila in cursor:
        listado.append(fila)    
    conexion.close()
    return listado
