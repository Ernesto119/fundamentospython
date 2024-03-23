

class Almacen:
    def __init__(self,idalmacen,nombre,altura,largura,anchura,):
        self.idamalcen = idalmacen
        self.nombre = nombre
        self.capacidad = altura*largura*anchura
        self.inventario = []
    def insetar(self):
        return [self.idamalcen, self.nombre, self.capacidad] 
    

class Articulo:
    def __init__(self,idarticulo,nombre,area):
        self.idarticulo = idarticulo
        self.nombre = nombre
        self.area = area
    def insetar(self):
        return [self.idarticulo, self.nombre, self.area]
    
            

def pantalla_almacenes(almacenes,inventario):
    print('ID','Nombre'.center(44),'Capacidad disponible')
    print('-'*70)
    for alma in range(len(almacenes)):
        capacidad_actual = almacenes[alma][2]
        for i in inventario[alma]:
            capacidad_actual -= i[2]
          #calula  el espacio que queda de cada almacen restado el area de los los articulos  en el inventario al elemento[2](Representa la capcidad del almacen)              
        almacen = almacenes[alma]
        print(almacen[0],almacen[1].center(45),f"{str(capacidad_actual).rjust(10)}/{str(almacen[2])}")
        
        
        
def pantalla_inventario(lista_inventarios):
    print('ID','nombre'.center(44),'Area del onjecto')
    print('-'*70)
    for inve in range(len(lista_inventarios)):
        inventario = lista_inventarios[inve]
        print(inventario[0],inventario[1].center(45),str(inventario[2]).center(20))        
        
    


