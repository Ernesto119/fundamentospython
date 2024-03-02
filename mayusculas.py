cadenas =input("ingrese palabras o oraciones separadas por coma:").split(",")

def uppercase_string(chain):
    return chain.upper()

lista_mayuscula = list(map(uppercase_string,cadenas))

print(lista_mayuscula)
