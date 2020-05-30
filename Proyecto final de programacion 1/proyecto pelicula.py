#Nombre: Bonifacio Ceferino Patal Gómez
#No. de carnet: 1990-19-8121
#Nombre: Axel Marcos Humberto Olcot Patal
#No. de carnet: 1990-19-6785
#Lugar y fecha: Patzun, 06/05/2020
#consiste en registrar por medio de ARCHIVOS,  “Las ventas de Peliculas y de contenido de Video”, usando un sistema de inventario donde podremos Agregar, Modificar
# Buscar, Mostrar y Eliminar Datos, dependiendo lo que necesite el Usario.

import os

opcionMenu = 0


def numeros(costoFabrica,precioVenta, unidades, ganancia):

    validar = bool()
    validar = False
    if costoFabrica < 0:
        validar = True    
    if precioVenta < 0:         #Esta funcion esta encargada de validar que nos nuemeros ingresados, en los datos, de los costos de lo
        validar = True          #productos no sean menores a 0.
    if unidades < 0:
        validar = True
    if ganancia< 0:
        validar = True
    return validar 


def existencias(producto, numero):
    contador = 0
    archivoBusqueda = open("Registro.txt", "r") 
    palabraProducto = producto + "\n"
    for producto in archivoBusqueda:
        contador = contador + 1             #En esta funcion se encarga de verificar/validar, la existencia del producto ingresado
        if producto == palabraProducto:     #para que al momento de estar ingresando productos no hayan repetidos.
            numero = contador 
    archivoBusqueda.close() 
    return numero - 1 

def unidad(numero):
    archivoDatos = open("Registro.txt", "r")
    listado = archivoDatos.readlines()
    print(listado)
    print(listado[numero])      #En esta funcion nos mustra la unidad que se busca con el numero en la lista
    os.system("pause")
    archivoDatos.close()
    return listado[numero + 6]


def agregarunidad(numero, nuevaCantidad):
    listadocompelto = {}
    archivo = open("Registro.txt", "r")  #En esta funcion la utilizamos para que al momento de que intentemos ingresar un producto y este
    listado = archivo.readlines()        #ya este en nuestro inventario nos, pida las nuevas unidades, que debamos sumar a las ya existentes.
    operacion = int(listado[numero + 6]) + nuevaCantidad 
    operacionGanacia = float((float(listado[numero + 4]) - float(listado[numero + 2])) * operacion) 
    listado[numero + 6] = str(operacion) + "\n" 
    listado[numero + 8] = str(operacionGanacia) + "\n" #De igual manera que al momento de aumentar las unidades, las ganancias aumentaran
    listadocompelto = listado 
    archivo.close()

    archivo2 = open("Registro.txt", "w") 
    for x in listadocompelto:           #Aquí volvemos abrir el archivo para que podamos cambiar los resultados del listado del producto
        archivo2.write(x)
    archivo2.close() 


def actualizardato(numero, nombredato, valorfabrica, valorcosto, valorunidad, valorganancia):
    listadocompelto = {}
    archivo = open("Registro.txt", "r")
    listado = archivo.readlines()

    listado[numero] = nombredato +  "\n"
    listado[numero + 2] = str(valorfabrica) + "\n"
    listado[numero + 4] = str(valorcosto) + "\n"
    listado[numero + 6] = str(valorunidad) + "\n"       #Esta funcion la utilizamos para poder actualizar los datos ingresados en la lista del
    listado[numero + 8] = str(valorganancia) + "\n"     #producto que deseemos en el momento.
    listadocompelto = listado

    archivo.close()

    archivo2 = open("Registro.txt", "w")
    for x in listadocompelto:
        archivo2.write(x)
    archivo2.close()


