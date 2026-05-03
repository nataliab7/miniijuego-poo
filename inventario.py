class Inventario:
    def __init__(self):
        self.items = []

    def añadir(self, item):
        self.items.append(item)

    def mostrar(self):
        contador = 0
        for item in self.items:
            print(f"{contador}. {item.descripcion}: +{item.valor} de {item.tipo}.")
            contador = contador + 1