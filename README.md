## Temática del juego

Juego de combate por turnos donde dos personajes luchan usando objetos y teniendo en cuenta sus atributos de vida, ataque y defensa.

## clases creadas

- `Personaje`: representa a un luchador con `vida`, `ataque`, `defensa`, `nivel` e `inventario`.
- `Item`: define un objeto con `nombre`, `tipo`, `valor` y `descripción`.
- `Inventario`: almacena los objetos de un personaje y permite añadir ítems. También se utiliza para tener un inventario total con todos los ítems disponibles.

## métodos dunder utilizados

- `Personaje.__init__`: inicializa los atributos del personaje.
- `Item.__init__`: inicializa el nombre, tipo, valor y descripción del objeto.
- `Inventario.__init__`: crea la lista de ítems vacía para el inventario.
- `Personaje.__sub__`: permite calcular el daño recibido cuando un personaje es atacado.
- `Personaje.__add__`: aplica los efectos de un `Item` al personaje.

## funcionamiento general de la partida

1. Se muestran los objetos disponibles para elegir.
2. Cada jugador ingresa nombre y distribuye puntos entre vida, ataque y defensa.
3. Cada jugador selecciona dos ítems para su inventario.
4. Se aplican los efectos de los ítems a los personajes.
5. El combate avanza por turnos, restando primero defensa y después vida al recibir daño.
6. Gana el jugador que quede con vida, es decir, que la vida sea mayor a cero cuando el otro muere o después de 10 turnos.

## posibles ampliaciones para el proyecto final.

- Añadir un mapa en el que los personajes se puedan mover.
- Nuevos objetos.
- Ampliaciones de personajes en función del nivel.
- Habilidades especiales.
- Interfaz gráfica.
- Guardar el progreso del jugador o distintos personajes en archivos.
- Añadir más tipos de ítems.