def eliminardato(numero):
    listadocompelto = {}
    archivo = open("Registro.txt", "r")
    listado = archivo.readlines()

    print("\nDatos Eliminados...")
    print(listado[numero - 1], end="")
    print(listado[numero], end="")
    print(listado[numero + 1], end="")
    print(listado[numero + 2], end="")
    print(listado[numero + 3], end="")      #En esta funcion es donde nosotros eliminamos el producto incluido todos los datos de este, 
    print(listado[numero + 4], end="")      #al momento de selecionar/escribir su nombre respectivo
    print(listado[numero + 5], end="")
    print(listado[numero + 6], end="")
    print(listado[numero + 7], end="")
    print(listado[numero + 8], end="")
    print(listado[numero + 9], end="")
    for x in range(11):
        listado.pop(int(numero) - 1)

    listadocompelto = listado
    archivo.close()
    archivo2 = open("Registro.txt", "w")
    for x in listadocompelto:
        archivo2.write(x)
    archivo2.close()



def ingreso():
    os.system("cls")

    numeroProducto = 0
    print("Ingreso de productos\n")
    print("Nombre del producto: ", end ="") #En esta funcion es donde pedimos los datos que hemos de ingresar, como los costos y ventas Etc.
    nombreProducto = input()                           #donde para esto hacemos uso de las funciones anteriormente mencionadas, para que nos ayuden
                                                       #proceso de ingreso de los mismos.
    numeroProducto = existencias(nombreProducto, numeroProducto)

    if  numeroProducto > 0:

        
        print("El producto ya esta registrado\nIngrese las unidades")
        print("Unidades", unidad(numeroProducto), end="")
        unidades = int(input("Ingrese las nuevas unidades: "))

        while numeros(0,0, unidades, 0) != False:
            print("\nLos datos no pueden ser menores a 0")
            print("Ingrese los datos\n")
            print("Las unidades son: ", unidad(numeroProducto), end="")
            unidades = int(input("Ingrese las unidades del producto: "))
        agregarunidad(numeroProducto, unidades)

    else:
        costoFabrica = float(input("Ingrese el costo del producto: "))
        precioVenta = float(input("Ingrese el precio de venta del producto: "))
        unidades = int(input("Ingrese las unidades del producto: "))
        ganancia = (precioVenta-costoFabrica) * unidades
        while numeros(costoFabrica,precioVenta, unidades, ganancia) != False:
            print("\nLos datos no pueden ser menores a 0\n  El precio de costo de fabrica debe de ser menor al precio de venta del producto")
            print("Ingrese los datos nuevamente\n")
            costoFabrica = float(input("Ingrese el costo del producto: "))
            precioVenta = float(input("Ingrese el precio de venta del producto: "))
            unidades = int(input("Ingrese las unidades del producto: "))
            ganancia = (precioVenta-costoFabrica) * unidades
        archivoNuevo = open("Registro.txt", "a")
        archivoNuevo.write("Nombre del producto:\n")
        archivoNuevo.write(nombreProducto  + "\n")
        archivoNuevo.write("Costo de fabrica:\n")
        archivoNuevo.write(str(costoFabrica) + "\n")
        archivoNuevo.write("Precio de venta:\n")
        archivoNuevo.write(str(precioVenta) + "\n")
        archivoNuevo.write("Unidades:\n")
        archivoNuevo.write(str(unidades) + "\n")
        archivoNuevo.write("Ganancias:\n")
        archivoNuevo.write(str(ganancia) + "\n")
        archivoNuevo.write('****************************\n')
        archivoNuevo.close()

    
    os.system("pause")
    os.system("cls")

def mostrar():
    os.system("cls")
    archivoProducto = open("Registro.txt", "r")
    for listado in archivoProducto:
        print(listado, end = "")        #En esta funcion nos ayuda a mostrar los datos de los productos que hemos ingresado anteriormente
    archivoProducto.close               
    os.system("pause")
    os.system("cls")


