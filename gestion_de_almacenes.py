class Item:#sera almaacen
    def __init__(self,uid,nombre):
        self.uid = uid
        self.nombre = nombre
        self.data = []
        
    def inventario(self):
        self.data.append(self.nombre)
        
sub = []      
           
objecto = Item(1,"leche")
objecto2 = Item(2,"arroz")
sub.append(objecto.data) 
sub.append(objecto2.data)
objecto.inventario()
objecto2.inventario()
objecto.data.append("agua")


while True:
    print("1Agregar","2ver")
    opcion = input(": ")
    if opcion == "1":
        sub.append(objecto.data)
    elif opcion =="2":
        print(sub[0])