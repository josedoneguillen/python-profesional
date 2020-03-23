# Definir una funcion
def saluda() :
  print("Hola Mundo")

# Llamar la funcion saluda
saluda()

# Definir una funcion que recibe parametros por valor
def crear_mensaje(nombre) :
  mensaje = "Hola {}, bienvenido al curso de Python 3".format(nombre)
  return mensaje

# Llamar la funcion crear_mensaje
print(crear_mensaje("Jose"))

# Definir una funcion que recibe parametros por valor y los suma
def suma(val1, val2, val3) :
  return val1 + val2 + val3

# Llamar la funcion crear_mensaje
print(suma(10, 10, 10))

# Definir una funcion para retornar mas de un valor
def obtener_curso() :
  return "Curso de Python", "Basico", 3.6

# Asignar los valores de la funcion obtener_curso
curso, nivel, version = obtener_curso()

# Llamar la funcion obtener_curso
print(curso, nivel, version)