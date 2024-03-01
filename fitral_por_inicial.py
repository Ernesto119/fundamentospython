# filtra nombres que comienzan con a y hacer una funcion llama filter_names_starting_with_a
def filter_names_starting_with_a(nombre):
   nueva_lista = filter(lambda x: not x.startswith("A"),nombre)

   return list(nueva_lista)

nombres = list(input("Ingrese nombres seoarados por coma:").split(","))



print(filter_names_starting_with_a(nombres))