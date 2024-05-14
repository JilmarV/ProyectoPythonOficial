from tkinter import *
from tkinter import messagebox
from BD import *
class agenda(Toplevel):
    def __init__(self,id, ventana_padre, *args, **kwargs):
        super().__init__(ventana_padre)
        self.id_usuario = id
        self.ANCHO = 560
        self.ALTO = 540
        self.POSX = 400
        self.POSY = 400
        self.anchoAlto = str(self.ANCHO) + "x" + str(self.ALTO)
        self.posicionX = "+" + str(self.POSX)
        self.posicionY = "+" + str(self.POSY)
        
        self.colorVentana = "#01172F"
        self.color_boton = "#08A4BD"
        self.color_boton_secundario = "#00635D"

        self.config(bg=self.colorVentana)
        self.geometry(self.anchoAlto + self.posicionX + self.posicionY)
        self.title("Agenda")

        self.frame = Frame(self)
        self.frame.config(width=self.ANCHO, height=self.ALTO, bg="darkblue")
        self.frame.pack()

        self.ID = IntVar()
        self.nombre = StringVar()
        self.apellido = StringVar()
        self.telefono = StringVar()
        self.email = StringVar()

        self.etiquetaID = Label(self.frame, text="ID: ").place(x=50, y=50)
        self.cajaID = Entry(self.frame, textvariable=self.ID).place(x=130, y=50)
        self.ID.set(str(self.id_usuario))
        self.etiquetaNombre = Label(self.frame, text="Nombre: ").place(x=50, y=90)
        self.cajaNombre = Entry(self.frame, textvariable=self.nombre).place(x=130, y=90)
        self.etiquetaApellido = Label(self.frame, text="Apellido:").place(x=50, y=130)
        self.cajaApellido = Entry(self.frame, textvariable=self.apellido).place(x=130, y=130)
        self.etiquetaTelefono = Label(self.frame, text="Telefono").place(x=50, y=170)
        self.cajaTelefono = Entry(self.frame, textvariable=self.telefono).place(x=130, y=170)
        self.etiquetaEmail = Label(self.frame, text="Email: ").place(x=50, y=210)
        self.cajaEmail = Entry(self.frame, textvariable=self.email).place(x=130, y=210)

        self.text = Text(self.frame)
        self.text.place(x=50, y=240, width=500, height=200)

        botonAñadir = Button(self.frame, text="Añadir", command=self.guardarDatos, background=self.color_boton).place(x=150, y=500)
        botonBorrar = Button(self.frame, text="Borrar", command=self.borrar_registro, background=self.color_boton).place(x=200, y=500)
        botonConsultar = Button(self.frame, text="Consultar", command=self.mostrar, background=self.color_boton).place(x=250, y=500)
        botonModificar = Button(self.frame, text="Actualizar", command=self.actualizar, background=self.color_boton).place(x=320, y=500)


    def mostrarMensaje(titulo, mensaje):
            messagebox.showinfo(titulo, mensaje)

    def limpiarDatos(self):
        self.nombre.set("")
        self.apellido.set("")
        self.telefono.set("")
        self.email.set("")
        self.text.delete(1.0, END)

    def guardarDatos(self):
        crearTablaContactos()
        if self.nombre.get() == "" or self.apellido.get() == "":
            self.mostrarMensaje("ERROR", "Debes rellenar Los datos")
        else:
            datos = self.nombre.get(), self.apellido.get(), self.telefono.get(), self.email.get()
            self.mostrarMensaje("Guardar", "Contacto Guardado")
            self.insertarContacto(datos)
            self.limpiarDatos()

    def actualizar(self):
        crearTablaContactos()
        if self.ID.get() == "" and self.nombre.get() == "":
            self.mostrarMensaje("Error", "Debes rellenar los datos ")
        else:
            self.modificarContacto(self.ID.get(), self.nombre.get(), self.apellido.get(), self.telefono.get(), self.email.get())
            self.mostrarMensaje("Modificacion", "Se han modificado los datos")
            self.limpiarDatos()

    def borrar_registro(self):
        if self.ID.get() == "":
            self.mostrarMensaje("Error", "No se encontro el contacto")
        else:
            self.borrarContacto(self.ID.get())
            self.mostrarMensaje("Borrar", "Se ha borrado el contacto")
            self.limpiarDatos()

    def mostrar(self):
        listado = consultarContacto()
        self.text.delete(1.0, END)
        self.text.insert(INSERT, "ID\tNombre\tApellido\t\tTelefono\tEmail\n")
        for elemento in listado:
            id_ = elemento[0]
            nombre_ = elemento[1]
            apellido_ = elemento[2]
            telefono_ = elemento[3]
            email_ = elemento[4]
            self.text.insert(INSERT, id_)
            self.text.insert(INSERT, "\t")
            self.text.insert(INSERT, nombre_)
            self.text.insert(INSERT, "\t")
            self.text.insert(INSERT, apellido_)
            self.text.insert(INSERT, "\t\t")
            self.text.insert(INSERT, telefono_)
            self.text.insert(INSERT, "\t")
            self.text.insert(INSERT, email_)
            self.text.insert(INSERT, "\n")
