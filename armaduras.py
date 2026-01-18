class Armadura:
    def __init__(self, tipo, nombre, reduccion, durabilidad_max):
        self.tipo = tipo
        self.nombre = nombre
        self.reduccion = reduccion
        self.durabilidad_max = durabilidad_max
        self.durabilidad = durabilidad_max

    def reparar(self, cantidad):
        self.durabilidad += cantidad
        if self.durabilidad > self.durabilidad_max:
            self.durabilidad = self.durabilidad_max

# --- Funciones para que usen los demás ---

def aplicar_armadura(defensor, daño):
    arm = defensor.armadura
    if arm and arm.durabilidad > 0:
        daño_final = daño - arm.reduccion
        arm.durabilidad -= 1  # Pierde durabilidad al recibir golpe
        if daño_final < 0: daño_final = 0
        return daño_final
    return daño

def reparar_armadura(personaje):
    if personaje.kits_reparacion > 0:
        personaje.armadura.reparar(15)
        personaje.kits_reparacion -= 1
        print(f"¡{personaje.nombre} reparó su armadura!")
    else:
        print("¡No te quedan kits!")

def resumen_armadura(personaje):
    arm = personaje.armadura
    if arm:
        return f"Armadura: {arm.nombre} ({arm.durabilidad}/{arm.durabilidad_max})"
    return "Sin armadura"