# Asignar funcion a una variable

# Definir funcion
def centigrados_a_farenheit(grados) :
  return grados * 1.8 + 32

# Declaracion de variable
funcion_variable = centigrados_a_farenheit(128)

# Imprimir resultado
print(funcion_variable)

#  O Declaracion de variable
funcion_variable = centigrados_a_farenheit

# Imprimir resultado
print(funcion_variable(28))

# Lambdas o funcion anonima en una sola linea retornan a la variable por defecto
mi_funcion = lambda grados=0 : grados * 1.8 + 32

# llamar e imprimir
print(mi_funcion(30))