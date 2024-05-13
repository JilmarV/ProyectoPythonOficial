import sqlite3
class Conexion :
    def conectar():
        conexion = sqlite3.connect("agendaBD.sqlite3")
        cursor = conexion.cursor()
        return conexion, cursor