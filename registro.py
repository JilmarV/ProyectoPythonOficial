
from tkinter import *
from tkinter import messagebox
from BD_admin_usuario_sql import *
from PIL import Image, ImageTk
class Registro:
    def __init__(self,ventana_Login:Tk):
        self.ventana = Tk()
        self.ventanaLogin = ventana_Login
        # Obtener dimensiones de la pantalla
        ancho_pantalla = self.ventana.winfo_screenwidth()
        alto_pantalla = self.ventana.winfo_screenheight()
        # Dimensiones de la ventana
        ancho_ventana = 500
        alto_ventana = 700
        
        x = (ancho_pantalla // 2) - (ancho_ventana // 2)
        y = (alto_pantalla // 2) - (alto_ventana // 2)
        self.ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")
        self.ventana.title("Registro de usuario")
        self.ventana.positionfrom
        
        fondo = "#01172F"
        color_boton = "#08A4BD"
        color_boton_secundario = "#00635D"
        
        #--------------------------------
        #       parte frames
        #--------------------------------
        
        self.frame_superior = Frame(self.ventana)
        self.frame_superior.configure(bg=fondo)
        self.frame_superior.pack(fill="both", expand=True)
        
        self.frame_inferior = Frame(self.ventana)
        self.frame_inferior.configure(bg = fondo)
        self.frame_inferior.pack(fill="both", expand=True)
        self.frame_inferior.columnconfigure(0, weight=1)
        self.frame_inferior.columnconfigure(1, weight=1)

                
        #--------------------------------
        #       parte del titulo
        #--------------------------------
        
        self.titulo = Label(self.frame_superior,
                            text="Registro de usuario",
                            font=("Calisto MT", 36, "bold"),
                            bg=fondo,
                            fg="white")
        self.titulo.pack(side="top", pady=20)
        
        #--------------------------------
        #       parte de imagenes
        #--------------------------------
        
        self.img = Image.open("imagenes/user_icon_124042.png")
        self.img = self.img.resize((150, 150))
        self.render = ImageTk.PhotoImage(self.img)
        self.label_imagen = Label(self.frame_superior, image=self.render, bg=fondo)
        self.label_imagen.pack(side="top", pady=20) 
        
        #--------------------------------
        #       parte de datos
        #--------------------------------
        self.nombre = StringVar()
        self.apellido = StringVar()
        self.correo = StringVar()
        self.contrasena = StringVar()
        self.direccion = StringVar()
        
        self.label_nombre_usuario = Label(self.frame_inferior,
                                              text = "Nombres:",
                                              font = ("Arial", 15),
                                              bg = fondo,
                                              fg = "white")
        self.label_nombre_usuario.grid(row = 0, column = 0, padx = 10, sticky = "e")
        
        self.entry_nombre_usuario = Entry(self.frame_inferior,
                                                   bd = 0,
                                                   width = 20,
                                                   font = ("Arial", 15),textvariable=self.nombre)
        self.entry_nombre_usuario.grid(row = 0, column = 1, columnspan = 3, padx = 10, sticky = "w")
        
        self.label_apellido_usuario = Label(self.frame_inferior,
                                              text = "Apellidos:",
                                              font = ("Arial", 15),
                                              bg = fondo,
                                              fg = "white")
        self.label_apellido_usuario.grid(row = 1, column = 0, padx = 10, sticky = "e")
        
        self.entry_apellido_usuario = Entry(self.frame_inferior,
                                                   bd = 0,
                                                   width = 20,
                                                   font = ("Arial", 15),textvariable=self.apellido)
        self.entry_apellido_usuario.grid(row = 1, column = 1, columnspan = 3, padx = 10, sticky = "w")
        
        self.label_correo_electronico = Label(self.frame_inferior,
                                              text = "Correo electrónico:",
                                              font = ("Arial", 15),
                                              bg = fondo,
                                              fg = "white")
        self.label_correo_electronico.grid(row = 2, column = 0, padx = 10, sticky = "e")
        
        self.entry_correo_electronico = Entry(self.frame_inferior,
                                                   bd = 0,
                                                   width = 20,
                                                   font = ("Arial", 15),textvariable=self.correo)
        self.entry_correo_electronico.grid(row = 2, column = 1, columnspan = 3, padx = 10, sticky = "w")
        
        self.label_contrasena = Label(self.frame_inferior,
                                              text = "Contraseña:",
                                              font = ("Arial", 15),
                                              bg = fondo,
                                              fg = "white")
        self.label_contrasena.grid(row = 3, column = 0, padx = 10, sticky = "e")
        
        self.entry_contrasena = Entry(self.frame_inferior,
                                                   bd = 0,
                                                   width = 20,
                                                   font = ("Arial", 15),textvariable=self.contrasena)
        self.entry_contrasena.grid(row = 3, column = 1, columnspan = 3, padx = 10, sticky = "w")
        
        self.label_direccion = Label(self.frame_inferior,
                                      text = "direccion",
                                      font = ("Arial", 15),
                                      bg = fondo,
                                      fg = "white")
        self.label_direccion.grid(row = 4, column = 0, padx = 10, sticky = "e")
        
        self.entry_direccion = Entry(self.frame_inferior,
                                                   bd = 0,
                                                   width = 20,
                                                   font = ("Arial", 15),textvariable=self.direccion)
        self.entry_direccion.grid(row = 4, column = 1, columnspan = 3, padx = 10, sticky = "w")
        
        self.boton_registro_usuario = Button(self.frame_inferior,
                                          text = "Registrarme",
                                          width = 15,
                                          font = ("Arial", 15),
                                          background = color_boton,
                                          command = self.registrase)
        self.boton_registro_usuario.grid(row = 5, column = 0, columnspan = 1, pady = 35)
        
        self.boton_atras = Button(self.frame_inferior,
                                          text = "Atras",
                                          width = 15,
                                          font = ("Arial", 15),
                                          background = color_boton_secundario,command=self.atras)
        self.boton_atras.grid(row = 5, column = 1, columnspan = 1, pady = 35)
        
        self.ventana.mainloop()
        
    def registrase(self):
        res = insertarUsuario((self.nombre.get(),self.apellido.get(),self.correo.get(),self.contrasena.get(),self.direccion.get()))
        if(res == True):
            messagebox.showinfo("Aun no sirve", "Se ha registrado el usuario") 
        else:
            messagebox.showinfo("Aun no sirve", "No Se ha registrado el usuario") 
    def atras(self):
        self.ventana.withdraw
        self.ventanaLogin.deiconify()
