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
    conexion, cursor = Conexion.conectar()
    sql = "DELETE FROM usuario WHERE id_usuario = ?"
    cursor.execute(sql, (id))
    conexion.commit()
    conexion.close()