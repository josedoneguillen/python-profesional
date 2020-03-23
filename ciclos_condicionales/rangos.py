# uso de la funcion range (desde, hasta, saltos)
for valor in range(1, 21, 2) :
  print(valor)

# uso de la funcion range para iterar una lista
lista =  [1,2,3,4,5]
for valor in range(len(lista)) :
  print("indice: ", valor, " valor: ", lista[valor])


# uso de la funcion enumerate para iterar una lista
for indice, valor in enumerate(lista) :
  print("indice: ", indice, " valor: ", valor)