# git add .
# git commit -m "Commit Bernat (Breve explicación)"
# git push origin rama-bernat
import random
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
    
# Funcion para que la opción de defenderse no se quede pillada
def debug_defensa(personaje):
    personaje.defenderse = False

#Funcion para activar defensa y recibir solo un 20% de daño, se desactiva al usarse.
def defensa_on(personaje, daño):
    if personaje.defenderse:
        daño = int(daño * 0.20)
        personaje.defenderse = False

    return daño