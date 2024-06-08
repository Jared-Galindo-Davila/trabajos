#LIBRERIAS IMPORTADA 
from tkinter import Tk, Label, Button, Entry, ttk, messagebox, Toplevel, Menu
import pymysql
from tkinter import *
from datetime import datetime
import sys
import tkinter as tk

#VARIABLES ACUMULATIVAS 
tvControlEmpleado = None
tvControlFactura = None
ventanaEmpleado = None

#FUNCIONES 

#FUNCION DE HORA
def actualizar_fecha_hora(label):
    ahora = datetime.now()
    fecha_hora_actual = ahora.strftime("%Y-%m-%d %H:%M:%S")
    label.config(text=f"Fecha y Hora Actual:\n{fecha_hora_actual}")

    label.after(1000, lambda: actualizar_fecha_hora(label))

#FUNCION DE FACTURA 

def ventana_factura():
    global tvControlFactura

    #SUBVENTANAS DE FACTURA 
     
     
    
    def eliminarFactura():
        #MY SQL
        try:
            query= "delete from factura where id_factura= %s"
            id_factura= txtFactura.get()
        
            c.execute(query, (id_factura))
            j.commit()
            messagebox.showinfo(message="Factura Eliminada Satisfactoriamente.")
            ListadoFactura()
        except Exception as ex:
            messagebox.showerror(message=ex)

    def nuevoFactura():
        #ELIMINAR EL TEXTO
        txtFactura.delete(0, "end")
        txtNombre_ClientefACTURA.delete(0, "end")
        txtTelefono_Facturacion.delete(0, "end")
        comboone.set("")
        combotwo.set("")
        combotree.set("")
        txtCantidadFacturacion.delete(0, "end")
        combofourd.set("")
        txtFactura.focus()


    def modificarFactura():
        #MY SQL
        try:
            query="update factura set nombre_cliente= %s, telefono_factura= %s , categoria= %s, sub_categoria=%s, articulo=%s, cantidad=%s, precio=%s where id_factura= %s"
            id_factura= txtFactura.get()
            nombre_cliente= txtNombre_ClientefACTURA.get()
            telefono_factura=txtTelefono_Facturacion.get()
            categoria= comboone.get()
            sub_categoria= combotwo.get()
            articulo= combotree.set("")
            cantidad= txtCantidadFacturacion.get()
            precio = combofourd.get()
            c.execute(query,(nombre_cliente, telefono_factura, categoria, sub_categoria, articulo, cantidad, precio, id_factura))
            j.commit()
            messagebox.showinfo(message="Factura Modificada Satisfactoriamente.")
            ListadoFactura()
            nuevoFactura()
        except Exception as ex:
            messagebox.showerror(message=ex)
    def ListadoFactura():
        #VARIABLE GLOBAL 
        global tvControlFactura
        query= "select * from factura"
        c.execute(query)
        datos= c.fetchall()

        #CONCIONAL 
        for item in tvControlFactura.get_children():
            tvControlFactura.delete(item)
        for reg in datos:
            tvControlFactura.insert("", "end", text=reg[0], values=(reg[1], reg[2], reg[3], reg[4], reg[5], reg[6], reg[7]))
        
        #OPERACION TOTAL
        totalArticulos=len(datos)
        lblTotalArticulos.config(text="Total Articulos: {}".format(totalArticulos))
    def registrarFactura():
        #MY SQL
        try:
            query = "insert into factura values(%s, %s, %s, %s, %s, %s, %s, %s)"
            id_factura = txtFactura.get()
            nombre_cliente = txtNombre_ClientefACTURA.get()
            telefono_cliente = txtTelefono_Facturacion.get()
            categoria = comboone.get()
            sub_categoria = combotwo.get()  
            articulo = combotree.get()  
            cantidad = txtCantidadFacturacion.get()
            precio = combofourd.get()  

            if not id_factura or not nombre_cliente or not telefono_cliente or not categoria or not sub_categoria or not articulo or not cantidad or not precio:
                messagebox.showwarning(message="Por favor, complete todos los campos.")
                return
            c.execute(query, (id_factura, nombre_cliente, telefono_cliente, categoria, sub_categoria, articulo, cantidad, precio))
            j.commit()
            messagebox.showinfo(message="La Factura {} fue registrada satisfactoriamente.".format(id_factura))
            ListadoFactura()
        except Exception as ex:
            messagebox.showerror(message=ex)

            
    def total():
        #MY SQL
        try:
            query = "select * from factura"
            c.execute(query)
            datos = c.fetchall()

            totalArticulos = len(datos)
            lblTotalArticulos.config(text="Total Articulos: {}".format(totalArticulos))
            messagebox.showinfo(message="El Total de Facturas es: {}".format(totalArticulos))
        except Exception as ex:
            messagebox.showerror(message=ex)


            
    def buscar():
        id_factura = txtFactura.get()
        try:
        # Consulta SQL con un parámetro
            query = "SELECT * FROM factura WHERE id_factura = %s"
        
        # Ejecutar la consulta con el parámetro
            c.execute(query, (id_factura,))
        
        # Obtener los resultados de la consulta
            datos = c.fetchall()

        # Limpiar el Treeview
            for item in tvControlFacturacion.get_children():
                tvControlFacturacion.delete(item)

        # Insertar los resultados en el Treeview
            for reg in datos:
                tvControlFacturacion.insert("", "end", text=reg[0], values=(reg[1], reg[2], reg[3], reg[4], reg[5], reg[6], reg[7]))

        except Exception as ex:
            messagebox.showerror(message=ex)
            


    # VENTANA FACTURA 
    ventanaFacturacion=Toplevel(ventana)
    ventanaFacturacion.title("Factura")
    ventanaFacturacion.geometry("900x500")
    ventanaFacturacion.resizable(0,0)
    ventanaFacturacion.config(bg="#FF0000")

    #TITULO
    Label(ventanaFacturacion, text="ꜰᴀᴄᴛᴜʀᴀᴄɪᴏɴ", bg="#FF0000",fg="#FFF", font=("Algerian", 20, "bold")).pack()


    #DECORACIÓN DE MARCOS DE FONDOS
    marco = Frame(ventanaFacturacion, bd=1, relief="solid",bg="#FF0000")
    marco.place(x=10, y=40, width=880, height=40)
    
    marco = Frame(ventanaFacturacion, bd=1, relief="solid",bg="#FF0000")
    marco.place(x=10, y=400, width=400, height=90)
    
    marco = Frame(ventanaFacturacion, bd=1, relief="solid",bg="#FF0000")
    marco.place(x=10, y=100, width=400, height=290)
    
    marco = Frame(ventanaFacturacion, bd=1, relief="solid",bg="#FF0000")
    marco.place(x=420, y=100, width=470, height=390)
    
    marco = Frame(ventanaFacturacion, bg="lemon chiffon", bd=1, relief="solid")
    marco.place(x=530, y=110, width=245, height=90)
    
    #UN PEQUEÑO TEXTO 
    label_encima_marco = Label(ventanaFacturacion, text="Informacion de Cliente",fg="#FFF", bg="#FF0000", font=("Arial", 12, "bold"))
    label_encima_marco.place(x=10, y=15)
    
    #TEXTO
    Label(ventanaFacturacion, text="Factura No.",bg="#FF0000",fg="#FFF").place(x=20, y=50)
    #CAJA 
    txtFactura= Entry(ventanaFacturacion, width=20)
    txtFactura.place(x=90, y=50)
    
    #TEXTO
    Label(ventanaFacturacion, text="Nombre del Cliente:",bg="#FF0000",fg="#FFF").place(x=290, y=50)
    #CAJA
    txtNombre_ClientefACTURA= Entry(ventanaFacturacion, width=30)
    txtNombre_ClientefACTURA.place(x=400, y=50)
    
    #TEXTO
    Label(ventanaFacturacion, text="Telefono:",bg="#FF0000",fg="#FFF").place(x=600, y=50)
    #CAJA
    txtTelefono_Facturacion= Entry(ventanaFacturacion, width=35)
    txtTelefono_Facturacion.place(x=660, y=50)
    
    #TEXTO
    Label(ventanaFacturacion, text="Cantidad:",bg="#FF0000",fg="#FFF").place(x=20, y=265)
    #CAJA
    txtCantidadFacturacion = Entry(ventanaFacturacion, width=63)
    txtCantidadFacturacion.place(x=20, y=285)

    #serias los textos de la VENTANA FACTURACION
    Label(ventanaFacturacion, text="Articulos:",font="bold",bg="#FF0000",fg="#FFF").place(x=30, y=85)
    Label(ventanaFacturacion, text="Vista Factura:",font="bold",bg="#FF0000",fg="#FFF").place(x=450, y=85)
    Label(ventanaFacturacion, text="Super 'El Porvenir'",bg="lemon chiffon", font="bold").place(x=580, y=120)
    Label(ventanaFacturacion, text="RFC: 5A24X541C35'",bg="lemon chiffon").place(x=590, y=140)
    Label(ventanaFacturacion, text="Plaza Central no. 64,C.P.4720 Tel. 952532115",bg="lemon chiffon").place(x=535, y=155)
    Label(ventanaFacturacion, text="NuevaPeruYork City",bg="lemon chiffon").place(x=590, y=170)


    #LOS BOTONES DE  LA VENTANA " FACTURACION "
    Button(ventanaFacturacion, text="Total", bg="#66150D",fg="#FFF", width=10, command=total).place(x=50, y=430)
    Button(ventanaFacturacion, text="Generar", bg="#66150D",fg="#FFF", width=10, command=registrarFactura).place(x=130, y=430)
    Button(ventanaFacturacion, text="Limpiar", bg="#66150D",fg="#FFF", width=10, command=nuevoFactura).place(x=210, y=430)
    Button(ventanaFacturacion, text="Salir", bg="#66150D",fg="#FFF", width=10, command=Salir).place(x=290, y=430)
    
    Button(ventanaFacturacion, text="Buscar", bg="#66150D",fg="#FFF",command=buscar).place(x=220, y=45)
    
    Button(ventanaFacturacion, text="Eliminar", bg="#66150D",fg="#FFF", width=10, command=eliminarFactura).place(x=130, y=355)
    Button(ventanaFacturacion, text="Limpiar", bg="#66150D",fg="#FFF", width=10, command=nuevoFactura).place(x=210, y=355)
    

    #DECORACION  VENTANA FACTURA 
    lblFechaHora = Label(ventanaFacturacion, text="",bg="#FF0000",fg="#FFF", font=("Arial", 9,"bold"))
    lblFechaHora.place(x=760, y=3)
    
    #INICA LA FECHA Y HORA
    actualizar_fecha_hora(lblFechaHora)
    
    #TEXTO
    Label(ventanaFacturacion, text="Seleccionar Categoria",fg="#FFF",bg="#FF0000").place(x=20, y=130)
    #CAJA
    comboone = ttk.Combobox(ventanaFacturacion, state="readonly", width=60 ,values=["Juguetes", "Electrodomesticos", "Alimentos"])
    comboone.place(x=20, y=150)
    
    #TEXTO
    Label(ventanaFacturacion, text="Sub-Categoria:",bg="#FF0000",fg="#FFF").place(x=20, y=175)
    #CAJA
    combotwo = ttk.Combobox(ventanaFacturacion, state="readonly", width=60 ,values=["Armables", "No Destruibles", "Destruibles"])
    combotwo.place(x=20, y=195)
    
    #TEXTO
    Label(ventanaFacturacion, text="Artículo:",bg="#FF0000",fg="#FFF").place(x=20, y=220)
    #CAJA
    combotree = ttk.Combobox(ventanaFacturacion, state="readonly", width=60 ,values=["Lego", "Plastilina"])
    combotree.place(x=20, y=240)
    
    #TEXTI
    Label(ventanaFacturacion, text="Precio:",bg="#FF0000",fg="#FFF").place(x=20, y=305)
    #CAJA
    combofourd = ttk.Combobox(ventanaFacturacion, state="readonly", width=60 ,values=["120 Soles", "150 Soles"])
    combofourd.place(x=20, y=325)
    
    #TEXTO DE "VENTANA  FACTURA "
    Label(ventanaFacturacion, text="Cliente:",bg="#FF0000",fg="#FFF").place(x=450, y=220)
    Label(ventanaFacturacion, text="Factura No.",bg="#FF0000",fg="#FFF").place(x=450, y=240)
    Label(ventanaFacturacion, text="Telefono:",bg="#FF0000",fg="#FFF").place(x=720, y=220)
    Label(ventanaFacturacion, text="Fecha:",bg="#FF0000",fg="#FFF").place(x=730, y=240)
    
    #COLUMNAS DE LA TABLA "VENTANA FACTURA "
    tvControlFacturacion= ttk.Treeview(ventanaFacturacion, columns=("col1", "col2", "col3", "col4", "col5", "col6", "col7"), height=8)
    tvControlFacturacion.column("#0",width=70)
    tvControlFacturacion.column("col1",width=50)
    tvControlFacturacion.column("col2",width=60)
    tvControlFacturacion.column("col3",width=60)
    tvControlFacturacion.column("col4",width=60)
    tvControlFacturacion.column("col5",width=60)
    tvControlFacturacion.column("col6",width=50)
    tvControlFacturacion.column("col7",width=50)

    tvControlFacturacion.heading("#0", text="N. FACTURA")
    tvControlFacturacion.heading("col1", text="NOMBRE")
    tvControlFacturacion.heading("col2", text="TELEFONO")
    tvControlFacturacion.heading("col3", text="CATEGORIA")
    tvControlFacturacion.heading("col4", text="SUB CATEGORIA")
    tvControlFacturacion.heading("col5", text="ARTICULO")
    tvControlFacturacion.heading("col6", text="CANTIDAD")
    tvControlFacturacion.heading("col7", text="PRECIO")
    tvControlFacturacion.place(x=423, y=290)
    
    lblTotalArticulos= Label(ventanaFacturacion, text="Total Articulos: 0",bg="#FF0000",fg="#FFF")
    lblTotalArticulos.place(x=450, y=260)
   
