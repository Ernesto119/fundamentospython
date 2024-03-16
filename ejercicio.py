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