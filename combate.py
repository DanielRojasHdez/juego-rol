import random
import armaduras

def activar_defensa(personaje):
    personaje.defendiendo = True
    print(f"{personaje.nombre} se pone en guardia.")

def calcular_daño_final(atacante, defensor):
    # 1. Suerte (Crítico/Fallo)
    suerte = random.randint(1, 100)
    daño = atacante.ataque_base + random.randint(-2, 2)
    mensaje_extra = ""

    if suerte <= 10:  # 10% Fallo
        return 0, "¡Falló el ataque!"
    elif suerte >= 90: # 10% Crítico
        daño *= 2
        mensaje_extra = "¡GOLPE CRÍTICO! "

    # 2. Defensa (si el defensor activó defensa el turno anterior)
    if defensor.defendiendo:
        daño = int(daño * 0.3)  # Reduce al 30% del daño
        defensor.defendiendo = False # Se gasta la defensa
        mensaje_extra += "(Defendido) "

    # 3. Armadura (llamamos al archivo de tu compañero)
    daño_tras_armadura = armaduras.aplicar_armadura(defensor, daño)
    
    return daño_tras_armadura, mensaje_extra

def hacer_ataque(atacante, defensor):
    daño, efecto = calcular_daño_final(atacante, defensor)
    defensor.recibir_daño(daño)
    
    return f"{efecto}{atacante.nombre} ataca a {defensor.nombre} haciendo {daño} de daño."