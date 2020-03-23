# Declarar variable
def mostrar_mensaje(mensaje) :
  mensaje = mensaje.title()

  def mostrar() :
   print(mensaje)
  return mostrar

# Asignar la funcion a una variable global
nueva_funcion = mostrar_mensaje("CodigoFacilito")

# Llamar la nueva funcion
nueva_funcion()