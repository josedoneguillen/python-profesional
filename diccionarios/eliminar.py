# Declarar variable tipo diccionario
diccionario = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8}

# Imprimir cantidad
print(len(diccionario))

# Eliminar una llave del diccionario
del diccionario["a"]

# Imprimir cantidad
print(len(diccionario))

# Eliminar un elemento del diccionario con pop 
print(diccionario.pop("b"))

# Imprimir cantidad
print(len(diccionario))

# Eliminar todo del diccionario con clear
diccionario.clear()

# Imprimir cantidad
print(len(diccionario))
