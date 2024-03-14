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
    
    def __init__(self,uid,nombre):
        self.uid = uid
        self.nombre = nombre
    
        
def crear_almacen(nombre,altura,anchura,largura,lista_almacenes,inventario): 
    #creaa el objecto ingresado por el usuario, zfilll(4) se usa para agregar ceros a la izquierda
    almacen = Almacenes(str(len(lista_almacenes)).zfill(4),nombre,altura,anchura,largura)
    lista_almacenes.append(almacen.data)
    almacen.inventario() #este llamda agrega los elementos
    inventario.append([]) #cuando se cree un nuevo almacen se agregara una lista vacia a inventario para que asi se agrege los item en la misma posicion del almacen
   # print(len(lista_almacenes)) cuidado por si hago se rompe por quitar esta linea
 
 
def crear_articulo(nombre,inventario):
    
    articulo = Item(str(len(inventario)).zfill(4),nombre)
    inventario.append(articulo.nombre)
    
      
    
def pantalla(lista_almacenes):
     # muestra el menz de llos almacenes
    datos_de_listas = ""
    datos_de_listas+="ID"
    datos_de_listas+="Nombre".center(30)#aqui la logica es que se agregen los elmentp de manera separada por center
    datos_de_listas+="Capacidad"
    print(datos_de_listas)
    print("".rjust(45,"-"))# aqui se agrega "-" para que tenfa una apariencia mejor
    
    for i in range(len(lista_almacenes)):
        # los ellemento de la listas selecionado se van a separar de esta manera
        elgir_elemtnos_de_lista = lista_almacenes[i]
        separador_de_palabras = ""
        separador_de_palabras+=elgir_elemtnos_de_lista[0]
        separador_de_palabras+=elgir_elemtnos_de_lista[1].rjust(15)
        separador_de_palabras+=elgir_elemtnos_de_lista[2].rjust(20)
        print(separador_de_palabras)
        
        
def pantalla_de_inventario(inventario):
    #muestra la pantala de los item en los almacenes
    datos_de_listas = ""
    datos_de_listas+="ID"
    datos_de_listas+="Nombre".center(30)
    print(datos_de_listas)
    print("".rjust(45,"-"))
    
    for i in range(len(inventario_de_almacen)):
        
        elgir_elemtnos_de_lista = inventario_de_almacen[i]
        separador_de_palabras = ""
        separador_de_palabras+=elgir_elemtnos_de_lista[0]
        separador_de_palabras+=elgir_elemtnos_de_lista[1].rjust(15)
        print(separador_de_palabras)
    
    
    
lista_almacenes = []  # aqui se guardan los almacenes    
inventario_de_almacen = []# aqui se guardan los objeto de cada almacen
     

while True:
    print("1.Registrar almacen","\n2.ver almacenes","\n3.Acceder al almacen","\n4.Salir")
    opcion = input("Ingrese una opcion: ")
    os.system("clear")
    if opcion == "1":
        #crea almacenes
        nombre_del_almacen = input("ingrese el nombre: ")
        altura= int(input("Ingrese la altura:"))
        anchura= int(input("Ingrese la anchura: "))
        largura= int(input("Ingre la largura: "))
        crear_almacen(nombre_del_almacen,altura,anchura,largura,lista_almacenes,inventario_de_almacen)
        os.system("clear")
        
    elif opcion =="2":
        #muestra la lista de los almacenes el imput es que el usuario salga
        print(inventario_de_almacen)
        pantalla(lista_almacenes)
        input()
        os.system("clear")
        

    elif opcion == "3":
        
        print(inventario_de_almacen)
        #aqui se mostrarala lista de los almacenes para que el usuario ingrese dentro y vea los item adentro
        pantalla(lista_almacenes)
        selecciona_almacen = int(input("Elija el almacen: "))
        nombre = input("Ingrese el nombre del objecto:")
        crear_articulo(nombre,inventario_de_almacen[selecciona_almacen])
          
    elif opcion == "4":
        break
    
print("bye")