def añado():
    os.system("cls")
    numeroProducto = 0
    print("Añadir unidades.\n")   #Aquí es donde cambiamos las unidades de un producto a nuestra eleccion, donde sumamos las unidades
    print("************************\n")  #las unides ingresadas anteriormente y las nuevas, y calculamos la nueva ganancia de la misma.
    print("Ingrese el nombre del producto: ", end ="")  #donde de igual manera llamanos a las funciones anteriores para hacer las respectivas operaciones
    nombreProducto = input()
    numeroProducto = existencias(nombreProducto, numeroProducto)
    if  numeroProducto > 0:
        print("Las unidades: ", unidad(numeroProducto), end="")
        unidades = int(input("Ingrese las unidades del producto: "))
        while numeros(0,0, unidades, 0) != False:
            print("\nLos datos no pueden ser menores a 0")
            print("Ingrese de nuevo los datos\n")
            print("Las unidaes", unidad(numeroProducto), end="")
            unidades = int(input("Ingrese las unidades del producto "))
        agregarunidad(numeroProducto, unidades)
        print("\nLas unidades se agregaron '" , unidades, "'al producto existente.")
    else:
        print(" El producto que ha ingresado no existe.\n ")
    
    os.system("pause")
    os.system("cls")


def actualizo():
    os.system("cls")
    numeroProducto = 0
    print("Actualizar datos del producto\n")  #En esta funcion es donde podemos llegar a actualizar los datos de un producto ya existente,
    print("Ingrese el nombre del producto que desea actualizar: ", end ="") #en nuestro inventario, donde de igual manera hacemos uso de las funciones anteriores.
    nombreProducto = input()
    numeroProducto = existencias(nombreProducto, numeroProducto)
    if  numeroProducto > 0:
        print("******************************\n")
        nProducto = input("Ingrese el nuevo nombre del producto: ")
        nfabrica = float(input("Ingrese el el costo del producto: "))
        nventa = float(input("Ingrese el precio de venta del producto: "))
        nCantidad = int(input("Ingrese las unidades del producto: "))
        nganancia = (nventa-nfabrica) * nCantidad
        while numeros(nfabrica,nventa, nCantidad, nganancia) != False:
            print("Los datos no puden ser menores a 0")
            print("Ingrese los datos: \n")
            nProducto = input("Ingrese el nuevo nombre del producto ")
            nfabrica = float(input("Ingrese el Costo del producto: "))
            nventa = float(input("Ingrese el precio de venta del producto: "))
            nCantidad = int(input("Ingrese las unidades del producto:  "))
            nganancia = (nventa-nfabrica) * nCantidad
        actualizardato(numeroProducto, nProducto, nfabrica, nventa, nCantidad, nganancia)
    else: 
        
        print("El producto descrito no existe en el registro")
        

    os.system("pause")
    os.system("cls")


def elimino():
    os.system("cls")
    numeroProducto = 0
    print("Eliminar datos\n")#En esta funcion es donde llegamos a eliminar los datos de los productos que ya no son deseados,
    print("Ingrese el nombre del producto: ", end ="")#por el usuarios, donde de igual manera hacemos uso de las funciones anteriores.
    nombreProducto = input()
    numeroProducto = existencias(nombreProducto, numeroProducto)
    if  numeroProducto > 0:
        print("El producto se eliminara", nombreProducto, "desea realizar esta acción? si(S) | no(N)")
        respuesta = input()
        if  respuesta == 'S' or respuesta == 's':
            eliminardato(numeroProducto)
            print("Los datos del producto se han eliminado\n")
        elif respuesta == 'N' or respuesta == 'n':
            print("Los datos del producto no se han eliminado\n")
        else:
            print("El nombre del producto que ingreso no existe")
    else: 
        
        print("No se ha encontrado el producto.")
     

    os.system("pause")
    os.system("cls")



if os.path.isfile('Registro.txt'): 
    print("El archivo encontrado\n")        #Aquí es donde el programa buscara el archivo, para así poder hacer el ingreso de los datos
else:                                       #en caso de que el archivo no llegara a existir lo crea por si mismo.
    
    print("El archivo no se existe")
    archivo = open("Registro.txt", "w") 
    archivo.close()
    print("El archivo se ha creado")

#-----------------------------------------------------------------------------------------------------------------------------------------------    
#-----------------------------------------------------------------------------------------------------------------------------------------------
#-----DATOS DEL CLIENTE----------
def datoscliente(codcliente, telefono, nit, direccion):

    val = bool()
    val = False
    if codcliente < 0:
        val = True    
    if telefono < 0:   
        val = True      
    return val 

