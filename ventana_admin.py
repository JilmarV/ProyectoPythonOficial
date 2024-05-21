from tkinter import *
from tkinter import messagebox, ttk
from BD_admin_usuario_sql import *
from PIL import Image, ImageTk
import re
class ventana_admin(Toplevel):
    def __init__(self, ventana_padre, *args, **kwargs):
        super().__init__(ventana_padre)
        self.title("Inicio de sesión")
        
        # Obtener dimensiones de la pantalla
        ancho_pantalla = self.winfo_screenwidth()
        alto_pantalla = self.winfo_screenheight()
        
        # Dimensiones de la ventana
        ancho_ventana = 700
        alto_ventana = 700
        
        x = (ancho_pantalla // 2) - (ancho_ventana // 2)
        y = (alto_pantalla // 2) - (alto_ventana // 2)
        self.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")
        
        fondo = "#01172F"
        color_boton = "#08A4BD"
        color_boton_secundario = "#00635D"
        
        #--------------------------------
        #       parte frames
        #--------------------------------
        
        self.frame_superior = Frame(self, bg=fondo)
        self.frame_superior.pack(fill="both", expand=True)
        self.frame_superior.columnconfigure(0, weight=1)
        self.frame_superior.columnconfigure(1, weight=1)
        
        #--------------------------------
        #       parte del titulo
        #--------------------------------
        
        self.titulo = Label(self.frame_superior,
                            text="Gestion de usuarios",
                            font=("Calisto MT", 36, "bold"),
                            bg=fondo,
                            fg="white")
        self.titulo.grid(row=1, column=0, columnspan=2, pady=20)
        
        #--------------------------------
        #       parte datos
        #--------------------------------
        
        self.nombre = StringVar()
        self.apellido = StringVar()
        self.correo = StringVar()
        self.contrasena = StringVar()
        self.direccion =  StringVar()
        
        self.label_nombre = Label(self.frame_superior,
                                                text = "Nombres:",
                                                font = ("Arial", 15),
                                                bg = fondo,
                                                fg = "white")
        self.label_nombre.grid(row=2, column=0, padx=10, pady=2, sticky="e")
        
        self.entry_nombre = Entry(self.frame_superior,
                                                    bd = 0,
                                                    width = 20,
                                                    font = ("Arial", 15),textvariable=self.nombre)
        self.entry_nombre.grid(row=2, column=1, padx=10, pady=5, sticky="w")
        
        self.label_apellido = Label(self.frame_superior,
                                                text = "Apellidos:",
                                                font = ("Arial", 15),
                                                bg = fondo,
                                                fg = "white")
        self.label_apellido.grid(row=3, column=0, padx=10, pady=2, sticky="e")
        
        self.entry_apellido = Entry(self.frame_superior,
                                                    bd = 0,
                                                    width = 20,
                                                    font = ("Arial", 15),textvariable=self.apellido)
        self.entry_apellido.grid(row=3, column=1, padx=10, pady=5, sticky="w")
        
        self.label_correo_electronico = Label(self.frame_superior,
                                                text = "Correo electrónico:",
                                                font = ("Arial", 15),
                                                bg = fondo,
                                                fg = "white")
        self.label_correo_electronico.grid(row=4, column=0, padx=10, pady=2, sticky="e")
        
        self.entry_correo_electronico = Entry(self.frame_superior,
                                                    bd = 0,
                                                    width = 20,
                                                    font = ("Arial", 15),textvariable=self.correo)
        self.entry_correo_electronico.grid(row=4, column=1, padx=10, pady=5, sticky="w")
        
        self.label_contrasena = Label(self.frame_superior,
                                                text = "Contraseña:",
                                                font = ("Arial", 15),
                                                bg = fondo,
                                                fg = "white")
        self.label_contrasena.grid(row=5, column=0, padx=10, pady=2, sticky="e")
        
        self.entry_contrasena = Entry(self.frame_superior,
                                                    bd = 0,
                                                    width = 20,
                                                    font = ("Arial", 15),textvariable=self.contrasena)
        self.entry_contrasena.grid(row=5, column=1, padx=10, pady=5, sticky="w")
        
        self.label_direccion = Label(self.frame_superior,
                                                text = "Dirección:",
                                                font = ("Arial", 15),
                                                bg = fondo,
                                                fg = "white")
        self.label_direccion.grid(row=6, column=0, padx=10, pady=2, sticky="e")
        
        self.entry_direccion = Entry(self.frame_superior,
                                                    bd = 0,
                                                    width = 20,
                                                    font = ("Arial", 15),textvariable=self.direccion)
        self.entry_direccion.grid(row=6, column=1, padx=10, pady=5, sticky="w")
        
        #--------------------------------
        #       parte tabla
        #--------------------------------
        # Crear la tabla
        self.tree = ttk.Treeview(self.frame_superior, columns=("ID", "Nombres", "Apellidos", "Correo", "Contraseña", "Dirección"), show="headings")

        # Ajuste de las columnas
        self.tree.column("#0", width=50)
        self.tree.column("ID", width=50)  # Ajuste de la columna ID
        self.tree.column("Nombres", width=100)
        self.tree.column("Apellidos", width=100)
        self.tree.column("Correo", width=150)
        self.tree.column("Contraseña", width=100)  # Ajuste de la columna Contraseña
        self.tree.column("Dirección", width=150)

        # Encabezados de las columnas
        self.tree.heading("ID", text="ID")
        self.tree.heading("Nombres", text="Nombres")
        self.tree.heading("Apellidos", text="Apellidos")
        self.tree.heading("Correo", text="Correo Electrónico")
        self.tree.heading("Contraseña", text="Contraseña")  # Encabezado de la columna Contraseña
        self.tree.heading("Dirección", text="Dirección")

        # Agregar Treeview a la interfaz
        self.tree.grid(row=7, column=0, columnspan=2, padx=10, pady=10)
        
        # Llamar a la función para cargar los usuarios en la tabla
        self.cargar_usuarios_en_tabla()
        
        # Otras partes del código...
    
    # Función para cargar los usuarios en la tabla
    
        
        #--------------------------------
        #       parte botones
        #--------------------------------
        
        self.boton_registro_usuario = Button(self.frame_superior,
                                          text = "Crear",
                                          width = 15,
                                          font = ("Arial", 11),
                                          background = color_boton,
                                          command= self.registrase)
        self.boton_registro_usuario.grid(row = 8, column = 0, columnspan = 1, pady = 10)
        
        self.boton_eliminar_usuario = Button(self.frame_superior,
                                          text = "Eliminar",
                                          width = 15,
                                          font = ("Arial", 11),
                                          background = color_boton,
                                          command = self.eliminar_usuario)
        self.boton_eliminar_usuario.grid(row = 8, column = 1, columnspan = 1, pady = 10)
        
        self.boton_buscar_usuario = Button(self.frame_superior,
                                          text = "Buscar",
                                          width = 15,
                                          font = ("Arial", 11),
                                          background = color_boton,
                                          command = self.buscar_usuario)
        self.boton_buscar_usuario.grid(row = 9, column = 0, columnspan = 1, pady = 10)
        
        self.boton_actualizar_usuario = Button(self.frame_superior,
                                          text = "Editar",
                                          width = 15,
                                          font = ("Arial", 11),
                                          background = color_boton,
                                          command = self.modificar)
        self.boton_actualizar_usuario.grid(row = 9, column = 1, columnspan = 3, pady = 10)
        
        self.boton_atras = Button(self.frame_superior,
                                          text = "Atras",
                                          width = 15,
                                          font = ("Arial", 11),
                                          background = color_boton_secundario,
                                          command=self.atras)
        self.boton_atras.grid(row = 10, column = 1, columnspan = 3, pady = 10)
        
        self.entry_nombre.bind("<FocusOut>", self.validar_nombre_apellido)
        self.entry_apellido.bind("<FocusOut>", self.validar_nombre_apellido)
        self.entry_correo_electronico.bind("<FocusOut>", self.validar_correo)
        
    def limpiar(self):
        self.nombre.set("")
        self.apellido.set("")
        self.correo.set("")
        self.contrasena.set("")
        self.direccion.set("")
        
    def registrase(self):
        res = insertarUsuario((self.nombre.get(),self.apellido.get(),self.correo.get(),self.contrasena.get(),self.direccion.get()))
        if(res == True):
            messagebox.showinfo("Registro exitoso", "Se ha registrado el usuario") 
            self.limpiar()
            self.cargar_usuarios_en_tabla()
        else:
            messagebox.showinfo("Registro fallido", "No se ha registrado el usuario") 
    
    def eliminar_usuario(self):
        # Obtener el ID del usuario seleccionado en la tabla
        seleccion = self.tree.selection()
        if seleccion:
            id_usuario = self.tree.item(seleccion[0], 'values')[0]
            borrarUsuario(id_usuario)
            self.cargar_usuarios_en_tabla()
        else:
            messagebox.showinfo("Eliminar usuario", "Seleccione un usuario para eliminar.")
        
    def cargar_usuarios_en_tabla(self):
        usuarios = consultarUsuarios()
        
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        for usuario in usuarios:
            self.tree.insert("", "end", values=usuario)

    def modificar(self):
        seleccion = self.tree.selection()
        if seleccion:
            id_usuario = self.tree.item(seleccion[0], 'values')[0]
            nombre = self.nombre.get()
            apellido = self.apellido.get()
            correo = self.correo.get()
            contrasena = self.contrasena.get()
            direccion = self.direccion.get()
            res = modificarUsuario(id_usuario, nombre, apellido, correo, contrasena, direccion)
            if res == True:
                messagebox.showinfo("Registro exitoso", "Se ha registrado el usuario") 
                self.limpiar()
                self.cargar_usuarios_en_tabla()
            else:
                messagebox.showinfo("Modificación fallida", "Modificación fallida") 
        else:
            messagebox.showinfo("Modificación fallida", "Seleccione un usuario")

    def atras(self):
        self.destroy()
        ventanaInicio = self.master
        ventanaInicio.deiconify()
            
    def buscar_usuario(self):
    # Obtener la fila seleccionada
        item = self.tree.selection()
        if not item:
            messagebox.showinfo("Error", "Por favor, seleccione un usuario de la tabla.")
            return
        
        # Obtener los valores de la fila seleccionada
        valores = self.tree.item(item, 'values')
        
        self.nombre.set(valores[1])
        self.apellido.set(valores[2])
        self.correo.set(valores[3])
        self.contrasena.set(valores[4])
        self.direccion.set(valores[5])
        
    #----------------------------------
    #         meta-caracteres
    #----------------------------------
    
    def validar_correo(self, event):
        correo = self.correo.get()
        patron = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(patron, correo):
            messagebox.showerror("Error de validación", "El correo electrónico no es válido")

    def validar_nombre_apellido(self, event):
        texto = event.widget.get()
        patron = r'^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s\'\-]+$'
        if not re.match(patron, texto):
            messagebox.showerror("Error de validación", "El campo solo puede contener letras y caracteres especiales")
