class Inventario:
    def __init__(self):
        self.items = []

    def añadir(self, item):
        self.items.append(item)

    # Método para mostrar los items disponibles en el inventario
    def mostrar(self):
        contador = 0
        for item in self.items:
            print(f"{contador}. {item.descripcion}: +{item.valor} de {item.tipo}.")
            contador = contador + 1

    def eliminar(self, item):
        self.items.remove(item)

    # Método para consultar los atributos de un item por su nombre
    def consultar(self, nombre):
        for i in self.items:
            if i.nombre == nombre:
                return f'Item: {i.nombre}, Tipo: {i.tipo}, Valor: {i.valor}, Descripción: {i.descripcion}'
        return None
    
    # Método para verificar si un item existe en el inventario por su nombre
    def existe(self, nombre):
        for i in self.items:
            if i.nombre == nombre:
                return True
        return False