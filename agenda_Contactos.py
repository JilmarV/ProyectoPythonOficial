from tkinter import *
from tkinter import messagebox
from BD_contactos import *
from tkinter import ttk
class agenda(Toplevel):
    def __init__(self,id, ventana_padre, *args, **kwargs):
        super().__init__(ventana_padre)
        self.id_usuario = id
        self.ANCHO = 560
        self.ALTO = 600
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
        self.frame.config(width=self.ANCHO, height=self.ALTO, bg=self.colorVentana)
        self.frame.pack()
        
        self.titulo = Label(self.frame,
                            text="GESTION DE CONTACTOS",
                            font=("Calisto MT", 26, "bold"),
                            bg=self.colorVentana,
                            fg="white")
        self.titulo.place(x=40, y=10)

        self.nombre = StringVar()
        self.apellido = StringVar()
        self.email = StringVar()
        self.telefonoUno = IntVar()
        self.telefonoDos = StringVar()
        
        self.etiquetaNombre = Label(self.frame, text="Nombre: ", bg=self.colorVentana, fg="white").place(x=50, y=90)
        self.cajaNombre = Entry(self.frame, textvariable=self.nombre).place(x=130, y=90)
        self.etiquetaApellido = Label(self.frame, text="Apellido:", bg=self.colorVentana, fg="white").place(x=50, y=130)
        self.cajaApellido = Entry(self.frame, textvariable=self.apellido).place(x=130, y=130)
        self.etiquetaTelefono = Label(self.frame, text="Telefono:", bg=self.colorVentana, fg="white").place(x=50, y=170)
        self.cajaTelefono = Entry(self.frame, textvariable=self.telefonoUno).place(x=130, y=170)
        self.etiquetaEmail = Label(self.frame, text="Email: ", bg=self.colorVentana, fg="white").place(x=50, y=210)
        self.cajaEmail = Entry(self.frame, textvariable=self.email).place(x=130, y=210)
        
        self.label_telefonoDos = Label(self.frame,
                                                text = "Telefono 2:",
                                                bg = self.colorVentana,
                                                fg = "white")
        self.label_telefonoDos.place(x = 300, y =170 )
        
        self.entry_telefonoDos = Entry(self.frame,
                                                    bd = 0,
                                                    width = 20,
                                                    textvariable=self.telefonoDos)
        self.entry_telefonoDos.place(x = 400, y =170 )
        
        self.etiquetaCombo = Label(self.frame, text="Categoría: ", bg=self.colorVentana, fg="white").place(x=300, y=90)
        self.combo = ttk.Combobox(self.frame)
        self.combo.place(x=400,y=90)
        listaCategoria =  consultarCategoria()
        self.combo['values'] = listaCategoria
        self.combo.current(0)
        #   metodo para cuando el suaurio cambie de seleccion cargarCategoria()
        self.text = Text(self.frame)
        self.text.place(x=50, y=240, width=650, height=300)
        self.categoria = self.combo.current()
        self.combo.bind("<<ComboboxSelected>>",self.cargarCategoria)
        botonAñadir = Button(self.frame, text="Añadir", command=self.guardarDatos, background=self.color_boton).place(x=150, y=500)
        botonBorrar = Button(self.frame, text="Borrar", command=self.borrar_registro, background=self.color_boton).place(x=200, y=500)
        botonConsultar = Button(self.frame, text="Consultar", command=self.mostrar, background=self.color_boton).place(x=250, y=500)
        botonModificar = Button(self.frame, text="Actualizar", command=self.actualizar, background=self.color_boton).place(x=320, y=500)
        boton_atras = Button(self.frame,
                                          text = "Atras",
                                          background = self.color_boton_secundario,
                                          command=self.atras).place(x=420, y=500)
    def on_selected(self):
        self.cargarCategoria(self.id_usuario,self.combo.current())
    
    
    def cargarCategoria(self,event):
        listado = obtenerContactosPorUsuarioYCategoria(self.id_usuario,self.combo.current())
        self.text.delete(1.0, END)
        self.text.insert(INSERT, "ID_Categoria\tID_Usuario\tNombre_Contacto\tApellido_Contacto\t\tEmail\tTelefono_Uno\tTelefono_Dos\n")
        for elemento in listado:
            id_categoria_ = elemento[0]
            id_usuario_ = elemento[1]
            nombre_ = elemento[2]
            apellido_ = elemento[3]
            email_ = elemento[4]
            telefono_Uno = elemento[5]
            telefono_Dos = elemento[6]
            self.text.insert(INSERT, id_categoria_)
            self.text.insert(INSERT, "\t")
            self.text.insert(INSERT, id_usuario_)
            self.text.insert(INSERT, "\t")
            self.text.insert(INSERT, nombre_)
            self.text.insert(INSERT, "\t\t")
            self.text.insert(INSERT, apellido_)
            self.text.insert(INSERT, "\t")
            self.text.insert(INSERT, email_)
            self.text.insert(INSERT, "\t")
            self.text.insert(INSERT, telefono_Uno)
            self.text.insert(INSERT, "\t")
            self.text.insert(INSERT, telefono_Dos)
            self.text.insert(INSERT, "\n")
    def atras(self):
        self.destroy()
        ventanaInicio = self.master
        ventanaInicio.deiconify()
        
    def mostrarMensaje(self,titulo, mensaje):
            messagebox.showinfo(titulo, mensaje)

    def limpiarDatos(self):
        self.nombre.set("")
        self.apellido.set("")
        self.telefonoUno.set("")
        self.email.set("")
        self.text.delete(1.0, END)

    def guardarDatos(self):
        if self.nombre.get() == "" or self.apellido.get() == "":
            self.mostrarMensaje("ERROR", "Debes rellenar Los datos")
        else:
            #self.mostrarMensaje("Guardar","Contacto Guardado")
            datos = self.combo.current()+1,self.id_usuario,self.nombre.get(), self.apellido.get(), self.email.get(), self.telefonoUno.get(),self.telefonoDos.get()
            insertarContacto(datos)
            self.limpiarDatos()

    def actualizar(self):
        if  self.nombre.get() == "":
            self.mostrarMensaje("Error", "Debes rellenar los datos ")
        else:
            modificarContacto(self.id_usuario,self.combo.current()+1,self.nombre.get(), self.apellido.get(), self.email.get(), self.telefonoUno.get(),self.telefonoDos.get())
            self.mostrarMensaje("Modificacion", "Se han modificado los datos")
            self.limpiarDatos()

    def borrar_registro(self):
            borrarContacto(self.id_usuario,self.telefonoUno.get(),self.nombre.get())
            self.mostrarMensaje("Borrar", "Se ha borrado el contacto")
            self.limpiarDatos()

    def mostrar(self):
        listado = consultarFiltrar()
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
