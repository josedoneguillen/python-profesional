#lista = []
#
#for x in range(0, 101):
#  lista.append(x)
#
#print(lista)

estructura_lista = [ "indice-" + str(x) for x in range(0, 100) ]

print(estructura_lista)

estructura_tupla = tuple(( x for x in range(0, 100) 
                                              if x % 2 == 0) )

print(estructura_tupla)

estructura_diccionario = { indice:valor 
                           for indice, valor in enumerate(estructura_lista) }

print(estructura_diccionario)