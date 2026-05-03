from inventario import Inventario

class Personaje:
    def __init__(self, nombre, vida, ataque, defensa, nivel, inventario):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.defensa = defensa
        self.nivel = nivel
        self.inventario = Inventario()

    def estado(self):
        nombres_items = []
        for item in self.inventario.items:
            nombres_items.append(item.nombre)
        r = f"{self.nombre}: vida = {self.vida} | ataque = {self.ataque} | defensa = {self.defensa} | nivel = {self.nivel} | inventario = {nombres_items}"
        return r
       
    def vivo(self):
        r = (self.vida > 0)
        return r
    
    def __sub__(self, atacante):
        ataque_restante = atacante.ataque
        if ataque_restante <= self.defensa:
            self.defensa = self.defensa - ataque_restante
            ataque_restante = 0
        else:
            ataque_restante = ataque_restante - self.defensa
            self.defensa = 0
        if ataque_restante > 0:
            self.vida = self.vida - ataque_restante
        return self.vida
    
    def __add__(self, item):
        # item.aplicar(self)
        if item.tipo == "ataque":
            self.ataque = self.ataque + item.valor
        elif item.tipo == "defensa":
            self.defensa = self.defensa + item.valor
        elif item.tipo == "vida":
            self.vida = self.vida + item.valor
        return self