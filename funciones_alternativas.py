import os
import personajes

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
        print("\n1) Atacar | 2) Defender | 3) Curar (+15) | 4) Reparar Armadura | 5) Tienda")
        opcion = input("Elige acción: ").strip()
        if opcion in ("1", "2", "3", "4", "5"): return int(opcion)
        print("Opción no válida.")


# TIENDA
def tienda(personaje, opcion):
    if opcion == "1" and personaje.oro >= 20:
        personaje.comprar_curas(1)
        personaje.oro -= 20
    elif opcion == "2" and personaje.oro >= 30:
        personaje.comprar_curas(2)
        personaje.oro -= 30
    elif opcion == "3" and personaje.oro >= 5:
        personaje.comprar_reparaciones(1)
        personaje.oro -= 5
    elif opcion == "4" and personaje.oro >= 8:
        personaje.comprar_reparaciones(2)
        personaje.oro -= 8
    else:
        print("Opción no válida")
    



def catalogo():
    print("1 cura: 20 oro")
    print("2 curas: 30 oro")
    print("1 reparación de armadura: 5 oro")
    print("2 reparaciones de armadura: 8 oro")
