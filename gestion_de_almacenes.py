import os

class Almacenes:
    
    def __init__(self,uid,nombre,altura,anchura,largura):
        self.uid = uid#esto es el id esta asi porwue python tiene una funcion llamada id
        self.nombre = nombre
        self.data = []#esta lista se va a agregar a la lista de almacenes cono los datos "inventario" para que asi este dividido cada almacen nuevo
        self.capacidad = altura*largura*anchura #multiplica esto elemento para dar la capacidad
        
    def inventario(self):
        self.data.append(str(self.uid))#coviete en string el numero id
        self.data.append(self.nombre)
        self.data.append(str(self.capacidad))#convierte en estring la capacidad
    
        
class Item:
    
    def __init__(self,uid,nombre,area):
        self.uid = uid
        self.nombre = nombre
        self.area = area
        self.estante = []
        
    def archivar(self):  
        self.estante.append(str(self.uid))
        self.estante.append(self.nombre)
        self.estante.append(str(self.area))
        
def crear_almacen(nombre,altura,anchura,largura,lista_almacenes,inventario): 
    #creaa el objecto ingresado por el usuario, zfilll(4) se usa para agregar ceros a la izquierda
    almacen = Almacenes(str(len(lista_almacenes)).zfill(4),nombre,altura,anchura,largura)
    lista_almacenes.append(almacen.data)
    almacen.inventario() #este llamda agrega los elementos
    inventario.append([]) #cuando se cree un nuevo almacen se agregara una lista vacia a inventario para que asi se agrege los item en la misma posicion del almacen
   # print(len(lista_almacenes)) cuidado por si hago se rompe por quitar esta linea
 
 
def crear_articulo(nombre,inventario,area):
    #creaccion del item
    articulo = Item(str(len(inventario)).zfill(4),nombre,area)
    inventario.append(articulo.estante)
    articulo.archivar()
 
def retirar_objecto(seleccion,inventario):
    inventario[seleccion].pop(seleccion)     
    
def pantalla(lista_almacenes,inventario):
     #muestra el mene de los almacenesf

    print("ID","Nombre".center(33),"Capacidad disponible")
    print("".center(59,"-")) # aqui se agrega "-" para que tenfa una apariencia mejor
    estante = inventario[0]
    descatar = 0
    for est in estante:#calcular la suma del area de todos los objeto dentro del almacen para restacelo luego a "disponible"
        for lista in est:
            if len(lista)>= 3:
                descatar += int(est[2])
        
    for i in range(len(lista_almacenes)):
        
        # los ellemento de la listas selecionado se van a separar de esta manera
        elegir_elemetnos_de_lista = lista_almacenes[i]#espacio total
        disponible = elegir_elemetnos_de_lista[2]# esto sirve par que sea el espacion disponible
        print(elegir_elemetnos_de_lista[0],elegir_elemetnos_de_lista[1].center(30),f"{int(disponible)-descatar}/{elegir_elemetnos_de_lista[2]}".center(21))
        
 #cambia esta funcion       
def pantalla_de_inventario(inventario):
    #muestra la pantala de los item en los almacenes
    
    print("ID","Nombre".center(33),"Area del articulo")
    print("".center(59,"-"))
    # aqui se agrega "-" para que tenfa una apariencia mejor
    for i in range(len(inventario)):
        
        # los ellemento de la listas selecionado se van a separar de esta manera
        
        elegir_elemtnos_de_lista = inventario[i]
        print(elegir_elemtnos_de_lista[0],elegir_elemtnos_de_lista[1].center(30),elegir_elemtnos_de_lista[2].center(12))
    
    
lista_almacenes = []  # aqui se guardan los almacenes    
inventario_de_almacen = []# aqui se guardan los objeto de cada almacen
     

while True:
    print("1.Registrar almacen","\n2.ver almacenes","\n3.Acceder al almacen","\n4.Salir")
    opcion = input("Ingrese una opcion: ")
    os.system("clear")
    if opcion == "1":
        while True:
            
            try:
                #crea almacenes
                nombre_del_almacen = input("ingrese el nombre: ")
                altura= int(input("Ingrese la altura: "))
                anchura= int(input("Ingrese la anchura: "))
                largura= int(input("Ingre la largura: "))
                crear_almacen(nombre_del_almacen,altura,anchura,largura,lista_almacenes,inventario_de_almacen)
                os.system("clear")
                break
            except:
                
                os.system("clear")
                print("Ingrese numeros enteros en las medidas")
                
    elif opcion =="2":
        #muestra la lista de los almacenes el imput es que el usuario salga
       
        pantalla(lista_almacenes,inventario_de_almacen)
        input()
        os.system("clear")
        
        
    elif opcion == "3":
        
        while True:
            try:   
                #aqui se mostrarala lista de los almacenes para que el usuario ingrese dentro y vea los item adentro
                pantalla(lista_almacenes,inventario_de_almacen)
                selecciona_almacen = (input("\nElija el almacen o escriba \"-exict\" para salir: "))
                os.system("clear")
                if selecciona_almacen == "-exict":
                    break
                
                #aqui se tiene que mostrar el inventario
                pantalla_de_inventario(inventario_de_almacen[int(selecciona_almacen)])
                os.system("clear")
                opciones_invetario = int(input("1.Salir 2.Agregar objecto 3.Retirar objecto\nElija: "))
                os.system("clear")
                
                if opciones_invetario == 1:
                    
                    break
                
                elif opciones_invetario == 2:
                    
                    while True:
                        
                        pantalla_de_inventario(inventario_de_almacen[int(selecciona_almacen)])
                        nombre = input("\nEscriba  \"-exict\" para salir \nIngrese el nombre del objecto: ")
                       
                        if nombre == "-exict":
                            os.system("clear")
                            break
                           
                        area_objecto = int(input("Ingrese el valor de area del objecto: "))
                        os.system("clear")
                        crear_articulo(nombre,inventario_de_almacen[int(selecciona_almacen)],area_objecto)
                        
                        
                elif opciones_invetario == 3:
                    pantalla_de_inventario(inventario_de_almacen[int(selecciona_almacen)])
                    retirar = int(input("Ingese el id del objeto: "))
                    retirar_objecto(retirar,inventario_de_almacen)
                    os.system("clear")
                    break
                    
                else:
                    os.system("clear")
                    print("Esa opcion no existe")
                    
            except:
                print("Error")
                
    elif opcion == "4":
        break
    
    else:
        print("Esa opcion no existe")
    
print("bye")