def existenciass(codcliente, numero):
    contador = 0
    archivoBusqueda = open("Registrocliente.txt", "r") 
    palabraProducto = codcliente + "\n"
    for codcliente in archivoBusqueda:
        contador = contador + 1            
        if codcliente == palabraProducto:  
            numero = codcliente 
    archivoBusqueda.close() 
    return numero - 1 

def ingresocliente():
    os.system("cls")

    numeroProducto = 0
    print("Ingreso clientes\n")
    print("Nombre del cliente: ", end ="") 
    nombreProducto = input()                          
                                                       
    numeroProducto = existenciass(nombreProducto, numeroProducto)

    if  numeroProducto > 0:

        
        print("El nombre del cliente ya esta registrado.")
        print("Codigo", unidad(numeroProducto), end="")
        unidades = int(input("Ingrese el nuevo codigo: "))

        while datoscliente(0,0, unidades, 0) != False:
            print("\nLos datos no pueden ser menores a 0")
            print("Ingrese los datos\n")
            print("Los codigos son: ", unidad(numeroProducto), end="")
            unidades = int(input("Ingrese el codigo del cliente: "))
        agregarunidad(numeroProducto, unidades)

    else:
        codcliente = int(input("Ingrese codigo del cliente: "))
        telefono = int(input("Ingrese el telefono del cliente: "))
        nit = (input("Ingrese el nit del cliente: "))
        direccion = (input("Ingrese direccion del cliente: "))
        while datoscliente(codcliente,telefono, nit, direccion) != False:
            print("\nLos datos no pueden ser menores a 0\n  El precio de costo de fabrica debe de ser menor al precio de venta del producto")
            print("Ingrese los datos nuevamente\n")
            codcliente = int(input("Ingrese el costo del producto: "))
            telefono = int(input("Ingrese el precio de venta del producto: "))
            nit = (input("Ingrese las unidades del producto: "))
            direccion =  (input("Ingrese direccion del cliente: "))
        archivoNuevo = open("Registrocliente.txt", "a")
        archivoNuevo.write('**********Datos del cliente**********\n')
        archivoNuevo.write("Nombre del cliente:\n")
        archivoNuevo.write(nombreProducto  + "\n")
        archivoNuevo.write("Codigo del cliente:\n")
        archivoNuevo.write(str(codcliente) + "\n")
        archivoNuevo.write("Telefono del cliente:\n")
        archivoNuevo.write(str(telefono) + "\n")
        archivoNuevo.write("Nit del cliente:\n")
        archivoNuevo.write(nit + "\n")
        archivoNuevo.write("Dirección del cliente:\n")
        archivoNuevo.write(direccion + "\n")
        archivoNuevo.write('*************************************\n')
        archivoNuevo.close()

    
    os.system("pause")
    os.system("cls")


if os.path.isfile('Registrocliente.txt'): 
    print("El archivo encontrado\n")       
else:                                      
    
    print("El archivo no se existe")
    archivo = open("Registrocliente.txt", "w") 
    archivo.close()
    print("El archivo se ha creado")
#-------------------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------------------
#-----DATOS DE LA COMPRA----------
def datoscompra(codcliente,nombre, cantidad):

    val = bool()
    val = False
    if codcliente < 0:
        val = True    
    if cantidad < 0:   
        val = True      
    return val 


def existenciasss(codcliente, numero):
    contador = 0
    archivoBusqueda = open("Registrocompra.txt", "r") 
    palabraProducto = codcliente + "\n"
    for codcliente in archivoBusqueda:
        contador = contador + 1             
        if codcliente == palabraProducto:  
            numero = codcliente 
    archivoBusqueda.close() 
    return numero - 1 

