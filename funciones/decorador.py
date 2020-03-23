# Declarar funcion decoradora con la palabra reservada pass
def decorador(funcion) :
  def nueva_funcion(*args, **kwargs):
    print("Podemos agregar codigo antes")
    resultado = funcion(*args, **kwargs)
    print("Podemos agregar codigo despues")
    return resultado
  return nueva_funcion

@decorador
def funcion_a_decorar() :
  print("Esta es una funcion a decorar")

# LLamar funcion a decorar
funcion_a_decorar()


# Definir una funcion que recibe parametros por valor y los suma
@decorador
def suma(val1, val2) :
  return val1 + val2

# Llamar la funcion crear_mensaje
print(suma(10, 10))