#FUNCIONES
def crear():
    global tvControlEmpleado
    global tvControlCrear
    
    #SUBFUNCION
    def eliminar():
        #MY SQL
        try:
            query= "delete from empleados where id_empleado= %s"
            id_empleado= txtIDEmpleado.get()
        
            c.execute(query, (id_empleado))
            j.commit()
            messagebox.showinfo(message="Empleados Eliminados Satisfactoriamente.")
            Listado()
        except Exception as ex:
            messagebox.showerror(message=ex)

    #SUBFUNCION

    def nuevo():
        #ELIMINAR TEXTO ESCRITO
        txtIDEmpleado.delete(0, "end")
        txtNombre.delete(0, "end")
        txtTelefo.delete(0, "end")
        txtDomi.delete(0, "end")
        txtDni.delete(0, "end")
        txtContra.delete(0, "end")
        txtDesig.delete(0, "end")
        txtIDEmpleado.focus()


    #SUBFUNCION
    def modificar():
        #MY SQL
        try:
            query="update empleados set nombre= %s, telefono= %s , domicilio= %s, dni=%s, contraseña=%s, designacion=%s where id_empleado= %s"
            id_empleado= txtIDEmpleado.get()
            nombre= txtNombre.get()
            telefono=txtTelefo.get()
            domicilio= txtDomi.get()
            dni= txtDni.get()
            contraseña= txtContra.get()
            designacion= txtDesig.get()
            c.execute(query,(nombre, telefono, domicilio, dni, contraseña, designacion, id_empleado))
            j.commit()
            messagebox.showinfo(message="Empleado Modificado Satisfactoriamente.")
            Listado()
            nuevo()
        except Exception as ex:
            messagebox.showerror(message=ex)

     #SUBFUNCION    
    def Listado():
        global tvControlEmpleado
        query= "select * from empleados"
        c.execute(query)
        datos= c.fetchall()
    
        for item in tvControlCrear.get_children():
            tvControlEmpleado.delete(item)
            tvControlCrear.delete(item)
        for reg in datos:
            tvControlEmpleado.insert("", "end", text=reg[0], values=(reg[1], reg[2], reg[3], reg[4], reg[5], reg[6]))
            tvControlCrear.insert("", "end", text=reg[0], values=(reg[1], reg[2], reg[3], reg[4], reg[5], reg[6]))
        
        totalEmpleados=len(datos)
        lblTotalEmpleados.config(text="Total Empleados: {}".format(totalEmpleados))


    #SUBFUNCION
    def registrar():
        try:
            query= "insert into empleados values(%s, %s, %s, %s, %s, %s, %s)"
            id_empleado=txtIDEmpleado.get()
            nombre= txtNombre.get()
            telefono= txtTelefo.get()
            domicilio= txtDomi.get()
            dni= txtDni.get()
            contraseña= txtContra.get()
            designacion= txtDesig.get()
            c.execute(query,(id_empleado, nombre, telefono, domicilio, dni, contraseña, designacion))
            j.commit()
            messagebox.showinfo(message="El Empleado {} Registrado Satisfactoriamente.".format(nombre))
            Listado()
        except Exception as ex:
            messagebox.showerror(message=ex)


    #VENTANA DE "CREAR"        
    ventanacrear = Toplevel(ventana, bg="#FF0000")
    ventanacrear.title("Ventana Crear Empleados")
    Label(ventanacrear, text="ᴍᴀɴᴛᴇɴɪᴍɪᴇɴᴛᴏ ᴅᴇ ᴇᴍᴘʟᴇᴀᴅᴏꜱ",fg="#FFF", bg="#FF0000", font=("Algerian", 16, "bold")).place(x=380,y=10)
    ventanacrear.geometry("900x440")
    ventanacrear.resizable(0,0)
    
    #DISEÑO
    lblFechaHora = Label(ventanacrear, text="", fg="#FFF", bg="#FF0000", font=("Arial", 10,"bold"))
    lblFechaHora.place(x=755, y=5)

    #INICALIZACION DE "FECHA Y HORA "
    actualizar_fecha_hora(lblFechaHora)
    
    # TEXTO
    Label(ventanacrear, text="ID Empleado: ", fg="snow", bg="#FF0000").place(x=10, y=49)
    #CAJA 
    txtIDEmpleado= Entry(ventanacrear, width=30)
    txtIDEmpleado.place(x=10, y=70)

    #TEXTO
    Label(ventanacrear, text="Nombre: ", fg="snow", bg="#FF0000").place(x=10, y=89)
    #CAJA
    txtNombre= Entry(ventanacrear, width=30)
    txtNombre.place(x=10, y=110)

    #TEXTO
    Label(ventanacrear, text="Telefono: ", fg="snow", bg="#FF0000").place(x=10, y=129)
    #CAJA
    txtTelefo= Entry(ventanacrear, width=30)
    txtTelefo.place(x=10, y=150)

    #TEXTO 
    Label(ventanacrear, text="Domicilio: ", fg="snow", bg="#FF0000").place(x=10, y=169)
    #CAJA 
    txtDomi= Entry(ventanacrear, width=30)
    txtDomi.place(x=10, y=190)
    
    #TEXTO
    Label(ventanacrear, text="DNI: ", fg="snow", bg="#FF0000").place(x=10, y=215)
    #CAJA
    txtDni= Entry(ventanacrear, width=30)
    txtDni.place(x=10, y=235)

    #TEXTO
    Label(ventanacrear, text="Contraseña: ", fg="snow", bg="#FF0000").place(x=10, y=255)
    #CAJA
    txtContra= Entry(ventanacrear, width=30)
    txtContra.place(x=10, y=280)
    
    #TEXTO
    Label(ventanacrear, text="Designacion: ", fg="snow", bg="#FF0000").place(x=10, y=305)
    #CAJA
    txtDesig= Entry(ventanacrear, width=30)
    txtDesig.place(x=10, y=330)

    #BOTONES DE "CENTANA CREAR"
    Button(ventanacrear, text="Registrar",bg="#66150D",fg="#FFF", width=12, command=registrar).place(x=10, y=380)
    Button(ventanacrear, text="Modificar",bg="#66150D",fg="#FFF", width=12, command=modificar).place(x=103, y=380)
    Button(ventanacrear, text="Eliminar",bg="#66150D",fg="#FFF", width=12, command=eliminar).place(x=193, y=380)
    Button(ventanacrear, text="Nuevo",bg="#66150D",fg="#FFF", width=12,command=nuevo).place(x=283, y=380)
    

    #COLUMNAS DE LA TABLA " VENTANA CREAR"
    tvControlCreacion= ttk.Treeview(ventanacrear, columns=("col1", "col2", "col3", "col4", "col5", "col6"))
    tvControlCreacion.column("#0",width=120)
    tvControlCreacion.column("col1",width=100)
    tvControlCreacion.column("col2",width=80)
    tvControlCreacion.column("col3",width=80)
    tvControlCreacion.column("col4",width=90)
    tvControlCreacion.column("col5",width=90)
    tvControlCreacion.column("col6",width=100)

    tvControlCreacion.heading("#0", text="ID EMPLADO")
    tvControlCreacion.heading("col1", text="NOMBRE")
    tvControlCreacion.heading("col2", text="TELEFONO")
    tvControlCreacion.heading("col3", text="DOMICILIO")
    tvControlCreacion.heading("col4", text="DNI")
    tvControlCreacion.heading("col5", text="CONTRASEÑA")
    tvControlCreacion.heading("col6", text="DESIGNACION")
    tvControlCreacion.place(x=210, y=50)

    lblTotalEmpleados = Label(ventanacrear, text="Total Empleados: 0", fg="#FFF", bg="#FF0000",font=14)
    lblTotalEmpleados.place(x=680, y=300)
    
    #FUNCIONES GLOBALES PARA QUE FUNCIONE EL PROCEDIMIENTO 
    global tvControlEmplea
    global ventana_empleado


