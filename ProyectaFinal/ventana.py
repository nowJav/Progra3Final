from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from Conexion import Connect


class Ventana(Frame):

    con = Connect()
    
    def __init__(self,master=None):
        super().__init__(master,width=750,height=300)
        self.master = master
        self.pack()
        self.create_widgets()
        self.Visualizar()
        self.habilitarCajas("disabled")
        self.habilitarBotones("normal")
        self.habilitarBotonesGuardar("disabled")
        self.id = -1
        
    
    def limpiar_cajas(self):
        self.txtcodigo.delete(0,END)
        self.txtnombre.delete(0,END)
        self.txttipo.delete(0,END)
        self.txtestatus.delete(0,END)
        self.txtfecha.delete(0,END)
        

    def habilitarCajas(self,estado):
        self.txtcodigo.configure(state=estado)
        self.txtnombre.configure(state=estado)
        self.txttipo.configure(state=estado)
        self.txtestatus.configure(state=estado)
        self.txtfecha.configure(state=estado)
        

    def habilitarBotones(self,estado):
        self.nuevo.configure(state=estado)
        self.modificar.configure(state=estado)
        self.eliminar.configure(state=estado)

    def habilitarBotonesGuardar(self,estado):
        self.aceptar.configure(state=estado)
        self.cancelar.configure(state=estado)
    
    def limpiarGrid(self):
        for item in self.grid.get_children():
            self.grid.delete(item)
        

    def Visualizar(self):
        datos = self.con.consulta()

        for row in datos:
            self.grid.insert("",END,text=row[0], values=(row[1],row[2], row[3], row[4],row[5]))

        if len(self.grid.get_children()) > 0:
            self.grid.selection_set(self.grid.get_children()[0])


    def fNuevo(self):
        self.habilitarCajas("normal")
        self.habilitarBotones("disabled")
        self.habilitarBotonesGuardar("normal")
        self.limpiar_cajas()
        self.txtcodigo.focus()
           
    def fModificar(self):
        selected = self.grid.focus()
        clv = self.grid.item(selected,'text')
        if clv == '':
            messagebox.showwarning("Modificar","Debes seleccionar un elemento")
        else:
            self.id = clv
            self.habilitarCajas("normal")
            val = self.grid.item(selected,'values')
            self.limpiar_cajas()
            self.txtcodigo.insert(0,val[0])
            #self.txtcodigo.configure(state="disabled")
            self.txtnombre.insert(0,val[1])
            self.txttipo.insert(0,val[2])
            self.txtestatus.insert(0,val[3])
            self.txtfecha.insert(0,val[4])
            self.habilitarBotones("disabled")
            self.habilitarBotonesGuardar("normal")   
            self.txtnombre.focus()

    def fEliminar(self):
        selected = self.grid.focus()
        clv = self.grid.item(selected,'text')
        if clv == '':
            messagebox.showwarning("Eliminar","Debes seleccionar un elemento")
        else:
            val = self.grid.item(selected,'values')
            data = str(clv) + ", " + val[0] + ", "+ val[1] + ", " + str(val[2])
            r = messagebox.askquestion("Eliminar", "Deseas eliminar el registro seleccionado? \n"+ data)
            if r == messagebox.YES:
                x = self.con.eliminar(clv)
                if x==1:
                    messagebox.showwarning("Eliminar", "No fue posible eliminar el elemento")
                    
                else:
                    messagebox.showinfo("Eliminar", "Elemento eliminado correctamente")
                    self.limpiarGrid()
                    self.Visualizar()

    def fAceptar(self):
        '''
        self.con.insertar(self.txtcodigo.get(),self.txtnombre.get(),self.txttipo.get(),self.txtestatus.get(),self.txtfecha.get())
        messagebox.showinfo("Insertar", "Datos Insertados correctamente") ''' 
        
        if self.id == -1:
            self.con.insertar(self.txtcodigo.get(),self.txtnombre.get(),self.txttipo.get(),self.txtestatus.get(),self.txtfecha.get())
            messagebox.showinfo("Insertar", "Datos Insertados correctamente")
            
        else: 
            self.con.modificar(self.id,self.txtcodigo.get(),self.txtnombre.get(),self.txttipo.get(),self.txtestatus.get())
            messagebox.showinfo("Modificar", "Datos Modificados correctamente")
            self.id = -1
            #self.txtcodigo.configure(state="normal")
    
        self.limpiarGrid()
        self.Visualizar()
        self.limpiar_cajas()
        self.habilitarBotonesGuardar("disabled")
        self.habilitarBotones("normal")
        self.habilitarCajas("disabled")    
        
        
    
    def fCancelar(self):
        r = messagebox.askquestion("Cancelar", "Deseas cancelar el proceso actual?")
        if r == messagebox.YES:
            self.txtcodigo.configure(state="normal")
            self.limpiar_cajas()
            self.habilitarBotonesGuardar("disabled")
            self.habilitarBotones("normal")
            self.habilitarCajas("disabled")  


    def create_widgets(self):
        frame1 = Frame(self, bg="#bfdaff")
        frame1.place(x=0,y=0,width=93,height=300)
        self.nuevo = Button(frame1,text="Nuevo", command=self.fNuevo, bg="white", fg="black")
        self.nuevo.place(x=5,y=50,width=80,height=30)
        self.modificar = Button(frame1,text="Modificar", command=self.fModificar, bg="white", fg="black")
        self.modificar.place(x=5,y=90,width=80,height=30)
        self.eliminar = Button(frame1,text="Eliminar", command=self.fEliminar, bg="white", fg="black")
        self.eliminar.place(x=5,y=130,width=80,height=30)
        
        frame2 = Frame(self, bg="#d3dde3")
        frame2.place(x=95,y=0,width=150,height=300)        
        lbl1 = Label(frame2,text="Codigo: ")
        lbl1.place(x=3,y=5)
        self.txtcodigo = Entry(frame2)
        self.txtcodigo.place(x=3,y=25,width=100,height=20)
        lbl2 = Label(frame2,text="Nombre: ")
        lbl2.place(x=3,y=55)
        self.txtnombre = Entry(frame2)
        self.txtnombre.place(x=3,y=75,width=100,height=20)
        lbl3 = Label(frame2,text="Tipo: ")
        lbl3.place(x=3,y=105)
        self.txttipo = Entry(frame2)
        self.txttipo.place(x=3,y=125,width=100,height=20)
        lbl4 = Label(frame2,text="Estatus: ")
        lbl4.place(x=3,y=155)
        self.txtestatus = Entry(frame2)
        self.txtestatus.place(x=3,y=175,width=100,height=20)
        lbl5 = Label(frame2,text="Fecha: ")
        lbl5.place(x=3,y=200)
        self.txtfecha = Entry(frame2)
        self.txtfecha.place(x=3,y=225,width=100,height=20)      
        self.aceptar = Button(frame2,text="Aceptar", command=self.fAceptar, bg="white", fg="black")
        self.aceptar.place(x=10,y=255,width=60,height=30)
        self.cancelar = Button(frame2,text="Cancelar", command=self.fCancelar, bg="white", fg="black")
        self.cancelar.place(x=80,y=255,width=60,height=30)

        frame3 = Frame(self, bg="#d3dde3")
        frame3.place(x=247,y=0,width=500,height=300) 
        self.grid = ttk.Treeview(frame3,columns=("col1","col2","col3","col4","col5"))
        self.grid.column("#0",width=50,anchor=CENTER)
        self.grid.column("col1",width=95,anchor=CENTER)
        self.grid.column("col2",width=95,anchor=CENTER)
        self.grid.column("col3",width=95,anchor=CENTER)
        self.grid.column("col4",width=50,anchor=CENTER)
        self.grid.column("col5",width=100,anchor=CENTER)
        self.grid.heading("#0",text="Id",anchor=CENTER)
        self.grid.heading("col1",text="Codigo", anchor=CENTER)
        self.grid.heading("col2",text="Nombre", anchor=CENTER)
        self.grid.heading("col3",text="Tipo", anchor=CENTER)
        self.grid.heading("col4",text="Estatus", anchor=CENTER)
        self.grid.heading("col5",text="Fecha", anchor=CENTER)
        self.grid.pack(side=LEFT, fill= Y)
        sb = Scrollbar(frame3,orient=VERTICAL)
        sb.pack(side=RIGHT,fill= Y)
        self.grid.config(yscrollcommand=sb.set)
        sb.config(command=self.grid.yview)
        self.grid['selectmode']='browse'
        