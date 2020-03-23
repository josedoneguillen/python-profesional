
# Declarar variable global
animal = "Leon"

# Definir funcion
def mostrar_animal() :
  # Definicion de variable local
  # animal = "Ballena"

  # Hacer uso de la palabra reservada global para acceder a la palabra global animal
  global animal 
  animal = "Ballena"
  print(animal)

# LLamar funcion
mostrar_animal()

# Imprimir la variable global animal
print(animal)