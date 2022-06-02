'''

def main():
        root = Tk()
        root.wm_title("Control")
        app = Ventana(root)
        app.mainloop()



if __name__ == "__main__":
    main()

'''
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
from ventana import *

def PaginaPrincipal():

    def main():
        root = Tk()
        root.wm_title("Control")
        app = Ventana(root)
        app.mainloop()


    def run():
        if (usuariotext.get() == "" or contratext.get() == ""):
            messagebox.showwarning("Datos Incompletos", "ERROR, No Ingreso Contraseña o Usuario")
            usuariotext.delete(0, END)
            contratext.delete(0, END)
        else:
            if (usuariotext.get() == "aaa" and contratext.get() == "111"):
                messagebox.showinfo("Iniciando Secion","Parametros Correctos, BIENVENIDO")
                root.destroy()
                main()
                
 
            else:
                messagebox.showerror("Iniciando Secion", "ERROR, Parametros Incorrectos")
                usuariotext.delete(0, END)
                contratext.delete(0, END)
                
    #VENTANA PRINCIPAL
    root = Tk()
    root.title("INGRESO USUARIO")

    #MAINFRAME
    mainFrame = Frame(root)
    mainFrame.pack()
    mainFrame.config(width=500, height=500)

    #TEXTOS Y TITULOS
    titulo = Label(mainFrame, text="Ingreso Del Usuario Administrador", font=("Courier New", 22))
    titulo.grid(column=0, row=0, padx=10, pady=10, columnspan=2)

    usuariolabel = Label(mainFrame, text="Usuario: ", font=("Courier New", 14))
    usuariolabel.grid(column=0, row=1)

    passlabel = Label (mainFrame, text="Contraseña: ", font=("Courier New", 14))
    passlabel.grid(column=0, row=2)

    #ENTRADAS DE TEXTO
    usuario = StringVar()
    usuariotext = Entry(mainFrame, textvariable=usuario, font=("Courier New", 12))
    usuariotext.grid(column=1, row=1)

    contra = StringVar()
    contratext = Entry(mainFrame, textvariable=contra, font=("Courier New", 12), show="*")
    contratext.grid(column=1, row=2)

    #BOTONES
    ingresarButton = Button(mainFrame, text="Ingresar", font=("Courier New", 13), command = run)
    ingresarButton.grid(column=0, row=3, ipadx=5, ipady=5, columnspan=2, padx=10, pady=10,)
    root.mainloop()


if __name__ == "__main__":
    PaginaPrincipal()
