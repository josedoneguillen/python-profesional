# Definir funcion para crear usuario
def crear_usuario(nombre, apellido, edad=0):
  return {
      'nombre' : nombre,
      'apellido' : apellido,
      'nombre_completo' : "{} {}".format(nombre, apellido),
      'edad': edad  
  }

# Crear usuario
user = crear_usuario("Jose", "Done")

# Imprimir usuario
print(user)