
from inventario import Inventario
from item import Item
from personaje import Personaje

espada = Item("Espada", "ataque", 15, "Una espada afilada de hierro")
veneno = Item("Veneno", "ataque", 12, "Un frasco con veneno para debilitar al enemigo")
botiquin = Item("Botiquín", "vida", 14, "Un botiquín con medicamentos para curar heridas")
elixir = Item("Elixir", "vida", 11, "Un elixir que revitaliza al personaje")
escudo = Item("Escudo", "defensa", 16, "Un escudo de metal")
casco = Item("Casco", "defensa", 13, "Un casco de hierro")
ataque10 = Item("Ataque 10", "ataque", 10, "Un objeto mágico que suma 10 puntos de ataque al personaje durante un turno")

inventarioTotal = Inventario()
inventarioTotal.añadir(espada)
inventarioTotal.añadir(veneno)  
inventarioTotal.añadir(botiquin)
inventarioTotal.añadir(elixir)
inventarioTotal.añadir(escudo)
inventarioTotal.añadir(casco)
inventarioTotal.añadir(ataque10)

print('¡Bienvenidos al juego de combate!')

# Mostrar los items disponibles
print() 
print('================== ITEMS DISPONIBLES =====================')
cotador = 1
for item in inventarioTotal.items:
    print(f"{cotador}. {item.descripcion}: + {item.valor} de {item.tipo}.")
    cotador = cotador + 1
print('==========================================================')
 
# Crear personaje del jugador 1
print()
print('==== JUGADOR 1 ====')
nombre = input('Nombre: ')
vida = int(input('Vida: '))
ataque = int(input('Ataque: '))
defensa = int(input('Defensa: '))
jugador1 = Personaje(nombre, vida, ataque, defensa, 1, Inventario())

# Agregar items al inventario del jugador 1
print()
print(f'Selecciona dos items para {nombre}:')
item1 = int(input('Item 1: '))
item2 = int(input('Item 2: '))
nombre_item1 = inventarioTotal.items[item1 - 1]
nombre_item2 = inventarioTotal.items[item2 - 1]
jugador1.inventario.añadir(nombre_item1)
jugador1.inventario.añadir(nombre_item2)

# Aplicar los items al personaje
for item in jugador1.inventario.items:
    jugador1 + item

print()
print("------------------")
print(jugador1.estado())
print("------------------")

# Crear personaje del jugador 2
print()
print('==== JUGADOR 2 ====')
nombre = input('Nombre: ')
vida = int(input('Vida: '))
ataque = int(input('Ataque: '))
defensa = int(input('Defensa: '))
jugador2 = Personaje(nombre, vida, ataque, defensa, 1, Inventario())

# Agregar items al inventario del jugador 2
print()
print(f'Selecciona dos items para {nombre}:')
item1 = int(input('Item 1: '))
item2 = int(input('Item 2: '))
nombre_item1 = inventarioTotal.items[item1 - 1]
nombre_item2 = inventarioTotal.items[item2 - 1]
jugador2.inventario.añadir(nombre_item1)
jugador2.inventario.añadir(nombre_item2)

# Aplicar los items al personaje
for item in jugador2.inventario.items:
    jugador2 + item

print()
print("------------------")
print(jugador2.estado())
print("------------------")


print()
print('======= ESTADO JUGADORES CON ITEMS APLICADOS =======')
print(jugador1.estado())
print(jugador2.estado())
print('====================================================')
print()

input('Presiona Enter para comenzar la batalla...')

print()
print('================== COMIENZA LA BATALLA===================')
turno = 1
while jugador1.vivo() and jugador2.vivo() and turno <= 10:
    print('')
    print(f"> Turno {turno}:")
    # El jugador 1 ataca al jugador 2
    jugador2.vida = jugador2 - jugador1
    # El jugador 2 ataca al jugador 1
    jugador1.vida = jugador1 - jugador2
    print(jugador1.estado())
    print(jugador2.estado())
    turno = turno + 1
    print('')
    input('Presiona Enter para continuar al siguiente turno...')

print('')
print('=================== FIN DE LA PARTIDA ===================')
print('')
if jugador1.vivo() and not jugador2.vivo():
    jugador1.nivel = jugador1.nivel + 1
    print(f'¡{jugador1.nombre} ha ganado el combate!, sube a nivel {jugador1.nivel}')
elif jugador2.vivo() and not jugador1.vivo():
    jugador2.nivel = jugador2.nivel + 1
    print(f'¡{jugador2.nombre} ha ganado el combate!, ¡sube a nivel {jugador2.nivel}!')
else:
    print('¡El combate ha terminado en empate!')



