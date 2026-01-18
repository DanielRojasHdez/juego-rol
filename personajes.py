# git add .
# git commit -m "Commit Bernat (Breve explicación)"
# git push origin rama-bernat


import random

# Clases

class Personaje:
    def __init__(self, nombre, vida, vida_max, ataque_base, defenderse, armadura):
        self.nombre = nombre
        self.vida = vida
        self.vida_max = vida_max
        self.ataque_base = ataque_base
        self.defenderse = defenderse
        self.armadura = armadura

heroe = Personaje("Héroe", 100, 100, 10, False, False)
soldado = Personaje("Soldado", 35, 35, random.randint(4, 6), False, False)
jefe = Personaje("Jefe", 50, 50, random.randint(7, 9), False, False)


# print(soldado.ataque_base)
# Funciones
# Fuincion para incremento de nivel dependiendo oleada


def increment_nivel (personaje):
    incremento = 2
    incremento_vida = 5
    personaje.ataque_base += incremento
    personaje.vida_max += incremento_vida

# Incremento +2 puntos al ataque del soldado
# print(jefe.ataque_base)
# print(jefe.vida_max)
# increment_nivel(jefe)
# print(jefe.ataque_base)
# print(jefe.vida_max)
# increment_nivel(jefe)
# print(jefe.ataque_base)
# print(jefe.vida_max)


# Función de cambio de vida al ser atacado. Resta vida actual del heroe dependiendo del ataque del soldado o jefe


def newhp (personaje, ataque_base):
    personaje.vida = personaje.vida - ataque_base

    if personaje.vida < 0:
        personaje.vida = 0

# print (heroe.vida)
# print (jefe.ataque_base)
# newhp(heroe, jefe.ataque_base)
# print(heroe.vida)
# newhp(heroe, jefe.ataque_base)
# print(heroe.vida)

#Funcion para determinar si el personaje sigue vivo

def sigue_vivo (personaje):
    if personaje.vida > 0:
        return True  
    else:
        return False
    
# print (sigue_vivo(heroe))


#Funcion para curar el personaje, por ejemplo con pocion o magia de cura
def curar (personaje, cantidad):
    personaje.vida += cantidad

    if personaje.vida > personaje.vida_max:
        personaje.vida = personaje.vida_max

#Funcion para activar defensa y recibir solo un 20% de daño, se desactiva al usarse.
def defensa_on (personaje, ataque_base):
    if personaje.defenderse:
        daño = ataque_base * 0.20
        personaje.defenderse = False  # se desactiva tras usarla
    else:
        daño = ataque_base
    
    personaje.vida -= daño
    
    if personaje.vida < 0:
        personaje.vida = 0

#Funcion mensaje para mostrar vida personaje en cada turno

def estado_actual(personaje):
    print(personaje.nombre) 
    print("vida: ", personaje.vida, "/", personaje.vida_max)
    print("oleada")

#newhp(heroe, jefe.ataque_base)
#estado_actual(heroe)

# Funcion para que la opción de defenderse no se quede pillada

def debug_defensa(personaje):
    personaje.defenderse = False

# Función para determinar fallo y golpe critico

def golpe_suerte(personaje):
    suerte = random.randint(1, 100)
    if suerte < 5:
        daño = 0
    elif suerte < 95:
        daño = personaje.ataque_base
    else:
        daño = personaje.ataque_base * 2   
    return daño
    