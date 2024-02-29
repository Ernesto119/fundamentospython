def filter_long_word(palabras):
    palabras_filtradas = filter(lambda p: len(p) < 5, palabras)
    ls = []
    
    for pal in palabras_filtradas:
        ls.append(pal)
    return ls


palabras = input("ingrse palabras separada por coma: ").split(",")
print(filter_long_word(palabras))
