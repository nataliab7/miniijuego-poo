# Mini Juego de Combate en Python

Pequeño proyecto de programación orientada a objetos que simula un combate entre dos personajes.

## Estructura del proyecto

- `main.py`: Lógica principal del juego, creación de personajes, selección de ítems y bucle de combate.
- `personaje.py`: Clase `Personaje` con atributos de vida, ataque, defensa, nivel e inventario.
- `item.py`: Clase `Item` que define los objetos disponibles y su efecto en el personaje.
- `inventario.py`: Clase `Inventario` para gestionar la lista de ítems de cada personaje.

## Cómo ejecutar

1. Abre una terminal en la carpeta del proyecto.
2. Ejecuta:

```bash
python main.py
```

3. Sigue las instrucciones en pantalla para crear los personajes y seleccionar los ítems.

## Funcionamiento básico

- El juego muestra una lista de ítems disponibles.
- Cada jugador ingresa nombre, vida, ataque y defensa.
- Cada jugador elige dos ítems.
- Los ítems se aplican al personaje para modificar sus estadísticas.
- El combate avanza por turnos hasta que uno de los personajes quede sin vida o se alcance el turno 10.

## Requisitos

- Python 3.x

## Notas

- El daño se calcula usando primero la defensa y luego la vida restante.
- El inventario almacena objetos `Item` para poder aplicar sus efectos correctamente.