def ingresocompra():
    os.system("cls")

    numeroProducto = 0
    print("Datos de compra\n")
    print("Nombre del producto/pelicula: ", end ="") 
    nombreProducto = input()                       
                                                       
    numeroProducto = existenciasss(nombreProducto, numeroProducto)

    if  numeroProducto > 0:

        
        print("El producto ya esta en la compra.")
        print("Cantidad", unidad(numeroProducto), end="")
        unidades = int(input("Ingrese nueva cantidad de compra: "))

        while datoscliente(0,0, unidades, 0) != False:
            print("\nLos datos no pueden ser menores a 0")
            print("Ingrese los datos\n")
            print("Los cantidad es: ", unidad(numeroProducto), end="")
            unidades = int(input("Ingrese candidad de la compra: "))
        agregarunidad(numeroProducto, unidades)

    else:
        codcliente = int(input("Ingrese codigo del cliente: "))
        nombre = (input("Ingrese el nombre del cliente: "))
        cantidad = int(input("Ingrese cantidad del producto"))
        while datoscompra(codcliente,nombre, cantidad) != False:
            codcliente = int(input("Ingrese el costo del producto: "))
            nombre = (input("Ingrese el precio de venta del producto: "))
            cantidad =  int(input("Ingrese direccion del cliente: "))
        archivoNuevo = open("Registrocompra.txt", "a")
        archivoNuevo.write('**********Datos de la compra**********\n')
        archivoNuevo.write("Codigo del cliente:\n")
        archivoNuevo.write(str(codcliente) + "\n")
        archivoNuevo.write("Nombre cliente:\n")
        archivoNuevo.write(nombre + "\n")
        archivoNuevo.write("Producto del cliente:\n")
        archivoNuevo.write(nombreProducto  + "\n")
        archivoNuevo.write("Cantidad del producto:\n")
        archivoNuevo.write(str(cantidad) + "\n")
        archivoNuevo.write('*************************************\n')
        archivoNuevo.close()

    
    os.system("pause")
    os.system("cls")


if os.path.isfile('Registrocompra.txt'): 
    print("El archivo encontrado\n")        
else:                                       
    
    print("El archivo no se existe")
    archivo = open("Registrocompra.txt", "w") 
    archivo.close()
    print("El archivo se ha creado")

#------------------------------------------------------------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------------------------------------------------
#-----DATOS DE VENTA----------
def datosventa(codcliente, nombre, cantidad,precioventa,costofabrica,ganancia):

    val = bool()
    val = False
    if codcliente < 0:
        val = True    
    if cantidad < 0:   
        val = True 
    if precioventa < 0:   
        val = True
    if costofabrica < 0:   
        val = True
    if ganancia < 0:   
        val = True      
    return val 

def existenciassss(codcliente, numero):
    contador = 0
    archivoBusqueda = open("Registroventa.txt", "r") 
    palabraProducto = codcliente + "\n"
    for codcliente in archivoBusqueda:
        contador = contador + 1             
        if codcliente == palabraProducto:  
            numero = codcliente 
    archivoBusqueda.close() 
    return numero - 1 

