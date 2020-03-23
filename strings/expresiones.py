# Declaracion de variable string
curso = "Python"
version= "3"

# Remplazar valores dentro del string por posicion y almacenarlo en resultado
resultado = "Curso de %s %s" %(curso, version)

# Imprimir resultado
print(resultado)

# Remplazar valores dentro del string con format y almacenarlo en resultado
#resultado = "Curso de {curso} {version}".format(curso, version)
resultado = "Curso de {a} {b}".format(a=curso, b=version)

# Imprimir resultado
print(resultado)