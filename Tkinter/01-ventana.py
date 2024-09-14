#Tkinter es un módulo para crear interfaces gráficas de usuario
import tkinter as tk
import os
from PIL import Image, ImageTk



#Establecer un icono en la ventana
"""
Windows
root=Tk() #crear la ventana raiz
ventana.iconbitmap("logos/icono.ico")
"""
#Linux
root = tk.Tk() #crear la ventana raiz
im = Image.open("logos/icono02.png")
photo = ImageTk.PhotoImage(im)
root.wm_iconphoto(True, photo)

#Redimensionar la ventana
root.geometry("750x450")

#Bloquear el tamaño de la ventana
root.resizable(1,1) #Esto indica los ejes que se bloquean de acurdo a la posición 1=bloqueo (vertical,horizontal)


#Debemos iniciar la ventana
root.mainloop()
