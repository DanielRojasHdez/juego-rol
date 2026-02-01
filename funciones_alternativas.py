import os
import personajes
from armaduras import armadura_ligera, armadura_media, armadura_pesada
import copy

def mejorar_armadura(personaje):
    # Si no tiene armadura (por seguridad)
    if not personaje.armadura:
        personaje.armadura = copy.deepcopy(armadura_ligera)
        print("Te equipas una armadura ligera nueva.")
        return

    tipo_actual = personaje.armadura.tipo

    if tipo_actual == "ligera":
        personaje.armadura = copy.deepcopy(armadura_media)
        print("🛡️  Tu armadura ha mejorado a ARMADURA MEDIA.")
    elif tipo_actual == "media":
        personaje.armadura = copy.deepcopy(armadura_pesada)
        print("🛡️  Tu armadura ha mejorado a ARMADURA PESADA.")
    else:
        print("❌  Ya llevas la mejor armadura posible.")
        return
    
# --- LÓGICA DE RÉCORD ---
RECORD_FILE = "record.txt"

# Función para leer el archivo record
def leer_record():
    if not os.path.exists(RECORD_FILE): return 0
    try:
        with open(RECORD_FILE, "r") as f: return int(f.read().strip())
    except: return 0

# Funcion para guardar el nuevo record
def guardar_record(nuevo):
    with open(RECORD_FILE, "w") as f: f.write(str(nuevo))

# Función para limpiar la terminal al derrotar una oleada
def limpiar_pantalla():
    # 'nt' es para Windows, 'posix' para Mac y Linux
    os.system('cls' if os.name == 'nt' else 'clear')

# --- FUNCIONES DE APOYO ---
def pedir_opcion():
    while True:
        print("1) Atacar | 2) Defender | 3) Curar (+15) | 4) Reparar Armadura (+3)")
        opcion = input("Elige acción: ").strip()
        if opcion in ("1", "2", "3", "4"): return int(opcion)
        print("Opción no válida.")


# TIENDA
def tienda(personaje, opcion):
    if opcion == "1" and personaje.oro >= 35:
        personaje.comprar_curas(1)
        personaje.oro -= 35
    elif opcion == "2" and personaje.oro >= 60:
        personaje.comprar_curas(2)
        personaje.oro -= 60
    elif opcion == "3" and personaje.oro >= 20:
        personaje.comprar_reparaciones(1)
        personaje.oro -= 20
    elif opcion == "4" and personaje.oro >= 35:
        personaje.comprar_reparaciones(2)
        personaje.oro -= 35
    else:
        print("Opción no válida, revisa la cantidad de oro que tienes y elige bien entre las opciones válidas.")
    

# Cátalogo de la tienda
def catalogo():
    print("-- CURAS -- ")
    print("1 Cura: 35 oro")
    print("2 Curas: 60 oro\n")
    print("-- REPARACIONES --")
    print("1 Reparación de armadura: 20 oro")
    print("2 Reparaciones de armadura: 35 oro\n")