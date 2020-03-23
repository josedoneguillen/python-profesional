# Declarar variable tipo diccionario
diccionario = {"a": 1, "b": 2, "c": 3, "a": 4}

# Encontrar un valor por llave y guardarlo en resultado
resultado = diccionario["a"]

# Imprimir diccionario
print(resultado)

# Encontrar un valor usando in y guardarlo en resultado
resultado = "z" in diccionario

# Imprimir diccionario
print(resultado)


# Encontrar un valor usando get y guardarlo en resultado
resultado = diccionario.get("x", "La llave no existe")

# Imprimir diccionario
print(resultado)

# Encontrar un valor usando setdefault y guardarlo en resultado
resultado = diccionario.setdefault("v", {})

# Imprimir diccionario
print(resultado)

# Imprimir diccionario
print(diccionario)