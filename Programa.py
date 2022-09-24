from pytube import YouTube
import os
from tkinter import *
from tkinter import messagebox as MessageBox
#getcwd: obtiene la ruta de acceso del directorio de trabajo actual para la unidad predeterminada y la almacena en buffer
print(os.getcwd())

def accion():
    enlace=videos.get()
    video = YouTube(enlace)
    descarga = video.streams.get_highest_resolution()
    descarga.download()
    
root = Tk()
root.config(bd=18)
root.title("Script Download")

menubar = Menu(root)
root.config(menu=menubar)
helpmenu = Menu(menubar, tearoff=0)

menubar.add_command(label="leave", command=root.destroy)

instrucciones = Label(root, text="Download youtube videos with Python \n")
instrucciones.grid(row=0, column=1)

videos = Entry(root)
videos.grid(row=1, column=1)

boton = Button(root, text="Download", command=accion)
boton.grid(row=2, column=1)

root.mainloop()
