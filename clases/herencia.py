# Declaracion de clase base
class Animal :

  # Metodos
  def comer(self) :
    print("Comiendo")

  def dormir(self) :
    print("Durmiendo")

# Declaracion de clase base para herencia multiple
class Mascota :

  # Metodos
  def fecha_adopcion(self, fecha) :
    self.fecha_adopcion = fecha 

# Declaracion de clase derivada con herencia multiple
class Perro(Animal, Mascota) :

  # Constructor para inicializar atributos
  def __init__(self, nombre) :
    self.nombre = nombre

  # Metodos
  def ladrar(self) :
    print("Ladrando")

# Instancia de perro
perro = Perro("Scooby")

# Ejecutar metodo comer de la clase base
perro.comer()

# Imprimir nombre de la clase perro
print(perro.nombre)

# Asignar e imprimir fecha adopcion
perro.fecha_adopcion = "hoy"
print(perro.fecha_adopcion)