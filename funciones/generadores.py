# Declarar un generador
def tabla_multiplicador(numero, maximo=10):
  for posicion in range(1, maximo+1) :
      # yield es un retorno que no termina la ejecucion de la funcion (al igual que return permite retornar mas valores en una tupla)
      yield numero, posicion, numero * posicion

# Cliclo For
for numero, posicion, resultado in tabla_multiplicador(9) :
  print(numero, "*", posicion, "=", resultado)