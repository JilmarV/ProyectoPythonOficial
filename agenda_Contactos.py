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
        ancho_ventana = 800
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
        self.text = Text(self.frame)
        self.text.place(x=80, y=240, width=650, height=300)
        self.categoria = self.combo.current()
        self.combo.bind("<<ComboboxSelected>>",self.cargarCategoria)
        
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
        
    def on_selected(self):
        self.cargarCategoria(self.id_usuario,self.combo.current())
    
    
    def cargarCategoria(self,event):
        listado = obtenerContactosPorUsuarioYCategoria(self.id_usuario,self.combo.current())
        self.text.delete(1.0, END)
        self.text.insert(INSERT, "Id Categoria\tID Usuario\tNombre\tApellido\t\tEmail\tTelefono Uno\tTelefono Dos\n")
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
