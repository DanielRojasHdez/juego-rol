class Armadura:
    def __init__(self, tipo, nombre, reduccion, durabilidad_max):
        self.tipo = tipo
        self.nombre = nombre
        self.reduccion = reduccion
        self.durabilidad_max = durabilidad_max
        self.durabilidad = durabilidad_max

armadura_ligera = Armadura("ligera", "Armadura ligera", 2, 50)
armadura_media = Armadura("media", "Armadura media", 4, 40)
armadura_pesada = Armadura("pesada", "Armadura pesada", 6, 30)

# Funcion para aplicar reduccion de daño de la armadura y gasta durabilidad si protege
def reducir_daño(armadura, daño):
    if armadura is None:
        return daño
    if armadura.durabilidad <= 0:
        return daño
    daño_final = daño - armadura.reduccion
    if daño_final < 0:
        daño_final = 0
    perder_durabilidad(armadura)
    return daño_final

# Funcion que Reduce la durabilidad de la armadura en 1.
def perder_durabilidad(armadura):
    if armadura.durabilidad > 0:
        armadura.durabilidad -= 1

# Funcion para reparar la armadura sin superar el máximo.
def reparar_armadura(armadura, cantidad):
    if armadura is None:
        return

    armadura.durabilidad += cantidad

    if armadura.durabilidad > armadura.durabilidad_max:
        armadura.durabilidad = armadura.durabilidad_max

# Funcion para saber si la armadura esta rota. Devuelve true
def esta_rota(armadura):
    if armadura is None:
        return True

    return armadura.durabilidad == 0

# Funcion para mostrar el estado de la armadura
def estado_armadura(armadura):
    if armadura is None:
        print("Sin armadura")
    else:
        print(f"{armadura.nombre} ({armadura.durabilidad}/{armadura.durabilidad_max})")