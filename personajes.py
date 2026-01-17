# git add .
# git commit -m "Commit Bernat (Breve explicación)"
# git push origin rama-bernat


import random

# Clases

class Personaje:
    def __init__(self, nombre, vida, vida_max, ataque_base, defendido, armadura):
        self.nombre = nombre
        self.vida = vida_max
        self.vida_max = vida_max
        self.ataque_base = ataque_base
        self.defendido = defendido
        self.armadura = armadura

heroe = Personaje("Héroe", 100, 100, 10, False, False)
soldado = Personaje("Soldado", 35, 35, random.randint(4, 6), None, None)
jefe = Personaje("Jefe", 50, 50, random.randint(7, 8), None, None)


# print(soldado.ataque_base)
# Funciones
# Fuincion para incremento de nivel dependiendo oleada


def increment_nivel (Personaje):
    incremento = 2
    Personaje.ataque_base += incremento

# Incremento +2 puntos al ataque del soldado
# print(jefe.ataque_base)
# increment_nivel(jefe)
# print(jefe.ataque_base)


# Función de cambio de vida al ser atacado. Resta vida actual del heroe dependiendo del ataque del soldado o jefe


def newhp (Personaje, daño):
    Personaje.vida = Personaje.vida - daño

    if Personaje.vida < 0:
        Personaje.vida = 0

# print (heroe.vida)
# print (jefe.ataque_base)
# newhp(heroe, jefe.ataque_base)
# print(heroe.vida)
# newhp(heroe, jefe.ataque_base)
# print(heroe.vida)

#Funcion para determinar si el personaje sigue vivo

def sigue_vivo (Personaje):
    if Personaje.vida > 0:
        return True  
    else:
        return False
    
# print (sigue_vivo(heroe))