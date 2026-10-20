"""Práctica complementaria 3-7: seguir el recorrido de varios assert."""

jugador = "Luna"
monedas = 7
vidas = 2
nivel = 3
inventario = ["llave", "mapa", "pocion"]

puntaje = monedas * 10 + nivel * 5

assert jugador == "Luna", "El nombre del jugador no coincide"
assert puntaje == 85, "El puntaje no coincide"
assert monedas + vidas * nivel == 13, "La cuenta de la segunda prueba no coincide"
assert len(inventario) + vidas == 5, "La cantidad total no coincide"
assert puntaje - monedas * 10 == 10, "El bonus no coincide"
assert nivel * vidas == 6, "El producto de nivel y vidas no coincide"

print("Todas las comprobaciones pasaron")

