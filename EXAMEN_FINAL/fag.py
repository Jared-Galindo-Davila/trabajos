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
            xD.commit()
            messagebox.showinfo(message="Factura Eliminada Satisfactoriamente.")
            ListadoFactura()
        except Exception as ex:
            messagebox.showerror(message=ex)

    def nuevoFactura():
        #ELIMINAR EL TEXTO
        txtFactura.delete(0, "end")
        txtNombre_Cliente.delete(0, "end")
        txtTelefono_Factura.delete(0, "end")
        combo1.set("")
        combo2.set("")
        combo3.set("")
        txtCantidad.delete(0, "end")
        combo4.set("")
        txtFactura.focus()
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
            nombre_cliente = txtNombre_Cliente.get()
            telefono_cliente = txtTelefono_Factura.get()
            categoria = combo1.get()
            sub_categoria = combo2.get()  
            articulo = combo3.get()  
            cantidad = txtCantidad.get()
            precio = combo4.get()  

            if not id_factura or not nombre_cliente or not telefono_cliente or not categoria or not sub_categoria or not articulo or not cantidad or not precio:
                messagebox.showwarning(message="Por favor, complete todos los campos.")
                return
            c.execute(query, (id_factura, nombre_cliente, telefono_cliente, categoria, sub_categoria, articulo, cantidad, precio))
            xD.commit()
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
            for item in tvControlFactura.get_children():
                tvControlFactura.delete(item)

        # Insertar los resultados en el Treeview
            for reg in datos:
                tvControlFactura.insert("", "end", text=reg[0], values=(reg[1], reg[2], reg[3], reg[4], reg[5], reg[6], reg[7]))

        except Exception as ex:
            messagebox.showerror(message=ex)
            


    # VENTANA FACTURA 
    ventanaFactura=Toplevel(ventana)
    ventanaFactura.title("Factura")
    ventanaFactura.geometry("900x500")

    #TITULO
    Label(ventanaFactura, text="FACTURACION", bg="cyan", font=("Algerian", 20, "bold")).pack()


    #DECORACIÓN DE MARCOS DE FONDOS
    marco = Frame(ventanaFactura, bd=1, relief="solid")
    marco.place(x=10, y=40, width=880, height=40)
    
    marco = Frame(ventanaFactura, bd=1, relief="solid")
    marco.place(x=10, y=400, width=400, height=90)
    
    marco = Frame(ventanaFactura, bd=1, relief="solid")
    marco.place(x=10, y=100, width=400, height=290)
    
    marco = Frame(ventanaFactura, bd=1, relief="solid")
    marco.place(x=420, y=100, width=470, height=390)
    
    marco = Frame(ventanaFactura, bg="lemon chiffon", bd=1, relief="solid")
    marco.place(x=530, y=110, width=245, height=90)
    
    #UN PEQUEÑO TEXTO 
    label_encima_marco = Label(ventanaFactura, text="Informacion de Cliente", bg="yellow", font=("Arial", 12, "bold"))
    label_encima_marco.place(x=10, y=15)
    
    #TEXTO
    Label(ventanaFactura, text="Factura No.").place(x=20, y=50)
    #CAJA 
    txtFactura= Entry(ventanaFactura, width=20)
    txtFactura.place(x=90, y=50)
    
    #TEXTO
    Label(ventanaFactura, text="Nombre del Cliente:").place(x=290, y=50)
    #CAJA
    txtNombre_Cliente= Entry(ventanaFactura, width=30)
    txtNombre_Cliente.place(x=400, y=50)
    
    #TEXTO
    Label(ventanaFactura, text="Telefono:").place(x=600, y=50)
    #CAJA
    txtTelefono_Factura= Entry(ventanaFactura, width=35)
    txtTelefono_Factura.place(x=660, y=50)
    
    #TEXTO
    Label(ventanaFactura, text="Cantidad:").place(x=20, y=265)
    #CAJA
    txtCantidad = Entry(ventanaFactura, width=63)
    txtCantidad.place(x=20, y=285)

    #serias los textos de la VENTANA FACTURACION
    Label(ventanaFactura, text="Articulos:",font="bold").place(x=30, y=85)
    Label(ventanaFactura, text="Vista Factura:",font="bold").place(x=450, y=85)
    Label(ventanaFactura, text="Super 'El Porvenir'",bg="lemon chiffon", font="bold").place(x=580, y=120)
    Label(ventanaFactura, text="RFC: 5A24X541C35'",bg="lemon chiffon").place(x=590, y=140)
    Label(ventanaFactura, text="Plaza Central no. 64,C.P.4720 Tel. 952532115",bg="lemon chiffon").place(x=535, y=155)
    Label(ventanaFactura, text="NuevaPeruYork City",bg="lemon chiffon").place(x=590, y=170)


    #LOS BOTONES DE  LA VENTANA " FACTURACION "
    Button(ventanaFactura, text="Total", bg="Orange", width=10, command=total).place(x=50, y=430)
    Button(ventanaFactura, text="Generar", bg="Orange", width=10, command=registrarFactura).place(x=130, y=430)
    Button(ventanaFactura, text="Limpiar", bg="Orange", width=10, command=nuevoFactura).place(x=210, y=430)
    Button(ventanaFactura, text="Salir", bg="Orange", width=10, command=Salir).place(x=290, y=430)
    
    Button(ventanaFactura, text="Buscar", bg="Orange",command=buscar).place(x=220, y=45)
    
    Button(ventanaFactura, text="Eliminar", bg="Orange", width=10, command=eliminarFactura).place(x=130, y=355)
    Button(ventanaFactura, text="Limpiar", bg="Orange", width=10, command=nuevoFactura).place(x=210, y=355)
    

    #DECORACION  VENTANA FACTURA 
    lblFechaHora = Label(ventanaFactura, text="", font=("Arial", 12))
    lblFechaHora.place(x=700, y=0)
    
    #INICA LA FECHA Y HORA
    actualizar_fecha_hora(lblFechaHora)
    
    #TEXTO
    Label(ventanaFactura, text="Seleccionar Categoria").place(x=20, y=130)
    #CAJA
    combo1 = ttk.Combobox(ventanaFactura, state="readonly", width=60 ,values=["Juguetes", "Electrodomesticos", "Alimentos"])
    combo1.place(x=20, y=150)
    
    #TEXTO
    Label(ventanaFactura, text="Sub-Categoria:").place(x=20, y=175)
    #CAJA
    combo2 = ttk.Combobox(ventanaFactura, state="readonly", width=60 ,values=["Armables", "No Destruibles", "Destruibles"])
    combo2.place(x=20, y=195)
    
    #TEXTO
    Label(ventanaFactura, text="Artículo:").place(x=20, y=220)
    #CAJA
    combo3 = ttk.Combobox(ventanaFactura, state="readonly", width=60 ,values=["Lego", "Plastilina"])
    combo3.place(x=20, y=240)
    
    #TEXTI
    Label(ventanaFactura, text="Precio:").place(x=20, y=305)
    #CAJA
    combo4 = ttk.Combobox(ventanaFactura, state="readonly", width=60 ,values=["120 Soles", "150 Soles"])
    combo4.place(x=20, y=325)
    
    #TEXTO DE "VENTANA  FACTURA "
    Label(ventanaFactura, text="Cliente:").place(x=450, y=220)
    Label(ventanaFactura, text="Factura No.").place(x=450, y=240)
    Label(ventanaFactura, text="Telefono:").place(x=720, y=220)
    Label(ventanaFactura, text="Fecha:").place(x=730, y=240)
    
    #COLUMNAS DE LA TABLA "VENTANA FACTURA "
    tvControlFactura= ttk.Treeview(ventanaFactura, columns=("col1", "col2", "col3", "col4", "col5", "col6", "col7"), height=8)
    tvControlFactura.column("#0",width=70)
    tvControlFactura.column("col1",width=50)
    tvControlFactura.column("col2",width=60)
    tvControlFactura.column("col3",width=60)
    tvControlFactura.column("col4",width=60)
    tvControlFactura.column("col5",width=60)
    tvControlFactura.column("col6",width=50)
    tvControlFactura.column("col7",width=50)

    tvControlFactura.heading("#0", text="N. FACTURA")
    tvControlFactura.heading("col1", text="NOMBRE")
    tvControlFactura.heading("col2", text="TELEFONO")
    tvControlFactura.heading("col3", text="CATEGORIA")
    tvControlFactura.heading("col4", text="SUB CATEGORIA")
    tvControlFactura.heading("col5", text="ARTICULO")
    tvControlFactura.heading("col6", text="CANTIDAD")
    tvControlFactura.heading("col7", text="PRECIO")
    tvControlFactura.place(x=423, y=290)
    
    lblTotalArticulos= Label(ventanaFactura, text="Total Articulos: 0")
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
            xD.commit()
            messagebox.showinfo(message="Empleados Eliminados Satisfactoriamente.")
            Listado()
        except Exception as ex:
            messagebox.showerror(message=ex)

    #SUBFUNCION

    def nuevo():
        #ELIMINAR TEXTO ESCRITO
        txtIDEmpleado.delete(0, "end")
        txtNombre.delete(0, "end")
        txtTelefono.delete(0, "end")
        txtDomicilio.delete(0, "end")
        txtDni.delete(0, "end")
        txtContraseña.delete(0, "end")
        txtDesignacion.delete(0, "end")
        txtIDEmpleado.focus()


    #SUBFUNCION
    def modificar():
        #MY SQL
        try:
            query="update empleados set nombre= %s, telefono= %s , domicilio= %s, dni=%s, contraseña=%s, designacion=%s where id_empleado= %s"
            id_empleado= txtIDEmpleado.get()
            nombre= txtNombre.get()
            telefono=txtTelefono.get()
            domicilio= txtDomicilio.get()
            dni= txtDni.get()
            contraseña= txtContraseña.get()
            designacion= txtDesignacion.get()
            c.execute(query,(nombre, telefono, domicilio, dni, contraseña, designacion, id_empleado))
            xD.commit()
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
            telefono= txtTelefono.get()
            domicilio= txtDomicilio.get()
            dni= txtDni.get()
            contraseña= txtContraseña.get()
            designacion= txtDesignacion.get()
            c.execute(query,(id_empleado, nombre, telefono, domicilio, dni, contraseña, designacion))
            xD.commit()
            messagebox.showinfo(message="El Empleado {} Registrado Satisfactoriamente.".format(nombre))
            Listado()
        except Exception as ex:
            messagebox.showerror(message=ex)


    #VENTANA DE "CREAR"        
    ventana_crear = Toplevel(ventana, bg="gray25")
    ventana_crear.title("Ventana Crear Empleados")
    Label(ventana_crear, text="Mantenimiento De Empleados",fg="snow", bg="gray25", font=("Algerian", 16, "bold")).pack()
    ventana_crear.geometry("900x500")
    
    #DISEÑO
    lblFechaHora = Label(ventana_crear, text="", fg="snow", bg="gray25", font=("Arial", 12))
    lblFechaHora.place(x=675, y=5)

    #INICALIZACION DE "FECHA Y HORA "
    actualizar_fecha_hora(lblFechaHora)
    
    # TEXTO
    Label(ventana_crear, text="ID Empleado: ", fg="snow", bg="gray25").place(x=10, y=49)
    #CAJA 
    txtIDEmpleado= Entry(ventana_crear, width=30)
    txtIDEmpleado.place(x=10, y=70)

    #TEXTO
    Label(ventana_crear, text="Nombre: ", fg="snow", bg="gray25").place(x=10, y=89)
    #CAJA
    txtNombre= Entry(ventana_crear, width=30)
    txtNombre.place(x=10, y=110)

    #TEXTO
    Label(ventana_crear, text="Telefono: ", fg="snow", bg="gray25").place(x=10, y=129)
    #CAJA
    txtTelefono= Entry(ventana_crear, width=30)
    txtTelefono.place(x=10, y=150)

    #TEXTO 
    Label(ventana_crear, text="Domicilio: ", fg="snow", bg="gray25").place(x=10, y=169)
    #CAJA 
    txtDomicilio= Entry(ventana_crear, width=30)
    txtDomicilio.place(x=10, y=190)
    
    #TEXTO
    Label(ventana_crear, text="DNI: ", fg="snow", bg="gray25").place(x=10, y=215)
    #CAJA
    txtDni= Entry(ventana_crear, width=30)
    txtDni.place(x=10, y=235)

    #TEXTO
    Label(ventana_crear, text="Contraseña: ", fg="snow", bg="gray25").place(x=10, y=255)
    #CAJA
    txtContraseña= Entry(ventana_crear, width=30)
    txtContraseña.place(x=10, y=280)
    
    #TEXTO
    Label(ventana_crear, text="Designacion: ", fg="snow", bg="gray25").place(x=10, y=305)
    #CAJA
    txtDesignacion= Entry(ventana_crear, width=30)
    txtDesignacion.place(x=10, y=330)

    #BOTONES DE "CENTANA CREAR"
    Button(ventana_crear, text="Registrar",bg="Yellow", width=12, command=registrar).place(x=10, y=380)
    Button(ventana_crear, text="Modificar",bg="Yellow", width=12, command=modificar).place(x=103, y=380)
    Button(ventana_crear, text="Eliminar",bg="Yellow", width=12, command=eliminar).place(x=193, y=380)
    Button(ventana_crear, text="Nuevo",bg="Yellow", width=12,command=nuevo).place(x=283, y=380)
    

    #COLUMNAS DE LA TABLA " VENTANA CREAR"
    tvControlCrear= ttk.Treeview(ventana_crear, columns=("col1", "col2", "col3", "col4", "col5", "col6"))
    tvControlCrear.column("#0",width=120)
    tvControlCrear.column("col1",width=100)
    tvControlCrear.column("col2",width=80)
    tvControlCrear.column("col3",width=80)
    tvControlCrear.column("col4",width=90)
    tvControlCrear.column("col5",width=90)
    tvControlCrear.column("col6",width=100)

    tvControlCrear.heading("#0", text="ID EMPLADO")
    tvControlCrear.heading("col1", text="NOMBRE")
    tvControlCrear.heading("col2", text="TELEFONO")
    tvControlCrear.heading("col3", text="DOMICILIO")
    tvControlCrear.heading("col4", text="DNI")
    tvControlCrear.heading("col5", text="CONTRASEÑA")
    tvControlCrear.heading("col6", text="DESIGNACION")
    tvControlCrear.place(x=210, y=50)

    lblTotalEmpleados = Label(ventana_crear, text="Total Empleados: 0", fg="snow", bg="gray25")
    lblTotalEmpleados.place(x=680, y=380)
    
    #FUNCIONES GLOBALES PARA QUE FUNCIONE EL PROCEDIMIENTO 
    global tvControlEmpleado
    global ventana_empleado


