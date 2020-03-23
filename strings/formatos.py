# Declaracion de variable tipo string
texto = " Curso de Python 3 "

# Capitalizar el texto y almacenarlo en resultado
resultado = texto.capitalize()

# Imprimir resultado
print(resultado)

# Mayusculas a minuscula en el texto y almacenarlo en resultado
resultado = texto.swapcase()

# Imprimir resultado
print(resultado)

# Todo a mayusculas en el texto y almacenarlo en resultado
resultado = texto.upper()

# Imprimir resultado
print(resultado)

# Todo a minuscula en el texto y almacenarlo en resultado
resultado = texto.lower()

# Imprimir resultado
print(resultado)

# Saber si es minuscula o mayuscula
print(resultado.islower())
print(resultado.isupper())

# Metodo title
print(resultado.title())

# Metodo replace (en el tercer valor se puede especificar cuantas veces remplazar)
texto_remplazado = texto.replace("Python", "Ruby")
print(texto_remplazado)

# Metodo strip es como el metodo trim en otros lenguajes para elminar el espacio al principio y al final
texto_remplazado = texto.strip()
print(texto_remplazado)