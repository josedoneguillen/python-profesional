# Definir funcion se puede usar nonlocal para modificar variables dentro de una funcion
def comenzar_playlist(lista) :
  def reproducir():
    for val in lista:
      print(val)
  reproducir()

# Definir lista
lista = ["Track 1", "Track 2", "Track 3", "Track 4"]

# Llamar funcion y pasar lista
comenzar_playlist(lista)