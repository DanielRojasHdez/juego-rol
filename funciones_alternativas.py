import os

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
        print("\n1) Atacar | 2) Defender | 3) Curar (+15)")
        op = input("Elige acción: ").strip()
        if op in ("1", "2", "3"): return int(op)
        print("Opción no válida.")