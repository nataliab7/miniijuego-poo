
from item import Item
from personaje import Personaje

espada = Item("Espada", "arma", 20, "Una espada afilada de hierro")
botiquin = Item("Botiquín", "curar", 50, "Un botiquín con medicamentos para curar heridas")
escudo = Item("Escudo", "defensa", 15, "Un escudo de metal")
veneno = Item("Veneno", "daño", 10, "Un frasco con veneno para debilitar al enemigo")
ataque10 = Item("Ataque 10", "ataque", 10, "Un objeto mágico que suma 10 puntos de ataque al personaje durante un turno")


jugador1 = Personaje("Juan", 100, 30, 20, 1, []) # Nombre, vida, ataque, defensa, nivel, inventario
jugador2 = Personaje("María", 100, 25, 15, 1, [])

print('¡Bienvenidos al juego de combate!')
print('Los jugadores son:')
print(jugador1.estado())
print(jugador2.estado())

jugador1.inventario.append(escudo)
jugador1.inventario.append(botiquin)
jugador2.inventario.append(veneno)
jugador2.inventario.append(espada)

for item in jugador1.inventario:
    item.aplicar(jugador1)
for item2 in jugador2.inventario:
    item2.aplicar(jugador2)

print('Los jugadores se han equipado:')
print(jugador1.estado())
print(jugador2.estado())

turno = 1
while jugador1.vivo() and jugador2.vivo() and turno <= 10:
    print('')
    print(f"Turno {turno}:")
    jugador2.vida = jugador2 - jugador1
    jugador1.vida = jugador1 - jugador2
    print(jugador1.estado())
    print(jugador2.estado())
    turno = turno + 1

