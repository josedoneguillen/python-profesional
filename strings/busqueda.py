# Declaracion de variable string
mensaje = "Este es un texto un poco grande en cuanto a longitud de caracteres se refiere"

# Buscar con count y almacernar la cantidad en resultado
resultado = mensaje.count("texto")

# Imprimir mensaje
print(resultado)

# Buscar con in y almacernar la cantidad en resultado
#resultado = "texto" not in mensaje
resultado = "texto" in mensaje

# Imprimir mensaje
print(resultado)

# Buscar con find y almacernar la cantidad en resultado
resultado = mensaje.find("texto")

# Sacar la palabra texto
resultado = mensaje[resultado: resultado + len("texto")]

# Imprimir mensaje
print(resultado)

# Buscar con startwith y almacernar la cantidad en resultado
resultado = mensaje.startswith("Este")

# Imprimir mensaje
print(resultado)

# Buscar con endswith y almacernar la cantidad en resultado
resultado = mensaje.endswith("e")

# Imprimir mensaje
print(resultado)