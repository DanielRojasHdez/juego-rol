# git add .
# git commit -m "Commit Bernat (Breve explicación)"
# git push origin rama-bernat

class Personaje:
    def __init__(self, nombre, vida, vida_max, ataque_base, defendido, armadura):
        self.nombre = nombre
        self.vida = vida_max
        self.vida_max = vida_max
        self.ataque_base = ataque_base
        self.defendido = defendido
        self.armadura = armadura

heroe = Personaje("Héroe", 100, 100, 10, False, False)
soldado = Personaje("Soldado", 35, 35, 5, None, None)
jefe = Personaje("Jefe", 50, 50, 7.5, None, None)