#FUNCIONES
def ventana_empleado():
        #FUNCIONES GLOBALES PARA QUE FUNCIONE EL PROCEDIMIENTO 
        global tvControlEmpleado
        global ventanaEmpleado

        #SUBFUNCIONES
        def buscarEmpleado():
            id_empleado = txtIDEmpleado.get()
            try:
                query = "SELECT * FROM empleados WHERE id_empleado = %s"
        
                c.execute(query, (id_empleado,))
        
                datos = c.fetchall()

                for item in tvControlEmpleado.get_children():
                        tvControlEmpleado.delete(item)

                for reg in datos:
                        tvControlEmpleado.insert("", "end", text=reg[0], values=(reg[1], reg[2], reg[3], reg[4], reg[5], reg[6]))

            except Exception as ex:
                messagebox.showerror(message=ex)
    
    
        #UNA TABLA DE "VENTANA EMPLEADO"
        tvControlEmpleado = ttk.Treeview(ventanaEmpleado, columns=("col1", "col2", "col3", "col4", "col5", "col6"))

        #VENTANA EMPLEADO
        ventanaEmpleado=Toplevel(ventana)
        ventanaEmpleado.title("Empleados")
        ventanaEmpleado.geometry("860x400")
        ventanaEmpleado.configure(bg="SkyBlue1")

        #TEXTO
        Label(ventanaEmpleado, text="Control De Empleados", bg="SkyBlue1", font=("Arial", 15, "bold")).pack()

        #TEXTO
        Label(ventanaEmpleado, text="Id Empleado: ", bg="SkyBlue1").place(x=13, y=50)
        #CAJA
        txtIDEmpleado= Entry(ventanaEmpleado, width=18)
        txtIDEmpleado.place(x=10, y=70)

        #DISEÑO 
        lblFechaHora = Label(ventanaEmpleado, text="", bg="SkyBlue1", font=("Arial", 12))
        lblFechaHora.place(x=640, y=10) 

        #INICALIZACION DE VARIABLE 
        actualizar_fecha_hora(lblFechaHora)


        #BOTOPNES DE "VENTANA EMPLEADO "
        Button(ventanaEmpleado, text="Buscar", width=12, bg="Orange", bd=4, command=buscarEmpleado).place(x=130, y=62)
        Button(ventanaEmpleado, text="Crear Empleado", width=30, bg="Orange", bd=4, command=crear).place(x=10, y=135) #AQUI AGREGAR EL COMANDO DE VENTANA PARA CREAR
        Button(ventanaEmpleado, text="Actualizar Empleado", width=30, bg="Orange", bd=4, command=crear).place(x=10, y=180)
        Button(ventanaEmpleado, text="Eliminar Empleado", width=30, bg="Orange", bd=4, command=crear).place(x=10, y=225)

        #TABLA DE "VENTANA EMPLEADO"
        tvControlEmpleado= ttk.Treeview(ventanaEmpleado, columns=("col1", "col2", "col3", "col4", "col5", "col6"))
        tvControlEmpleado.column("#0",width=70)
        tvControlEmpleado.column("col1",width=75)
        tvControlEmpleado.column("col2",width=80)
        tvControlEmpleado.column("col3",width=80)
        tvControlEmpleado.column("col4",width=90)
        tvControlEmpleado.column("col5",width=90)
        tvControlEmpleado.column("col6",width=100)

        tvControlEmpleado.heading("#0", text="ID")
        tvControlEmpleado.heading("col1", text="NOMBRE")
        tvControlEmpleado.heading("col2", text="TELEFONO")
        tvControlEmpleado.heading("col3", text="DOMICILIO")
        tvControlEmpleado.heading("col4", text="DNI")
        tvControlEmpleado.heading("col5", text="CONTRASEÑA")
        tvControlEmpleado.heading("col6", text="DESIGNACION")
        tvControlEmpleado.place(x=255, y=65)
        
        #INICALIZACION DE FUNCION
        return tvControlEmpleado
    

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
    ventanaMenu.geometry("500x400")
    #COLOR DE FONDO
    ventanaMenu.configure(bg="cyan")
    #TEXTO
    Label(ventanaMenu, text="ESCOGE UN OPCIÓN", bg="cyan", font=("Algerian", 20, "bold")).place(x=125, y=40)
    
    #DISEÑO "VENTANA MENU"
    marco = Frame(ventanaMenu, bd=1, relief="solid")
    marco.place(x=60, y=140, width=190, height=150)
    
    marco = Frame(ventanaMenu, bd=1, relief="solid")
    marco.place(x=260, y=140, width=190, height=150)
    
    #TEXTO DE VENTANA MENU
    Label(ventanaMenu, text="Presione Aquí Para:", font="bold").place(x=70, y=160)
    Label(ventanaMenu, text="Presione Aquí Para:", font="bold").place(x=270, y=160)
    
    
    #BOTONES DE VENTANA MENU
    Button(ventanaMenu, text="Empleados", width=10, bg="Orange", bd=15, command=ventana_empleado).place(x=100, y=200)
    Button(ventanaMenu, text="Facturas", width=10, bg="Orange", bd=15, command=ventana_factura).place(x=300, y=200)
    
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
ventana.geometry("300x300")
#TEXTO 
Label(ventana, text="Acceso", bg="aquamarine", font=("Arial", 15, "bold")).pack()
ventana.configure(bg="aquamarine")

