# Declaracion de clase
class Gato :
  def __init__(self, nombre):
    self.nombre = nombre

  def __str__(self):
    return self.nombre   

# Declaracion de clase
class Pato(object) :
  def __init__(self, nombre):
    self.nombre = nombre

  def __str__(self):
   return self.nombre

# Instanciar clases
gato = Gato("Bigotes")       
pato = Pato("Lucas")

# Imprimir resultado se usa __dict__ para ver un diccionario de todos los atributos del objeto
print(gato.__dict__)
print(pato)