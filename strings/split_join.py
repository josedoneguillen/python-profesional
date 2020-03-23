# Declaracion de variable string
lenguajes = "Python; Java; Ruby; PHP; Swift; JavaScript; C#; C; C++"

# Metodo almacenado en resultado split
resultado = lenguajes.split("; ")

# Imprimir resultado
print(resultado)

# Generar string de una lista con el metodo join y almacenarlo en nuevo_string
nuevo_string = "_".join(resultado)

# Imprimir nuevo_string
print(nuevo_string)

# Texto con saltos de linea
texto = """Este es un texto
Con 
Saltos
de

linea"""

# Imprimir texto explotado por lineas
print(texto.splitlines())