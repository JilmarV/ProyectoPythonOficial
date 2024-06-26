from tkinter import *
from tkinter import messagebox
from BD_contactos import *
from tkinter import ttk
import re
class agenda(Toplevel):
    def __init__(self,id, ventana_padre, *args, **kwargs):
        super().__init__(ventana_padre)
        self.id_usuario = id
        self.title("Agenda")
        
        # Obtener dimensiones de la pantalla
        ancho_pantalla = self.winfo_screenwidth()
        alto_pantalla = self.winfo_screenheight()
        
        # Dimensiones de la ventana
        ancho_ventana = 900
        alto_ventana = 650
        
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
        self.cajaNombre.grid(row = 2, column = 1, columnspan = 1, padx = 10, sticky = "w")
        
        self.etiquetaApellido = Label(self.frame,
                                      text="Apellido:",
                                      bg=self.colorVentana,
                                      fg="white")
        self.etiquetaApellido.grid(row = 3, column = 0, padx = 10, sticky = "e")
        
        self.cajaApellido = Entry(self.frame,
                                  textvariable=self.apellido)
        self.cajaApellido.grid(row = 3, column = 1, columnspan = 1, padx = 10, sticky = "w")
        
        self.etiquetaTelefono = Label(self.frame,
                                      text="Telefono:",
                                      bg=self.colorVentana,
                                      fg="white")
        self.etiquetaTelefono.grid(row = 4, column = 0, padx = 10, sticky = "e")
        
        self.cajaTelefono = Entry(self.frame,
                                  textvariable=self.telefonoUno)
        self.cajaTelefono.grid(row = 4, column = 1, columnspan = 1, padx = 10, sticky = "w")
        
        self.label_telefonoDos = Label(self.frame,
                                                text = "Telefono 2:",
                                                bg = self.colorVentana,
                                                fg = "white")
        self.label_telefonoDos.grid(row = 5, column = 0, padx = 10, sticky = "e")
        
        self.entry_telefonoDos = Entry(self.frame,
                                       textvariable=self.telefonoDos)
        self.entry_telefonoDos.grid(row = 5, column = 1, columnspan = 1, padx = 10, sticky = "w")
        
        self.etiquetaEmail = Label(self.frame,
                                   text="Email: ",
                                   bg=self.colorVentana,
                                   fg="white")
        self.etiquetaEmail.grid(row = 6, column = 0, padx = 10, sticky = "e")
        
        self.cajaEmail = Entry(self.frame,
                               textvariable=self.email)
        self.cajaEmail.grid(row = 6, column = 1, columnspan = 1, padx = 10, sticky = "w")
        
        self.etiquetaCombo = Label(self.frame,
                                   text="Categoría: ",
                                   bg=self.colorVentana,
                                   fg="white")
        self.etiquetaCombo.grid(row = 7, column = 0, padx = 10, sticky = "e")
        
        self.combo = ttk.Combobox(self.frame)
        self.combo.grid(row = 7, column = 1, columnspan = 1, padx = 10, sticky = "w")
        
        listaCategoria =  consultarCategoria()
        self.combo['values'] = listaCategoria
        self.combo.current(0)
        #   metodo para cuando el suaurio cambie de seleccion cargarCategoria()
        
        self.tree = ttk.Treeview(self.frame, columns=("categoria", "nombres", "apellidos", "email", "telefono uno", "telefono dos"), show="headings")

        # Ajuste de las columnas
        self.tree.column("categoria", width=100)
        self.tree.column("nombres", width=100)
        self.tree.column("apellidos", width=100)
        self.tree.column("email", width=200)
        self.tree.column("telefono uno", width=150)
        self.tree.column("telefono dos", width=150)

        # Encabezados de las columnas
        self.tree.heading("categoria", text="Categoría")
        self.tree.heading("nombres", text="Nombres")
        self.tree.heading("apellidos", text="Apellidos")
        self.tree.heading("email", text="Email")
        self.tree.heading("telefono uno", text="Teléfono Uno")
        self.tree.heading("telefono dos", text="Teléfono Dos")

        self.tree.grid(row=8, column=0, columnspan=2, padx=10, pady=10)

        self.combo.bind("<<ComboboxSelected>>", self.cargarCategoria)
        
        botonAñadir = Button(self.frame,
                             text="Añadir",
                             command=self.guardarDatos,
                             background=self.color_boton,
                             width=10)
        botonAñadir.grid(row=9, column=0, columnspan=1, padx=10, pady=10)
        
        botonBorrar = Button(self.frame,
                             text="Borrar",
                             command=self.borrar_registro_seleccionado,
                             background=self.color_boton,
                             width=10)
        botonBorrar.grid(row=9, column=1, columnspan=1, padx=10, pady=10)
        
        botonConsultar = Button(self.frame,
                                text="Consultar",
                                command=self.cargar_datos_seleccionados,
                                background=self.color_boton,
                                width=10)
        botonConsultar.grid(row=10, column=1, columnspan=1, padx=10, pady=10)
        
        botonModificar = Button(self.frame,
                                text="Actualizar",
                                command=self.modificar_contacto,
                                background=self.color_boton,
                                width=10)
        botonModificar.grid(row=10, column=0, columnspan=1, padx=10, pady=10)
        
        boton_atras = Button(self.frame,
                                          text = "Atras",
                                          background = self.color_boton_secundario,
                                          command=self.atras,
                                          width=10)
        boton_atras.grid(row=11, column=0, columnspan=1, padx=10, pady=10)
        
        boton_limpiar = Button(self.frame,
                                          text = "Ver todos",
                                          background = self.color_boton_secundario,
                                          command=self.cargarCategoriaInicio,
                                          width=10)
        boton_limpiar.place(x=600, y=190)
        
        self.cargarCategoriaInicio()
        
        #----------------------------------------
        #Parte llamado metodo velidacion meta caracteres
        #--------------------------------------------
        
        self.cajaEmail.bind("<FocusOut>", self.validar_correo)
        self.cajaTelefono.bind("<FocusOut>", self.validar_telefono)
        self.entry_telefonoDos.bind("<FocusOut>", self.validar_telefono)
        self.cajaNombre.bind("<FocusOut>", self.validar_nombre_apellido)
        self.cajaApellido.bind("<FocusOut>", self.validar_nombre_apellido)
        
    def cargarCategoria(self, event):
        listado = obtenerContactosPorUsuarioYCategoria(self.id_usuario, self.combo.current() + 1)

        for item in self.tree.get_children():
            self.tree.delete(item)

        for elemento in listado:
            id_categoria_ = elemento[0]
            nombre_ = elemento[2]
            apellido_ = elemento[3]
            email_ = elemento[4]
            telefono_Uno = elemento[5]
            telefono_Dos = elemento[6]
            self.tree.insert("", "end", values=(id_categoria_, nombre_, apellido_, email_, telefono_Uno, telefono_Dos))
            
    def cargarCategoriaInicio(self):
        listado = obtenerContactosPorUsuario(self.id_usuario)

        for item in self.tree.get_children():
            self.tree.delete(item)

        for elemento in listado:
            id_categoria_ = elemento[0]
            nombre_ = elemento[2]
            apellido_ = elemento[3]
            email_ = elemento[4]
            telefono_Uno = elemento[5]
            telefono_Dos = elemento[6]
            self.tree.insert("", "end", values=(id_categoria_, nombre_, apellido_, email_, telefono_Uno, telefono_Dos))

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
            self.cargarCategoriaInicio()
            self.limpiarDatos()

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
    
    def cargar_datos_seleccionados(self):
        seleccion = self.tree.selection()

        if seleccion:
            valores = self.tree.item(seleccion[0], 'values')
            
            self.nombre.set(valores[1])
            self.apellido.set(valores[2])
            self.email.set(valores[3])
            self.telefonoUno.set(valores[4])
            self.telefonoDos.set(valores[5])
            id_categoria = valores[0]
            if id_categoria in self.combo['values']:
                self.combo.current(self.combo['values'].index(id_categoria))
            else:
                self.combo.current(0)
        else:
            messagebox.showinfo("Información", "Por favor, seleccione una fila para cargar los datos")
            
    def borrar_registro_seleccionado(self):
        seleccion = self.tree.selection()
        
        if seleccion:
            id_usuario = self.id_usuario
            telefono_uno = self.tree.item(seleccion[0], 'values')[4]
            nombre = self.tree.item(seleccion[0], 'values')[1]
            
            borrarContacto(id_usuario, telefono_uno, nombre)
            
            messagebox.showinfo("Borrar", "Se ha borrado el contacto")
            
            self.limpiarDatos()
            self.cargarCategoriaInicio()
        else:
            messagebox.showinfo("Información", "Por favor, seleccione una fila para borrar el contacto")
    
    def modificar_contacto(self):
        seleccion = self.tree.selection()
        
        if seleccion:
            id_usuario = self.id_usuario
            categoria = self.combo.current() + 1 
            nombre = self.nombre.get()
            apellido = self.apellido.get()
            telefonoUno = self.telefonoUno.get()
            telefonoDos = self.telefonoDos.get()
            email = self.email.get()
            
            modificarContacto(id_usuario, categoria, nombre, apellido, telefonoUno, telefonoDos, email)
            
            messagebox.showinfo("Modificación", "Se han modificado los datos")
            
            self.limpiarDatos()
            self.cargarCategoria(None)
        else:
            messagebox.showinfo("Información", "Por favor, seleccione una fila para modificar el contacto")

    #----------------------------------
    #         meta-caracteres
    #----------------------------------
    
    def validar_correo(self, event):
        correo = self.email.get()
        patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(patron, correo):
            messagebox.showerror("Error de validación", "El correo electrónico no es válido")
            
    def validar_telefono(self, event):
        telefono = event.widget.get()
        if not telefono.isdigit() or len(telefono) != 10:
            messagebox.showerror("Error de validación", "El número de teléfono debe contener solo dígitos y tener 10 caracteres")
            
    def validar_nombre_apellido(self, event):
        texto = event.widget.get()
        patron = r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s\'\-]+$'
        if not re.match(patron, texto):
            messagebox.showerror("Error de validación", "El campo solo puede contener letras y caracteres especiales")
