from BD_conexionsql import Conexion

# CRUD DEL CONTACTO
def insertarContacto(datos):
    conexion, cursor = Conexion.conectar()
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
    conexion, cursor = Conexion.conectar()
    sql = "SELECT id,nombre,apellido,telefono,email FROM Contactos"
    cursor.execute(sql)
    listado = []
    for fila in cursor:
        listado.append(fila)    
    conexion.close()
    return listado

def modificarContacto(id, nombre, apellido, telefono, email):
    conexion, cursor = Conexion.conectar()
    sql = """UPDATE agenda 
             SET nombre=?, apellido=?, telefono=?, email=? 
             WHERE id=?"""
    cursor.execute(sql, (nombre, apellido, telefono, email, id))
    conexion.commit()
    conexion.close()

def borrarContacto(id):
    conexion, cursor = Conexion.conectar()
    sql = "DELETE FROM agenda WHERE id = ?"
    cursor.execute(sql, (id,))
    conexion.commit()
    conexion.close()