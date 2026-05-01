class Item:
    def __init__(self, nombre, tipo, valor, descripcion):
        self.nombre = nombre
        self.tipo = tipo
        self.valor = valor
        self.descripcion = descripcion

    def aplicar(self, personaje):
        if self.tipo == "arma":
            personaje.ataque = personaje.ataque + self.valor
        elif self.tipo == "defensa":
            personaje.defensa = personaje.defensa + self.valor
        elif self.tipo == "curar":
            personaje.vida = personaje.vida + self.valor
        elif self.tipo == "daño":
            personaje.ataque = personaje.ataque + self.valor
        elif self.tipo == "ataque":
            personaje.ataque = personaje.ataque + self.valor