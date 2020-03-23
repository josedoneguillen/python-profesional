# Declaracion de clase
class Circulo:
  pi = 3.14159265
  
  # Declarando metodo de clase para decorar la variable de clase pi
  @classmethod
  def area(cls, radio):
    return cls.pi * radio**2

    