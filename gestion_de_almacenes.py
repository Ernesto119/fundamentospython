import os

class Almacenes:#sera almaacen
    def __init__(self,uid,nombre,altura,anchura,largura):
        self.uid = uid
        self.nombre = nombre
        self.data = []
        self.capacidad = altura*largura*anchura
    def inventario(self):
        self.data.append(str(self.uid))
        self.data.append(self.nombre)
        self.data.append(str(self.capacidad))
    
        
class Item:
    def __init__(self,uid,nombre):
        self.uid = uid
        self.nombre = nombre
        self.contenedor = []
    def estantes(self):
        self.contenedor.append(str(self.uid))
        self.contenedor.append(self.nombre)
        
        
def crear_almacen(nombre,altura,anchura,largura,listado,inventario): 
     
    almacen = Almacenes(str(len(listado)).zfill(4),nombre,altura,anchura,largura)
    listado.append(almacen.data)
    almacen.inventario() 
    inventario.append([]) 
    print(len(listado))
    
def crear_objecto(nombre,invetario):
    objecto = Item(str(len(invetario)).zfill(4),nombre)
    invetario.append(objecto.contenedor)
    objecto.estantes()
    print(len(invetario))
    
def agregar_objeto(seleccion,inventario,nombre):
    estante = inventario[seleccion]
    estante.append(nombre)
    
def pantalla(listado):
     
    datos_de_listas = ""
    datos_de_listas+="ID"
    datos_de_listas+="Nombre".center(30)
    datos_de_listas+="Capacidad"
    print(datos_de_listas)
    print("".rjust(45,"-"))
    
    for i in range(len(listado)):
        
        elgir_elemtnos_de_lista = listado[i]
        separador_de_palabras = ""
        separador_de_palabras+=elgir_elemtnos_de_lista[0]
        separador_de_palabras+=elgir_elemtnos_de_lista[1].rjust(15)
        separador_de_palabras+=elgir_elemtnos_de_lista[2].rjust(20)
        print(separador_de_palabras)
        
def pantalla_de_inventario(inventario):
    
    datos_de_listas = ""
    datos_de_listas+="ID"
    datos_de_listas+="Nombre".center(30)
    print(datos_de_listas)
    print("".rjust(45,"-"))
    
    for i in range(len(invetario)):
        
        elgir_elemtnos_de_lista = invetario[i]
        separador_de_palabras = ""
        separador_de_palabras+=elgir_elemtnos_de_lista[0]
        separador_de_palabras+=elgir_elemtnos_de_lista[1].rjust(15)
        print(separador_de_palabras)
    
    
    
listado = []      
invetario = []
     

while True:
    print("1.Registrar almacen","\n2.ver almacenes","\n3.Acceder al almacen","\n4.Salir")
    opcion = input("Ingrese una opcion: ")
    os.system("clear")
    if opcion == "1":
        
        nombre_del_almacen = input("ingrese el nombre: ")
        altura= int(input("Ingrese la altura:"))
        anchura= int(input("Ingrese la anchura: "))
        largura= int(input("Ingre la largura: "))
        crear_almacen(nombre_del_almacen,altura,anchura,largura,listado,invetario)
        os.system("clear")
        
    elif opcion =="2":
        
        print(invetario)
        pantalla(listado)
        input()
        os.system("clear")
        
    elif opcion == "3":
        
        pantalla(listado)
        seleccion = int(input("Elija un almacen: "))
        nombre_del_objecto = input("ingrese el nombre: ")
        agregar_objeto(seleccion,invetario,nombre_del_objecto)
        
    elif opcion == "4":
        break
    
print("bye")