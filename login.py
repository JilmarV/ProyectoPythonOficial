from tkinter import *
ANCHO = 400
ALTO = 300
POSX = 550
POSY = 160
anchoAlto = str(ANCHO)+"x"+str(ALTO)
posicionX = "+"+str(POSX)
posicionY = "+"+str(POSY)
colorVentana = "blue"
colorFondo="blue"
colorLetra="white"
ventana= Tk()
ventana.config(bg=colorVentana)
ventana.geometry(anchoAlto+posicionX+posicionY)
ventana.title("Login")
frame = Frame()
frame.config(width=ANCHO,height=ALTO)
frame.config(bg="darkblue")
frame.pack()
#variables
correo_electronico = IntVar()
contrasena = StringVar()
#widgets
lbl_correo_electronico= Label(frame,text = "correo electronico:").place(x=80,y=80)
txt_correo_electronico = Entry(frame,textvariable = "correo_electronico").place(x=200,y=80)
lbl_contrasena= Label(frame,text = "correo electronico:").place(x=80,y=120)
txt_contrasena = Entry(frame,textvariable = "contrasena").place(x=200,y=120)
boton_login= Button(frame,text="Iniciar sesión").place(x=150,y=200)
boton_registro= Button(frame,text="Registrarse").place(x=150,y=230)
ventana.mainloop()