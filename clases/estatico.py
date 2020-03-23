# Declaracion de clase
class Triangulo :
  # Declarar metodo estatico
  @staticmethod  
  def area(base, altura):
    return (base * altura) / 2

  #def area(self):
    #return (self.base * self.altura) / 2

# Instanciar
#triangulo = Triangulo()    
#triangulo.base = 10  
#triangulo.altura = 20

# Resultado
#resultado = triangulo.area()
resultado = Triangulo.area(10,20)

# Imprimir resultado
print(resultado)