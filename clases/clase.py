# Declarar una clase
class Usuario:
  # Pass representa una sentencia nula
  pass
  
  # Constructor
  def __init__(self, username="", correo="", nombre="") :
      self.username = username
      self.correo= correo
      self.nombre = nombre

  # Metodos
  def saluda(self):
    print("Hola, soy {} un usuario".format(self.nombre))      

# Declarar un objeto instanciando la clase
codi = Usuario("josedone", "jdone@email.com", "Jose")
#codi.username = "Jose"
#codi.correo = "jdone@email.com"
#facilito = Usuario()

# Ver de que tipo es el objeto
print(type(codi))

# Usar el metodo saluda
codi.saluda()

# Imprimir email
print(codi.correo)