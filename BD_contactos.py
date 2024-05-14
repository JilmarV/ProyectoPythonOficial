from BD_conexionsql import Conexion

# CRUD DEL CONTACTO
def insertarContacto(datos):
    conexion, cursor = Conexion.conectar()
    sql = """
    INSERT INTO contacto(id_categoria, id_usuario, nombre_contacto, apellido_contacto, email,telefonoUno,telefonoDos)
    VALUES (?,?,?,?,?,?,?)
    """
    if cursor.execute(sql, datos):
        print("Datos guardados")
    else:
        print("No se pudieron guardar los datos ")
    conexion.commit()
    conexion.close()

def consultarFiltrar(id_contacto,id_categoria):
    conexion, cursor = Conexion.conectar()
    sql = "SELECT id_categoria,id_contacto, nombre_contacto, apellido_contacto, telefono, email FROM contacto"
    cursor.execute(sql)
    listado = []
    for fila in cursor:
        listado.append(fila)    
    conexion.close()
    return listado

def modificarContacto(id_contacto,categoria, nombre, apellido, telefonoUno,telefonoDos, email):
    conexion, cursor = Conexion.conectar()
    sql = """UPDATE contacto
            SET id_categoria=?, nombre_contacto=?, apellido_contacto=?, email=?, telefonoUno=?, telefonoDos=?
            WHERE id_contacto=?"""
    cursor.execute(sql, (categoria,nombre, apellido,email,telefonoUno,telefonoDos,id_contacto))
    conexion.commit()
    conexion.close()

def borrarContacto(id_contacto,telefono):
    conexion, cursor = Conexion.conectar()
    sql = "DELETE FROM contacto WHERE id_contacto = ? OR telefono=?"
    cursor.execute(sql, (id_contacto,telefono))
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
