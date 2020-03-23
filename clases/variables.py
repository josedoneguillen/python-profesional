# Declaracion de clase
class Circulo :
  # Variable de clase o atributos
  pi = 3.14159265
  def __init__(self, radio) :
    self.radio = radio


# Crear instancias
circulo_a = Circulo(10)
circulo_b = Circulo(20)

# Reasignar
circulo_b.radio = 100

# Imprimir resultados
print(circulo_a.radio)
print(circulo_b.radio)

# Imprimir resultados
print(Circulo.pi)
print(circulo_a.pi)
print(circulo_b.pi)