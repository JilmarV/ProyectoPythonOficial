from tkinter import *
from tkinter import messagebox

from PIL import Image, ImageTk

class Login:
    def __init__(self):
        
        self.ventana = Tk()
        
        # Obtener dimensiones de la pantalla
        ancho_pantalla = self.ventana.winfo_screenwidth()
        alto_pantalla = self.ventana.winfo_screenheight()
        # Dimensiones de la ventana
        ancho_ventana = 500
        alto_ventana = 700
        
        x = (ancho_pantalla // 2) - (ancho_ventana // 2)
        y = (alto_pantalla // 2) - (alto_ventana // 2)
        self.ventana.geometry(f"{ancho_ventana}x{alto_ventana}+{x}+{y}")
        self.ventana.title("Inicio de sesión")
        self.ventana.positionfrom
        
        fondo = "#01172F"
        color_boton = "#08A4BD"
        
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
        #       parte de las imagenes
        #--------------------------------
        
        self.label_correo_electronico = Label(self.frame_inferior,
                                              text = "Correo electrónico:",
                                              font = ("Arial", 15),
                                              bg = fondo,
                                              fg = "white")
        self.label_correo_electronico.grid(row = 0, column = 0, padx = 10, sticky = "e")
        
        self.entry_correo_electronico = Entry(self.frame_inferior,
                                                   bd = 0,
                                                   width = 20,
                                                   font = ("Arial", 15))
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
                                                   show = "•")
        self.entry_contrasena.grid(row = 1, column = 1, columnspan = 3, padx = 10, sticky = "w")
        
        self.boton_inicio_sesion = Button(self.frame_inferior,
                                          text = "Iniciar sesión",
                                          width = 15,
                                          font = ("Arial", 15),
                                          background = color_boton,
                                          command = self.inicio_sesion)
        self.boton_inicio_sesion.grid(row = 2, column = 0, columnspan = 2, pady = 35)
        
        self.boton_registrarse = Button(self.frame_inferior,
                                          text = "Registrarse",
                                          width = 15,
                                          font = ("Arial", 15),
                                          background = color_boton,
                                          command = self.registrase)
        self.boton_registrarse.grid(row = 3, column = 0, columnspan = 2, pady = 10)
        
        self.ventana.mainloop()
    
    def inicio_sesion(self):
        correo_electronico = self.entry_correo_electronico.get()
        contrasena = self.entry_contrasena.get()
        
        if correo_electronico == "usuario@" and contrasena == "123" :
            messagebox.showinfo("Acceso correcto", "felicidades shinji (❤️ ω ❤️)")
        else :
            messagebox.showinfo("Acceso incorrecto", "la cagaste shinji (┬┬﹏┬┬)")
    
    def registrase(self):
        mensaje = "Aun no sirve shinji\n\n┗( T﹏T )┛"
        messagebox.showinfo("Aun no sirve shinji", mensaje)

Login()