#FUNCIONES
def ventana_empleado():
        #FUNCIONES GLOBALES PARA QUE FUNCIONE EL PROCEDIMIENTO 
        global tvControlEmplea
        global ventanaEmpleado

        #SUBFUNCIONES
        def buscarEmpleado():
            id_empleado = txtIDEmplea.get()
            try:
                query = "SELECT * FROM empleados WHERE id_empleado = %s"
        
                c.execute(query, (id_empleado,))
        
                datos = c.fetchall()

                for item in tvControlEmplea.get_children():
                        tvControlEmplea.delete(item)

                for reg in datos:
                        tvControlEmplea.insert("", "end", text=reg[0], values=(reg[1], reg[2], reg[3], reg[4], reg[5], reg[6]))

            except Exception as ex:
                messagebox.showerror(message=ex)
    
    
        #UNA TABLA DE "VENTANA EMPLEADO"
        tvControlEmplea = ttk.Treeview(ventanaEmpleado, columns=("col1", "col2", "col3", "col4", "col5", "col6"))

        #VENTANA EMPLEADO
        ventanaEmpleado=Toplevel(ventana)
        ventanaEmpleado.title("Empleados")
        ventanaEmpleado.geometry("860x320")
        ventanaEmpleado.configure(bg="#FF0000")

        #TEXTO
        Label(ventanaEmpleado, text="ᴄᴏɴᴛʀᴏʟ ᴅᴇ ᴇᴍᴘʟᴇᴀᴅᴏꜱ", bg="#FF0000",fg="#FFF", font=("Arial", 15, "bold")).place(x=440,y=15)

        #TEXTO
        Label(ventanaEmpleado,fg="#FFF", text="ID Empleado:", bg="#FF0000").place(x=35, y=50)
        Label(ventanaEmpleado,fg="#FFF", text="👤", bg="#FF0000",font=(10)).place(x=9, y=47)
        #CAJA
        txtIDEmplea= Entry(ventanaEmpleado, width=18)
        txtIDEmplea.place(x=10, y=70)

        #DISEÑO  DE LA HORA
        lblFechaHora = Label(ventanaEmpleado, text="", bg="#FF0000",fg="#FFF", font=("Arial", 9,"bold"))
        lblFechaHora.place(x=720, y=15) 

        #INICALIZACION DE VARIABLE 
        actualizar_fecha_hora(lblFechaHora)


        #BOTOPNES DE "VENTANA EMPLEADO "
        Button(ventanaEmpleado, text="Buscar", width=12,fg="#FFF", bg="#66150D", bd=4, command=buscarEmpleado).place(x=130, y=62)
        Button(ventanaEmpleado, text="Crear Empleado", width=30,fg="#FFF", bg="#66150D", bd=4, command=crear).place(x=10, y=135) #AQUI AGREGAR EL COMANDO DE VENTANA PARA CREAR
        Button(ventanaEmpleado, text="Actualizar Empleado",fg="#FFF",width=30, bg="#66150D", bd=4, command=crear).place(x=10, y=180)
        Button(ventanaEmpleado, text="Eliminar Empleado", width=30,fg="#FFF", bg="#66150D", bd=4, command=crear).place(x=10, y=225)

        #TABLA DE "VENTANA EMPLEADO"
        tvControlEmplea= ttk.Treeview(ventanaEmpleado, columns=("col1", "col2", "col3", "col4", "col5", "col6"))
        tvControlEmplea.column("#0",width=70)
        tvControlEmplea.column("col1",width=75)
        tvControlEmplea.column("col2",width=80)
        tvControlEmplea.column("col3",width=80)
        tvControlEmplea.column("col4",width=90)
        tvControlEmplea.column("col5",width=90)
        tvControlEmplea.column("col6",width=100)

        tvControlEmplea.heading("#0", text="ID")
        tvControlEmplea.heading("col1", text="NOMBRE")
        tvControlEmplea.heading("col2", text="TELEFONO")
        tvControlEmplea.heading("col3", text="DOMICILIO")
        tvControlEmplea.heading("col4", text="DNI")
        tvControlEmplea.heading("col5", text="CONTRASEÑA")
        tvControlEmplea.heading("col6", text="DESIGNACION")
        tvControlEmplea.place(x=255, y=65)
        
        #INICALIZACION DE FUNCION
        return tvControlEmplea
    

