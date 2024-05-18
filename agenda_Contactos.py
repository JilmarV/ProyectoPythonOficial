from tkinter import *
from tkinter import messagebox
from BD_contactos import *
from tkinter import ttk
class agenda(Toplevel):
    def __init__(self,id, ventana_padre, *args, **kwargs):
        super().__init__(ventana_padre)
        self.id_usuario = id
        self.title("Agenda")
        
        # Obtener dimensiones de la pantalla
        ancho_pantalla = self.winfo_screenwidth()
        alto_pantalla = self.winfo_screenheight()
        
        # Dimensiones de la ventana
        ancho_ventana = 1000
        alto_ventana = 700
        
        x = (ancho_pantalla // 2) - (ancho_ventana // 2)
        y = (alto_pantalla // 2) - (alto_ventana // 2)
        self.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")
        
        self.colorVentana = "#01172F"
        self.color_boton = "#08A4BD"
        self.color_boton_secundario = "#00635D"
        
        #--------------------------------
        #       parte frames
        #--------------------------------
        
        self.frame = Frame(self, bg=self.colorVentana)
        self.frame.pack(fill="both", expand=True)
        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=1)
        
        #--------------------------------
        #       parte del titulo
        #--------------------------------
        
        self.titulo = Label(self.frame,
                            text="Gestion de contactos",
                            font=("Calisto MT", 26, "bold"),
                            bg=self.colorVentana,
                            fg="white")
        self.titulo.grid(row=1, column=0, columnspan=2, pady=20)
        
        #--------------------------------
        #       parte datos
        #--------------------------------
        
        self.nombre = StringVar()
        self.apellido = StringVar()
        self.email = StringVar()
        self.telefonoUno = IntVar()
        self.telefonoDos = StringVar()
        
        self.etiquetaNombre = Label(self.frame,
                                    text="Nombre: ",
                                    bg=self.colorVentana,
                                    fg="white")
        self.etiquetaNombre.grid(row = 2, column = 0, columnspan = 1, padx = 10, sticky = "e")
        
        self.cajaNombre = Entry(self.frame,
                                textvariable=self.nombre)
        self.cajaNombre.grid(row = 2, column = 1, columnspan = 3, padx = 10, sticky = "w")
        
        self.etiquetaApellido = Label(self.frame,
                                      text="Apellido:",
                                      bg=self.colorVentana,
                                      fg="white")
        self.etiquetaApellido.grid(row = 3, column = 0, padx = 10, sticky = "e")
        
        self.cajaApellido = Entry(self.frame,
                                  textvariable=self.apellido)
        self.cajaApellido.grid(row = 3, column = 1, columnspan = 3, padx = 10, sticky = "w")
        
        self.etiquetaTelefono = Label(self.frame,
                                      text="Telefono:",
                                      bg=self.colorVentana,
                                      fg="white")
        self.etiquetaTelefono.grid(row = 4, column = 0, padx = 10, sticky = "e")
        
        self.cajaTelefono = Entry(self.frame,
                                  textvariable=self.telefonoUno)
        self.cajaTelefono.grid(row = 4, column = 1, columnspan = 3, padx = 10, sticky = "w")
        
        self.label_telefonoDos = Label(self.frame,
                                                text = "Telefono 2:",
                                                bg = self.colorVentana,
                                                fg = "white")
        self.label_telefonoDos.grid(row = 5, column = 0, padx = 10, sticky = "e")
        
        self.entry_telefonoDos = Entry(self.frame,
                                       textvariable=self.telefonoDos)
        self.entry_telefonoDos.grid(row = 5, column = 1, columnspan = 3, padx = 10, sticky = "w")
        
        self.etiquetaEmail = Label(self.frame,
                                   text="Email: ",
                                   bg=self.colorVentana,
                                   fg="white")
        self.etiquetaEmail.grid(row = 6, column = 0, padx = 10, sticky = "e")
        
        self.cajaEmail = Entry(self.frame,
                               textvariable=self.email)
        self.cajaEmail.grid(row = 6, column = 1, columnspan = 3, padx = 10, sticky = "w")
        
        self.etiquetaCombo = Label(self.frame,
                                   text="Categoría: ",
                                   bg=self.colorVentana,
                                   fg="white")
        self.etiquetaCombo.grid(row = 7, column = 0, padx = 10, sticky = "e")
        
        self.combo = ttk.Combobox(self.frame)
        self.combo.grid(row = 7, column = 1, columnspan = 3, padx = 10, sticky = "w")
        
        listaCategoria =  consultarCategoria()
        self.combo['values'] = listaCategoria
        self.combo.current(0)
        #   metodo para cuando el suaurio cambie de seleccion cargarCategoria()
        
        
        self.tree = ttk.Treeview(self.frame, columns=("categoria", "usuario", "nombres", "apellidos", "email", "telefono uno", "telefono dos"), show="headings")

        # Ajuste de las columnas
        self.tree.column("categoria", width=100)
        self.tree.column("usuario", width=100)
        self.tree.column("nombres", width=150)
        self.tree.column("apellidos", width=150)
        self.tree.column("email", width=200)
        self.tree.column("telefono uno", width=100)
        self.tree.column("telefono dos", width=100)

        # Encabezados de las columnas
        self.tree.heading("categoria", text="Categoría")
        self.tree.heading("usuario", text="Usuario")
        self.tree.heading("nombres", text="Nombres")
        self.tree.heading("apellidos", text="Apellidos")
        self.tree.heading("email", text="Email")
        self.tree.heading("telefono uno", text="Teléfono Uno")
        self.tree.heading("telefono dos", text="Teléfono Dos")

        self.tree.grid(row=8, column=0, columnspan=2, padx=10, pady=10)

        self.combo.bind("<<ComboboxSelected>>", self.cargarCategoria)
        
        botonAñadir = Button(self.frame, text="Añadir", command=self.guardarDatos, background=self.color_boton)
        botonAñadir.place(x=200, y=600)
        
        botonBorrar = Button(self.frame, text="Borrar", command=self.borrar_registro, background=self.color_boton)
        botonBorrar.place(x=250, y=600)
        
        botonConsultar = Button(self.frame, text="Consultar", command=self.mostrar, background=self.color_boton)
        botonConsultar.place(x=300, y=600)
        
        botonModificar = Button(self.frame, text="Actualizar", command=self.actualizar, background=self.color_boton)
        botonModificar.place(x=370, y=600)
        
        boton_atras = Button(self.frame,
                                          text = "Atras",
                                          background = self.color_boton_secundario,
                                          command=self.atras)
        boton_atras.place(x=500, y=600)
        
    def cargarCategoria(self, event):
        listado = obtenerContactosPorUsuarioYCategoria(self.id_usuario, self.combo.current() + 1)

        for item in self.tree.get_children():
            self.tree.delete(item)

        for elemento in listado:
            id_categoria_ = elemento[0]
            id_usuario_ = elemento[1]
            nombre_ = elemento[2]
            apellido_ = elemento[3]
            email_ = elemento[4]
            telefono_Uno = elemento[5]
            telefono_Dos = elemento[6]
            self.tree.insert("", "end", values=(id_categoria_, id_usuario_, nombre_, apellido_, email_, telefono_Uno, telefono_Dos))

    def atras(self):
        self.destroy()
        ventanaInicio = self.master
        ventanaInicio.deiconify()

    def mostrarMensaje(self, titulo, mensaje):
        messagebox.showinfo(titulo, mensaje)

    def limpiarDatos(self):
        self.nombre.set("")
        self.apellido.set("")
        self.telefonoUno.set("")
        self.email.set("")
        self.telefonoDos.set("")

    def guardarDatos(self):
        if self.nombre.get() == "" or self.apellido.get() == "":
            self.mostrarMensaje("ERROR", "Debes rellenar los datos")
        else:
            datos = (self.combo.current() + 1, self.id_usuario, self.nombre.get(), self.apellido.get(), self.email.get(), self.telefonoUno.get(), self.telefonoDos.get())
            insertarContacto(datos)
            self.limpiarDatos()

    def actualizar(self):
        seleccion = self.tree.selection()
        if seleccion:
            id_categoria = self.tree.item(seleccion[0], 'values')[0]
            id_usuario = self.tree.item(seleccion[0], 'values')[1]
            datos = (id_usuario, id_categoria, self.nombre.get(), self.apellido.get(), self.email.get(), self.telefonoUno.get(), self.telefonoDos.get())
            modificarContacto(datos)
            self.mostrarMensaje("Modificación", "Se han modificado los datos")
            self.limpiarDatos()
            self.cargarCategoria(None)
        else:
            self.mostrarMensaje("Error", "Seleccione un registro para actualizar")

    def borrar_registro(self):
        seleccion = self.tree.selection()
        if seleccion:
            id_usuario = self.tree.item(seleccion[0], 'values')[1]
            telefono_uno = self.tree.item(seleccion[0], 'values')[5]
            borrarContacto(id_usuario, telefono_uno)
            self.mostrarMensaje("Borrar", "Se ha borrado el contacto")
            self.limpiarDatos()
            self.cargarCategoria(None)
        else:
            self.mostrarMensaje("Error", "Seleccione un registro para borrar")

    def mostrar(self):
        listado = consultarFiltrar()
        self.tree.delete(*self.tree.get_children())
        for elemento in listado:
            id_ = elemento[0]
            nombre_ = elemento[1]
            apellido_ = elemento[2]
            telefono_ = elemento[3]
            email_ = elemento[4]
            self.tree.insert("", "end", values=(id_, "", nombre_, apellido_, email_, telefono_, ""))
