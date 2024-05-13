from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from imagenes import *
from BD_inicio_sesion_sql import *
from registro import Registro 
class Login:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ventana = Tk()
        self.ventana.title("Inicio de sesión prubea")
        # Obtener dimensiones de la pantalla
        ancho_pantalla = self.ventana.winfo_screenwidth()
        alto_pantalla = self.ventana.winfo_screenheight()
        
        # Dimensiones de la ventana
        ancho_ventana = 500
        alto_ventana = 700
        
        x = (ancho_pantalla // 2) - (ancho_ventana // 2)
        y = (alto_pantalla // 2) - (alto_ventana // 2)
        self.ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")
        
        fondo = "#01172F"
        color_boton = "#08A4BD"
        
        #--------------------------------
        #       parte frames
        #--------------------------------
        
        self.frame_superior = Frame(self.ventana, bg=fondo)
        self.frame_superior.pack(fill="both", expand=True)
        
        self.frame_inferior = Frame(self.ventana, bg=fondo)
        self.frame_inferior.pack(fill="both", expand=True)
        self.frame_inferior.columnconfigure(0, weight=1)
        self.frame_inferior.columnconfigure(1, weight=1)
        
        #--------------------------------
        #       parte del titulo
        #--------------------------------
        
        self.titulo = Label(self.frame_superior,
                            text="Inicio de sesión",
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
        #       parte de los campos de entrada
        #--------------------------------
        
        self.correo = StringVar()
        self.contrasena = StringVar()
        
        campos = [
            ("Correo electrónico:", self.correo, 0),
            ("Contraseña:", self.contrasena, 1)
        ]
        
        self.label_correo_electronico = Label(self.frame_inferior,
                                              text = "Correo electrónico:",
                                              font = ("Arial", 15),
                                              bg = fondo,
                                              fg = "white")
        self.label_correo_electronico.grid(row = 0, column = 0, padx = 10, sticky = "e")
        
        self.entry_correo_electronico = Entry(self.frame_inferior,
                                                   bd = 0,
                                                   width = 20,
                                                   font = ("Arial", 15),textvariable=self.correo)
        self.entry_correo_electronico.grid(row = 0, column = 1, columnspan = 3, padx = 10, sticky = "w")
        
        self.label_contrasena = Label(self.frame_inferior,
                                              text = "Contraseña:",
                                              font = ("Arial", 15),
                                              bg = fondo,
                                              fg = "white")
        self.label_contrasena.grid(row = 1, column = 0, padx = 10, sticky = "e")
        
        self.entry_contrasena = Entry(self.frame_inferior,
                                                   bd = 0,
                                                   width = 20,
                                                   font = ("Arial", 15),
                                                   show = "•",textvariable=self.contrasena)
        self.entry_contrasena.grid(row = 1, column = 1, columnspan = 3, padx = 10, sticky = "w")
        
        # Botones
        self.boton_inicio_sesion = Button(self.frame_inferior,
                                           text="Iniciar sesión",
                                           width=15,
                                           font=("Arial", 15),
                                           background=color_boton,
                                           command=self.inicio_sesion)
        self.boton_inicio_sesion.grid(row=2, column=0, columnspan=2, pady=35)
        
        self.boton_registrarse = Button(self.frame_inferior,
                                        text="Registrarse",
                                        width=15,
                                        font=("Arial", 15),
                                        background=color_boton,
                                        command=self.VentanaRegistrar)
        self.boton_registrarse.grid(row=3, column=0, columnspan=2, pady=10)
        
        self.ventana.mainloop()
        
    def mostrarMensaje(self, titulo, mensaje):
        messagebox.showinfo(titulo, mensaje)

    def limpiar(self):
        self.correo.set("")
        self.contrasena.set("")
        
    def inicio_sesion(self):
        if self.correo.get() == "" or self.contrasena.get() == "":
            self.mostrarMensaje("ERROR", "Debes rellenar los datos")
        else:    
            usuario = iniciarSesion(self.correo.get(),self.contrasena.get())
            if usuario is not None:
                self.mostrarMensaje("Inicio de sesión", "Inicio sesion")
                self.limpiar()
        
    def VentanaRegistrar(self):
        self.ventana.withdraw()
        Registro(self.ventana)
Login()