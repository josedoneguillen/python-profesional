# Solicitar al usuario su nombre
print("Escriba su nombre:")

# Declarar una nueva variable llamada nombre con la entrada del usuario
nombre = input()

# Solicitar al usuario su edad
print("Escriba su edad:")

# Declarar una nueva variable llamada edad con la entrada del usuario
edad = int(input())

# Solicitar al usuario su peso
print("Escriba su peso:")

# Declarar una nueva variable llamada peso con la entrada del usuario
peso = float(input())

# Solicitar al usuario su autorizacion
print("Esta autorizado? (si / no)")

# Declarar una nueva variable llamada autorizado con la entrada del usuario condicionada
autorizado = input() == "si"

# Saludar al usuario
print("Hola, ", nombre)
print("Su edad es: ", edad)
print("su peso es: ", peso)
print("autorizado? : ", autorizado)