def ingresoventa():
    os.system("cls")

    numeroProducto = 0
    print("Datos de venta\n")
    print("Nombre del producto/pelicula: ", end ="") 
    nombreProducto = input()                       
                                                       
    numeroProducto = existenciassss(nombreProducto, numeroProducto)

    if  numeroProducto > 0:

        
        print("El producto ya esta en la compra.")
        print("Cantidad", unidad(numeroProducto), end="")
        unidades = int(input("Ingrese nueva cantidad de compra: "))

        while datoscliente(0,0, unidades, 0) != False:
            print("\nLos datos no pueden ser menores a 0")
            print("Ingrese los datos\n")
            print("Los cantidad es: ", unidad(numeroProducto), end="")
            unidades = int(input("Ingrese candidad de la compra: "))
        agregarunidad(numeroProducto, unidades)

    else:
        codcliente = int(input("Ingrese el codigo del cliente: "))
        nombre = (input("Ingrese el nombre del cliente: "))
        cantidad = int(input("Ingrese la cantidad del producto: "))
        costofabrica = float(input("Ingrese el costo de fabrica del producto: "))
        precioventa = float(input("Ingrese el precio de venta del producto: "))
        ganancia = (precioventa-costofabrica) * cantidad
        while datosventa(codcliente, nombre, cantidad,precioventa,costofabrica,ganancia) != False:
            print("\nLos datos no pueden ser menores a 0\n  El precio de costo de fabrica debe de ser menor al precio de venta del producto")
            print("Ingrese los datos nuevamente\n")
            codcliente = int(input("Ingrese el codigo del cliente: "))
            nombre = (input("Ingrese el nombre del cliente: "))
            cantidad = int(input("Ingrese la cantidad del producto: "))
            costofabrica = float(input("Ingrese el costo del fabrica del producto: "))
            precioventa = float(input("Ingrese el precio de venta del producto: "))
            ganancia = (precioventa-costofabrica) * cantidad
        archivoNuevo = open("Registroventa.txt", "a")
        archivoNuevo.write('**********Datos de la venta**********\n')
        archivoNuevo.write("Codigo del cliente:\n")
        archivoNuevo.write(str(codcliente) + "\n")
        archivoNuevo.write("Nombre cliente:\n")
        archivoNuevo.write(nombre + "\n")
        archivoNuevo.write("Producto del cliente:\n")
        archivoNuevo.write(nombreProducto  + "\n")
        archivoNuevo.write("Cantidad del producto:\n")
        archivoNuevo.write(str(cantidad) + "\n")
        archivoNuevo.write("Costo de fabrica")
        archivoNuevo.write(str(costofabrica) + "\n")
        archivoNuevo.write("Precio de venta")
        archivoNuevo.write(str(precioventa) + "\n")
        archivoNuevo.write("Ganancia")
        archivoNuevo.write(str(ganancia) + "\n")
        archivoNuevo.write('*************************************\n')
        archivoNuevo.close()

    
    os.system("pause")
    os.system("cls")


if os.path.isfile('Registroventa.txt'): 
    print("El archivo encontrado\n")        
else:                                       
    
    print("El archivo no se existe")
    archivo = open("Registroventa.txt", "w") 
    archivo.close()
    print("El archivo se ha creado")
#-------------------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------------------------
#-----DATOS DE LA FACTURA----------
def mostrarfactura():
    os.system("cls")
    archivoProducto = open("Registroventa.txt", "r")
    for listado in archivoProducto:
        print(listado, end = "")        
    archivoProducto.close               
    os.system("pause")
    os.system("cls")

if os.path.isfile('Registrofactura.txt'): 
    print("El archivo encontrado\n")        
else:                                       
    
    print("El archivo no se existe")
    archivo = open("Registrofactura.txt", "w") 
    archivo.close()
    print("El archivo se ha creado")

while opcionMenu != 9: 
    
    print(" *********************** Menu ************************")
    print("| \t1-Ingreso de datos en el inventario              |")
    print("| \t2-Mostras productos existentes en el inventario  |")
    print("| \t3-Añadir unidades a productos registrados        |")
    print("| \t4-Modificacion de productos                      |")
    print("| \t5-Clientes.                                      |")
    print("| \t6-Compras.                                       |")
    print("| \t7-Ventas.                                        |")
    print("| \t8-Facturas.                                      |")    
    print("| \t9-Salir                                          |")   
    print(" *****************************************************")
    print("Seleccione una opcion: ", end="")
    opcion = int(input())
    opcionMenu = opcion
    
    if opcionMenu == 1:
        ingreso()       
    elif opcionMenu == 2:
        mostrar() 
    elif opcionMenu == 3:
        añado()                 # Aquí a cada una de las funciones para que al momento de seleccionar una opcion realice
    elif opcionMenu == 4:       #lo que desea el usuario
        actualizo() 
    elif opcionMenu == 5:
        ingresocliente() 
    elif opcionMenu == 6:
        ingresocompra()
    elif opcionMenu == 7:
        ingresoventa() 
    elif opcionMenu == 8:
        mostrarfactura() 
    elif opcionMenu == 9: 
       
        print("\n Nos vemos")
    else:
        print("\nSeleccione una opcion correcta.")
