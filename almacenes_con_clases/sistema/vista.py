"""Sistema de almacense con clases en python"""


from modulos import Almacen, Articulo, pantalla_almacenes, pantalla_inventario
import os






menu ="""
menu
1.ver almacenes
2.Registrar un almacen
3.Eliminar Almacen
4.Ver inventario de un almacen
5.Agregar articulos a un almacen
6.Eliminar articulos de un almacen
7.Salir
"""


lista_almacenes = []
inventario_de_almacen = []
#almacenamiento de los datos

while True:
    os.system('cls' if os.name == 'nt' else 'clear')

    print(menu)
    selector = input("Ingrese una opcion: ")

    os.system('cls' if os.name == 'nt' else 'clear')


    if  selector == "1":
        pantalla_almacenes(lista_almacenes,inventario_de_almacen)
        input("presione enter para salir:")  
    elif  selector == "2":
        while True:
            try:
                crear_almacen = Almacen(
                len(lista_almacenes)+1,
                input("ingrese el nombre: "),
                int(input("Ingrese la altura: ")),
                int(input("Ingrese la anchura: ")),
                int(input("Ingrese la largura: ")),     
            )
                lista_almacenes.append(crear_almacen.insetar())
                inventario_de_almacen.append(crear_almacen.inventario)
                break
            except:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Error, ingrese un numero entero")
            
    elif  selector == "3":
        pantalla_almacenes(lista_almacenes,inventario_de_almacen)
        elejir_dele = int(input("Elija el almacen que desea eliminar: "))
        lista_almacenes.pop(elejir_dele-1)
        inventario_de_almacen.pop(elejir_dele-1)
    
    elif  selector == "4":
        while True:
            try:
                pantalla_almacenes(lista_almacenes,inventario_de_almacen)
                elejir = int(input("Elija un almacen: "))
                os.system('cls' if os.name == 'nt' else 'clear')
                pantalla_inventario(inventario_de_almacen[elejir-1]) 
                input("Enter para salir:")
                break
            except:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Opcion invalidad")
            
    elif  selector == "5":
        while True:
            try:
                pantalla_almacenes(lista_almacenes,inventario_de_almacen)
                eleccion = int(input("ELija un almacen o escriba 0 para salir: "))
                if eleccion == 0:
                    break
                else:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    pantalla_inventario(inventario_de_almacen[eleccion-1])
                    crear_articulo = Articulo(
                    len(inventario_de_almacen[eleccion-1])+1,
                    input("Ingrese el nombre del articulo: "),
                    int(input("Ingrese el area cuadrada del articulo: "))
                    )
                    inventario_de_almacen[eleccion-1].append(crear_articulo.insetar())
                    os.system('cls' if os.name == 'nt' else 'clear')
            except:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Error: seleccione una opcion validad")
            
    elif  selector == "6":
        pantalla_almacenes(lista_almacenes,inventario_de_almacen)
        selec = int(input("ELija un almacen: "))
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            try: 
                pantalla_inventario(inventario_de_almacen[selec-1])
                quitar = int(input("Elija el objecto o escriba 0 para salir: "))
                if quitar == 0:
                    break
                else:
                    inventario_de_almacen[selec-1].pop(quitar-1)
            except:
                print("error")  
            
    elif selector == "7":
        break
    else:
        print("opcion invalidad")
        input("Presione enter para volver")
# pass
print("adios")

