import sqlite3

def conectar():
    conexion = sqlite3.connect("agendaBD")
    cursor = conexion.cursor()
    return conexion,cursor
def crearTabla():
    conexion,cursor = conectar()
    sql = """    
        
    """