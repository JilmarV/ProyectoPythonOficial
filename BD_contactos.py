from BD_conexionsql import Conexion

# CRUD DEL CONTACTO
def insertarContacto(datos):
    conexion, cursor = Conexion.conectar()
    sql = """
    INSERT INTO contacto(id_categoria, id_usuario, nombre_contacto, apellido_contacto, email)
    VALUES (?, ?, ?, ?, ?)
    """
    if cursor.execute(sql, datos):
        print("Datos guardados")
    else:
        print("No se pudieron guardar los datos ")
    conexion.commit()
    conexion.close()

def consultarContacto():
    conexion, cursor = Conexion.conectar()
    sql = "SELECT id_contacto, nombre_contacto, apellido_contacto, telefono, email FROM contacto"
    cursor.execute(sql)
    listado = []
    for fila in cursor:
        listado.append(fila)    
    conexion.close()
    return listado

def modificarContacto(id, nombre, apellido, telefono, email):
    conexion, cursor = Conexion.conectar()
    sql = """UPDATE contacto
            SET nombre_contacto=?, apellido_contacto=?, telefono=?, email=?
            WHERE id_contacto=?"""
    cursor.execute(sql, (nombre, apellido, telefono, email, id))
    conexion.commit()
    conexion.close()

def borrarContacto(id):
    conexion, cursor = Conexion.conectar()
    sql = "DELETE FROM contacto WHERE id_contacto = ? OR telefono=?"
    cursor.execute(sql, (id,))
    conexion.commit()
    conexion.close()

def consultarCategoria():
    conexion, cursor = Conexion.conectar()
    sql = "SELECT  nombre_categoria FROM categoria"
    cursor.execute(sql)
    listado = []
    for fila in cursor:
        listado.append(fila)    
    conexion.close()
    return listado
