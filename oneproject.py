import os 

def filter_even_numbers(num):
    if num%2 == 0:
        return True
    
termina = 0
while termina == 0:
    try:

        numbers = input("ingrese numeros separados por comas: ").split(",")
        lista_numeros = [int(x) for x in numbers]
        nueva_lista = list(filter(filter_even_numbers,lista_numeros))
        print(nueva_lista)

        termina += 1
    except:
        os.system("cls" if os.name == "nt" else "clear")
        print("Error,siga las instruciones")