import os
from funciones.logica import *
    
lista_almacenes = [] 
inventario_de_almacen = []
     

while True:
    print("1.Registrar almacen","\n2.ver almacenes","\n3.Acceder al almacen","\n4.Salir")
    opcion = input("Ingrese una opcion: ")
    os.system('cls' if os.name == 'nt' else 'clear')
    if opcion == "1":
        while True:
            
            try:
               
                nombre_del_almacen = input("ingrese el nombre: ")
                altura= int(input("Ingrese la altura: "))
                anchura= int(input("Ingrese la anchura: "))
                largura= int(input("Ingre la largura: "))
                crear_almacen(nombre_del_almacen,altura,anchura,largura,lista_almacenes,inventario_de_almacen)
                os.system('cls' if os.name == 'nt' else 'clear')
                break
            except:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Ingrese numeros enteros en las medidas")
                
    elif opcion =="2":
       
        pantalla(lista_almacenes,inventario_de_almacen)
        input()
        os.system('cls' if os.name == 'nt' else 'clear')
        
        
    elif opcion == "3":
        
        while True:
            try:   
                
                pantalla(lista_almacenes,inventario_de_almacen)
                selecciona_almacen = (input("\nElija el almacen o escriba \"-exict\" para salir: "))
                os.system('cls' if os.name == 'nt' else 'clear')
                
                if selecciona_almacen == "-exict":
                    break
                
                
                pantalla_de_inventario(inventario_de_almacen[selecciona_almacen])
                opciones_invetario = int(input("1.Salir 2.Agregar objecto 3.Retirar objecto\nElija: "))
                os.system('cls' if os.name == 'nt' else 'clear')
                
                if opciones_invetario == 1:
                    
                    break
                
                elif opciones_invetario == 2:
                    
                    while True:
                        
                        pantalla_de_inventario(inventario_de_almacen[int(selecciona_almacen)])
                        nombre = input("\nEscriba  \"-exict\" para salir \nIngrese el nombre del objecto: ")
                       
                        if nombre == "-exict":
                            
                            os.system('cls' if os.name == 'nt' else 'clear')
                            break
                           
                        area_objecto = int(input("Ingrese el valor de area del objecto: "))
                        os.system('cls' if os.name == 'nt' else 'clear')
                        crear_articulo(nombre,inventario_de_almacen[int(selecciona_almacen)],area_objecto)
                        
                        
                elif opciones_invetario == 3:
                    
                    pantalla_de_inventario(inventario_de_almacen[int(selecciona_almacen)])
                    retirar = int(input("Ingese el id del objeto: "))
                    inventario_de_almacen[retirar].pop(retirar)
                    
                    os.system('cls' if os.name == 'nt' else 'clear')
                    break
                    
                else:
                    
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("Esa opcion no existe")  
            except:
                print("Error opcion invalidad")
                
    elif opcion == "4":
        
        break
    
    else:
        print("Esa opcion no existe")
    
print("Gracias por usar el sistema")


def suma(n,n2):
    return n + n2