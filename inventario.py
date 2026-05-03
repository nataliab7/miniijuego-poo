class Inventario:
    def __init__(self):
        self.items = []

    def añadir(self, item):
        self.items.append(item)

    def eliminar(self, item):
        self.items.remove(item)

    def mostrar(self):
        for item in self.items:
            print(f"{item.nombre}: {item.descripcion}") 
            