#FUNCIONES
def Salir():
    ventana.destroy()

#FUNCIONES
def menu():
    #FUNCIONES GLOBALES PARA QUE FUNCIONE EL PROCEDIMIENTO 
    global ventanaEmpleado
    global tvControlEmpleado
    #INICA UNA VENTA " MENU "
    ventanaMenu=Toplevel(ventana)
    ventanaMenu.title("Menú")
    ventanaMenu.geometry("500x330")
    ventanaMenu.resizable(0,0)
    #COLOR DE FONDO
    ventanaMenu.configure(bg="#FF0000")
    #TEXTO
    Label(ventanaMenu, text="ᴇꜱᴄᴏɢᴇ ᴜɴᴀ ᴏᴘᴄɪᴏɴ",fg="#FFF" ,bg="#FF0000", font=("Algerian", 20, "bold")).place(x=125, y=40)
    
    #DISEÑO "VENTANA MENU"
    marco = Frame(ventanaMenu, bd=1, relief="solid")
    marco.place(x=60, y=140, width=190, height=150)
    
    marco = Frame(ventanaMenu, bd=1, relief="solid")
    marco.place(x=260, y=140, width=190, height=150)
    
    #TEXTO DE VENTANA MENU
    Label(ventanaMenu, text="👤💼 Empleados", font=("bold",15)).place(x=80, y=160)
    Label(ventanaMenu, text="📝💸 Facturas:", font=("bold",15)).place(x=280, y=160)
   
    
    #BOTONES DE VENTANA MENU
    Button(ventanaMenu, text="Entrar",fg="#FFF",font=("bold",10), width=10, bg="#FF0000", bd=13, command=ventana_empleado).place(x=100, y=215)
    Button(ventanaMenu, text="Entrar",fg="#FFF",font=("bold",10), width=10, bg="#FF0000", bd=13, command=ventana_factura).place(x=300, y=215)
    
    #"MENUS DEPLEGABLES DE ARRIBA DE LA VENTANA "
    barra_menu= Menu()
    ventanaMenu.config(menu=barra_menu)


    opciones_menu= Menu(barra_menu)
    opciones_menu.add_command(label="Salir",command=Salir)
    barra_menu.add_cascade(label="Archivo", menu=opciones_menu)

    opciones_menu2= Menu(barra_menu)
    opciones_menu2.add_command(label="Empleados", command=ventana_empleado)
    opciones_menu2.add_command(label="Factura", command=ventana_factura)
    barra_menu.add_cascade(label="Módulos", menu=opciones_menu2)


