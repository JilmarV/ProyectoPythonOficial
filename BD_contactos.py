from BD_conexionsql import Conexion
from Excepciones.CorreoExistenteException import CorreoExistenteException
from Excepciones.TelefonoExistenteException import TelefonoExistenteException
from tkinter import messagebox
# CRUD DEL CONTACTO
def insertarContacto(datos):
    try:
        conexion, cursor = Conexion.conectar()
        validacionCorreoExistente(datos[4])
        validacionTelefonoExistente(datos[5])
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
    except (CorreoExistenteException, TelefonoExistenteException) as e:
        messagebox.showerror("Error", str(e))
def consultarFiltrar(id_contacto,id_categoria):
    conexion, cursor = Conexion.conectar()
    sql = "SELECT id_categoria,id_contacto, nombre_contacto, apellido_contacto, telefono, email FROM contacto"
    cursor.execute(sql)
    listado = []
    for fila in cursor:
        listado.append(fila)    
    conexion.close()
    return listado

def modificarContacto(id_usuario,categoria, nombre, apellido, telefonoUno,telefonoDos, email):
    conexion, cursor = Conexion.conectar()
    sql = """UPDATE contacto
            SET id_categoria=?, nombre_contacto=?,apellido_contacto=?, email=?, telefonoDos=?
            WHERE id_usuario=? OR  telefonoUno=?"""
    cursor.execute(sql, (categoria,nombre,apellido,email,telefonoDos,id_usuario,telefonoUno))
    conexion.commit()
    conexion.close()

def borrarContacto(id_usuario,telefono,nombre):
    conexion, cursor = Conexion.conectar()
    sql = "DELETE FROM contacto WHERE (id_usuario =?) AND (telefonoUno=? OR nombre_contacto=?) "
    if cursor.execute(sql, (id_usuario,telefono,nombre)) != 0:
        print("print se borro")
    else:
        print("print se borro")
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

#consulta contacto
def obtenerContactosPorUsuario(id_usuario):
    conexion, cursor = Conexion.conectar()
    sql = """
    SELECT cat.nombre_categoria, c.id_usuario, c.nombre_contacto, c.apellido_contacto,
    c.email, c.telefonoUno, c.telefonoDos
    FROM contacto c
    INNER JOIN categoria cat ON c.id_categoria = cat.id_categoria
    WHERE c.id_usuario = ?
    """
    cursor.execute(sql, (id_usuario,))
    contactos = cursor.fetchall()
    conexion.close()
    return contactos

def obtenerContactosPorUsuarioYCategoria(id_usuario, id_categoria):
    conexion, cursor = Conexion.conectar()
    sql = """
    SELECT cat.nombre_categoria, c.id_usuario, c.nombre_contacto, c.apellido_contacto,
    c.email, c.telefonoUno, c.telefonoDos
    FROM contacto c
    INNER JOIN categoria cat ON c.id_categoria = cat.id_categoria
    WHERE c.id_usuario = ? AND c.id_categoria = ?
    """
    cursor.execute(sql, (id_usuario, id_categoria))
    contactos = cursor.fetchall()
    conexion.close()
    return contactos

def validacionCorreoExistente(correo):
        conexion, cursor = Conexion.conectar()
        sql = "SELECT * FROM contacto WHERE email = ?"
        cursor.execute(sql, (correo,))
        usuarioExiste = cursor.fetchone()
        if usuarioExiste:
            raise CorreoExistenteException()
        conexion.close()
def validacionTelefonoExistente(telefono):
        conexion, cursor = Conexion.conectar()
        sql = "SELECT * FROM contacto WHERE telefonoUno = ?"
        cursor.execute(sql, (telefono,))
        usuarioExiste = cursor.fetchone()
        if usuarioExiste:
            raise TelefonoExistenteException()
        conexion.close()