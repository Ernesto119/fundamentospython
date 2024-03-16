class Almacenes:
    
    def __init__(self,uid,nombre,altura,anchura,largura):
        self.uid = uid#esto es el id esta asi porwue python tiene una funcion llamada id
        self.nombre = nombre
        self.data = []#esta lista se va a agregar a la lista de almacenes cono los datos "inventario" para que asi este dividido cada almacen nuevo
        self.capacidad = altura*largura*anchura #multiplica esto elemento para dar la capacidad
        
    def inventario(self):
        self.data.append(str(self.uid))
        self.data.append(self.nombre)
        self.data.append(str(self.capacidad))
    
        
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
    
 
# def retirar_objecto(seleccion,inventario):
#     inventario[seleccion].pop(seleccion)   
      
    
def pantalla(lista_almacenes,inventario):

    print("ID","Nombre".center(33),"Capacidad disponible")
    print("".center(59,"-")) 
    for i in range(len(lista_almacenes)):
        almacen = lista_almacenes[i]
        espacio_ocupado = 0
        for item in inventario[i]:
            
            if len(item) >= 3:
                espacio_ocupado += int(item[2])  # Suma el área de cada artículo
        espacio_disponible = int(almacen[2]) - espacio_ocupado  # Calcula el espacio disponible restando el área ocupada del área total
        print(almacen[0], almacen[1].center(30), f"{espacio_disponible}/{almacen[2]}".center(21))
        
   
def pantalla_de_inventario(inventario:int):
    
    print("ID","Nombre".center(33),"Area del articulo")
    print("".center(59,"-"))
    for i in range(len(inventario)):
        
        # los ellemento de la listas selecionado se van a separar de esta manera
        
        elegir_elemtnos_de_lista = inventario[i]
        print(elegir_elemtnos_de_lista[0],elegir_elemtnos_de_lista[1].center(30),elegir_elemtnos_de_lista[2].center(12))
    