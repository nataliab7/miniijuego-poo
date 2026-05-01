class Personaje:
    def __init__(self, nombre, vida, ataque, defensa, nivel, inventario):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.defensa = defensa
        self.nivel = nivel
        self.inventario = inventario

    def estado(self):
        item_info = ""
        for item in self.inventario:
            item_info = item_info + f"{item.nombre} "
        r = f"{self.nombre} tiene {self.vida} puntos de vida, {self.ataque} puntos de ataque, {self.defensa} puntos de defensa y está en el nivel {self.nivel} y tiene los siguientes objetos en su inventario: {item_info}."
        return r
       
    def vivo(self):
        r = (self.vida > 0)
        return r
    
    def __sub__(self, atacante):
        dano = atacante.ataque - self.defensa
        r = self.vida - dano
        return r