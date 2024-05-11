from tkinter import *
from tkinter import messagebox
from BD import *

ANCHO = 560
ALTO = 540
POSX = 400
POSY = 400

def mostrarMensaje(titulo, mensaje):
    messagebox.showinfo(titulo, mensaje)

def limpiarDatos():
    nombre.set("")
    apellido.set("")
    telefono.set("")
    email.set("")
    text.delete(1.0, END)

def guardarDatos():
    crearTablaContactos()
    if nombre.get() == "" or apellido.get() == "":
        mostrarMensaje("ERROR", "Debes rellenar Los datos")
    else:
        datos = nombre.get(), apellido.get(), telefono.get(), email.get()
        mostrarMensaje("Guardar", "Contacto Guardado")
        insertarContacto(datos)
        limpiarDatos()

def actualizar():
    crearTablaContactos()
    if ID.get() == "" and nombre.get() == "":
        mostrarMensaje("Error", "Debes rellenar los datos ")
    else:
        modificarContacto(ID.get(), nombre.get(), apellido.get(), telefono.get(), email.get())
        mostrarMensaje("Modificacion", "Se han modificado los datos")
        limpiarDatos()

def borrar_registro():
    if ID.get() == "":
        mostrarMensaje("Error", "No se encontro el contacto")
    else:
        borrarContacto(ID.get())
        mostrarMensaje("Borrar", "Se ha borrado el contacto")
        limpiarDatos()

def mostrar():
    listado = consultarContacto()
    text.delete(1.0, END)
    text.insert(INSERT, "ID\tNombre\tApellido\t\tTelefono\tEmail\n")
    for elemento in listado:
        id_ = elemento[0]
        nombre_ = elemento[1]
        apellido_ = elemento[2]
        telefono_ = elemento[3]
        email_ = elemento[4]
        text.insert(INSERT, id_)
        text.insert(INSERT, "\t")
        text.insert(INSERT, nombre_)
        text.insert(INSERT, "\t")
        text.insert(INSERT, apellido_)
        text.insert(INSERT, "\t\t")
        text.insert(INSERT, telefono_)
        text.insert(INSERT, "\t")
        text.insert(INSERT, email_)
        text.insert(INSERT, "\n")

anchoAlto = str(ANCHO) + "x" + str(ALTO)
posicionX = "+" + str(POSX)
posicionY = "+" + str(POSY)
colorVentana = "blue"

ventana = Tk()
ventana.config(bg=colorVentana)
ventana.geometry(anchoAlto + posicionX + posicionY)
ventana.title("Agenda")

frame = Frame()
frame.config(width=ANCHO, height=ALTO, bg="darkblue")
frame.pack()

ID = IntVar()
nombre = StringVar()
apellido = StringVar()
telefono = StringVar()
email = StringVar()

etiquetaID = Label(frame, text="ID: ").place(x=50, y=50)
cajaID = Entry(frame, textvariable=ID).place(x=130, y=50)
etiquetaNombre = Label(frame, text="Nombre: ").place(x=50, y=90)
cajaNombre = Entry(frame, textvariable=nombre).place(x=130, y=90)
etiquetaApellido = Label(frame, text="Apellido:").place(x=50, y=130)
cajaApellido = Entry(frame, textvariable=apellido).place(x=130, y=130)
etiquetaTelefono = Label(frame, text="Telefono").place(x=50, y=170)
cajaTelefono = Entry(frame, textvariable=telefono).place(x=130, y=170)
etiquetaEmail = Label(frame, text="Email: ").place(x=50, y=210)
cajaEmail = Entry(frame, textvariable=email).place(x=130, y=210)

text = Text(frame)
text.place(x=50, y=240, width=500, height=200)

botonAñadir = Button(frame, text="Añadir", command=guardarDatos).place(x=150, y=500)
botonBorrar = Button(frame, text="Borrar", command=borrar_registro).place(x=200, y=500)
botonConsultar = Button(frame, text="Consultar", command=mostrar).place(x=250, y=500)
botonModificar = Button(frame, text="Actualizar", command=actualizar).place(x=320, y=500)

ventana.mainloop()