imagen_usuario = tk.PhotoImage("usuario.png")
imagen_contraseña = tk.PhotoImage("contraseña.png")

Label(ventana, image=imagen_usuario, bg="aquamarine").place(x=20, y=40)

txtUsuario= Entry(ventana, width=35)
txtUsuario.place(x=40, y=70)

Label(ventana, image=imagen_contraseña, bg="aquamarine").place(x=20, y=100)
txtContraseña= Entry(ventana, width=35)
txtContraseña.place(x=40, y=130)

Label(ventana, text="Usuarios:", bg="aquamarine", font="bold").place(x=50, y=40)

Label(ventana, text="Contraseñas:", bg="aquamarine", font="bold").place(x=50, y=100)
#BOTONES
Button(ventana, text="Verificar Usuario", width=12, bg="Orange", bd=4, command=verificar_credenciales).place(x=100, y=150)
Button(ventana, text="Continuar", width=12, bg="Orange", bd=4, command=menu).place(x=100, y=200)
#TEXTO 
Label(ventana, text="Primero Accione el boton Verificar Usuario", bg="aquamarine").place(x=30, y=240)
Label(ventana, text="Luego Accione el boton Continuar", bg="aquamarine").place(x=50, y=260)

#FUNCION DE CONSOLE
print(sys.getrecursionlimit())
sys.setrecursionlimit(2000)

#MY SQL
try:
    xD=pymysql.connect(host="localhost", user="root", password="", db="Finali")
    c=xD.cursor()
except Exception as ex:
    messagebox.showerror(message=ex)
    

#TERMINAL DE LA VENTANA 
ventana.mainloop()