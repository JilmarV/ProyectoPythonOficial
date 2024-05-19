from BD_conexionsql import Conexion
from Excepciones.UsuarioExistenteError import UsuarioExistenteError
import tkinter as tk
import sqlite3  
from tkinter import messagebox
## LOGIN CREAR USUARIO
def insertarUsuario(datos:tuple):
    conexion, cursor = Conexion.conectar()
    try:
        correo = datos[2]
        validacionUsuarioExistente(correo)
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
    except UsuarioExistenteError as e:
            messagebox.showerror("Error",str(e))

    
def borrarUsuario(id):
        conexion, cursor = Conexion.conectar()
        sql = "DELETE FROM usuario WHERE id_usuario = ?"
        cursor.execute(sql, (id,))
        conexion.commit()
        conexion.close()
        return True

def modificarUsuario(id_usuario, nombre, apellido, correo, contrasena, direccion):
        conexion, cursor = Conexion.conectar()
        try:
            
            validacionUsuarioExistente(correo)
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
        except UsuarioExistenteError as e:
            messagebox.showerror("Error",str(e))

def consultarUsuarios():
    conexion, cursor = Conexion.conectar()
    sql = "SELECT * FROM usuario"
    cursor.execute(sql)
    listado = []
    for fila in cursor:
        listado.append(fila)    
    conexion.close()
    return listado

def validacionUsuarioExistente(correo):
    conexion, cursor = Conexion.conectar()
    sql = "SELECT * FROM usuario WHERE correo_electronico = ?"
    cursor.execute(sql, (correo,))
    usuarioExiste = cursor.fetchone()
    if usuarioExiste:
        raise UsuarioExistenteError()
    conexion.close()