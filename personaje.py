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
        # Muestro en pantalla el estado del personaje, incluyendo su inventario
        nombres_items = []
        for item in self.inventario.items:
            nombres_items.append(item.nombre)
        r = f"{self.nombre}: vida = {self.vida} | ataque = {self.ataque} | defensa = {self.defensa} | nivel = {self.nivel} | inventario = {nombres_items}"
        return r
       
    def vivo(self):
        # El personaje está vivo si su vida es mayor a 0.
        r = (self.vida > 0)
        return r
    
    def __sub__(self, atacante):
        # El atacante ataca al defensor, y el defensor pierde vida si se consume toda su defensa.
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
        # Aplicar el efecto del item al personaje, es decir, suma los puntos del item al atributo correspondiente del personaje.
        if item.tipo == "ataque":
            self.ataque = self.ataque + item.valor
        elif item.tipo == "defensa":
            self.defensa = self.defensa + item.valor
        elif item.tipo == "vida":
            self.vida = self.vida + item.valor
        return self
    
    def curarse(self, puntos):
        # Al personaje se le aumenta la vida.
        self.vida = self.vida + puntos
        return self