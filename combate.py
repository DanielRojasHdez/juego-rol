import random

# Esta funcion decide el tipo de ataque realizado, para ello hemos implementado un sistema aleatorio. 
def golpe_suerte(personaje):
    # Determina si el ataque es normal, crítico o fallo.
    suerte = random.randint(1, 100)
    # Habrá un 5% de fallo de ataque
    if suerte < 5:
        print(f"¡{personaje.nombre} falló el ataque!")
        return 0
    # Un 90% de ataque normal
    elif suerte < 95:
        print(f"Ataque normal de {personaje.nombre}.")
        return personaje.ataque_base
    # Y un 5% de golpe crítico
    else:
        print(f"¡GOLPE CRÍTICO de {personaje.nombre}!")
        return personaje.ataque_base * 2

# Esta funcion determina si el defensor activo un "escudo" en el turno anterior, de esta manera el daño se reduce gracias a la proteccion.
def defensa_on(personaje, daño):
    # Si el personaje está defendiendo, reduce el daño al 20%.
    if personaje.defenderse:
        daño_final = int(daño * 0.8)
        # Reseteo del atributo 'defenderse' a false.
        personaje.defenderse = False 
        print(f"¡{personaje.nombre} amortiguó el golpe con su defensa!")
        return daño_final
    # Si el personaje no está defendiendo, recibe el 100% del daño.
    return daño


# --- EL CORAZÓN DEL COMBATE ---
def ejecutar_ataque(atacante, defensor):
    # Calculamos daño base (suerte)
    daño_base = golpe_suerte(atacante)
    
    if daño_base > 0:
        # Reducción del daño por activar la defensa, comprobando si el atributo 'defenderse' del defensor es true(está activo)
        daño_tras_defensa = defensa_on(defensor, daño_base)
        
        # Reducción por armadura
        if defensor.armadura:
            daño_final = defensor.armadura.reducir_daño(daño_tras_defensa)
        
        # Aplicar daño a la vida del defensor
        defensor.recibir_daño(daño_final)
        # Si el daño base es mayor a 0, devolvemos el daño final 
        return daño_final
    
    # Si el daño base es 0, es decir, 'fallo', devolvemos 0
    return 0