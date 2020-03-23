# Declaracion de funcion suma que reciba una cantidad indefinida de argumentos como una tupla
def suma(parametro_requerido, *args) :
  total = parametro_requerido
  for valor in args :
    total += valor
  return total

# Llamar funcion suma
print(suma(10,10,10,20))

# Declaracion de funcion suma que reciba una cantidad indefinida de argumentos como un diccionario
def usuarios_autenticados(**kwargs) :
  return kwargs

# Llamar funcion usuarios_autenticados
print(usuarios_autenticados(codi=True, facilito=False))