#FUNCION
def verificar_credenciales():
    # Obtener los valores de usuario y contraseña
    username = txtUsuario.get()
    password = txtContraseña.get()

    # Verificar las credenciales
    if username == "usuario" and password == "contraseña":
        messagebox.showinfo("Inicio de Sesión Exitoso", "Bienvenido, {}.".format(username))
    else:
        messagebox.showerror("Inicio de Sesión Fallido", "Credenciales incorrectas. Por favor, inténtalo de nuevo.")


#VENTANA PRINCIPAL
ventana=Tk()
ventana.title("Login")
ventana.geometry("240x290")
ventana.resizable(0,0)
#TEXTO 
Label(ventana, text="ᴀᴄᴄᴇꜱᴏ",fg="#FFF", bg="#FF0000", font=("Arial", 14, "bold")).place(x=85,y=20)
ventana.configure(bg="#FF0000")

##imagen_usuario =PhotoImage(file="usuario.png")
##imagen_contraseña =PhotoImage(file="contraseña.png")

Label(ventana,  bg="#FF0000").place(x=5, y=60)

txtUsuario= Entry(ventana, width=35)
txtUsuario.place(x=10, y=90)

Label(ventana, bg="#FF0000").place(x=5, y=140)
txtContraseña= Entry(ventana, width=35)
txtContraseña.place(x=10, y=170)

Label(ventana, text="Usuario:",fg="#FFF", bg="#FF0000", font=("bold",11)).place(x=40, y=65)
Label(ventana, text="Contraseña:",fg="#FFF", bg="#FF0000", font=("bold",11)).place(x=35, y=140)
#BOTONES
Button(ventana, text="Iniciar Sesión", width=12,fg="#FFF", bg="#FF0000", bd=4, command=verificar_credenciales).place(x=70, y=200)
Button(ventana, text="Continuar", width=12,fg="#FFF", bg="#FF0000", bd=4, command=menu).place(x=70, y=240)


#FUNCION DE CONSOLE
print(sys.getrecursionlimit())
sys.setrecursionlimit(2000)

#MY SQL
try:
    j=pymysql.connect(host="localhost", user="root", password="")
    c=j.cursor()
except Exception as ex:
    messagebox.showerror(message=ex)
    ventana.destroy()

#TERMINAL DE LA VENTANA 
ventana.mainloop()