# Declaracion de tupla
tupla = (1,2,3,4,5,6)
tupla_dos = (100,200,300,400)

# Declaracion de lista
lista = [10,20,30,40]

# Declaracion de variables por posicion en una sola linea
uno, dos, tres, *cuatro = tupla

# Imprimir
print(uno)
print(dos)
print(tres)
print(cuatro)

# Funcion zip para comprimir la tupla en un objeto
resultado = zip(tupla, lista, tupla_dos)

# Imprimir resultado
print(resultado)

# Convertir de lista a tupla
resultado = tuple(resultado)

# Imprimir resultado
print(resultado)

# Convertir de tupla a lista
resultado = list(resultado)

# Imprimir resultado
print(resultado)

