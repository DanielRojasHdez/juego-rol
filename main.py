# main.py
import random
import copy
import os

from personajes import Personaje, increment_nivel, newhp, sigue_vivo, curar, estado_actual
from armaduras import armadura_ligera, armadura_media, armadura_pesada, reducir_daño, estado_armadura
from combate import golpe_suerte, defensa_on


# -----------------------------
# RECORD (sin base de datos)
# -----------------------------
RECORD_FILE = "record.txt"

def leer_record():
    if not os.path.exists(RECORD_FILE):
        return 0
    try:
        with open(RECORD_FILE, "r", encoding="utf-8") as f:
            return int(f.read().strip())
    except:
        return 0

def guardar_record(nuevo_record):
    with open(RECORD_FILE, "w", encoding="utf-8") as f:
        f.write(str(nuevo_record))


# -----------------------------
# MENÚ / INPUT
# -----------------------------
def pedir_opcion():
    print("\nElige acción:")
    print("1) Atacar")
    print("2) Defender")
    print("3) Curar (+15)")
    while True:
        op = input("Opción (1-3): ").strip()
        if op in ("1", "2", "3"):
            return int(op)
        print("Opción no válida. Escribe 1, 2 o 3.")


# -----------------------------
# CREAR ENEMIGO POR OLEADA
# -----------------------------
def crear_enemigo_por_oleada(oleada):
    """
    Cada 3 oleadas sale el jefe.
    Oleada 1-2: soldado
    Oleada 3: jefe
    Oleada 4-5: soldado
    Oleada 6: jefe
    ...
    """
    if oleada % 3 == 0:
        enemigo = Personaje("Jefe", 50, 50, random.randint(7, 9), False, None)
        # armadura opcional del jefe
        enemigo.armadura = copy.deepcopy(armadura_media)
    else:
        enemigo = Personaje("Soldado", 35, 35, random.randint(4, 6), False, None)
        # armadura opcional del soldado
        enemigo.armadura = copy.deepcopy(armadura_ligera)

    return enemigo


def aplicar_dificultad(enemigo, oleada):
    """
    Sube la dificultad usando increment_nivel.
    Regla simple:
    - subidas = oleada - 1
    (si se hace demasiado difícil, cambia a (oleada - 1)//2)
    """
    subidas = oleada - 1
    for _ in range(subidas):
        increment_nivel(enemigo)

    # Muy importante: si sube vida_max, ponemos la vida al máximo al crear el enemigo
    enemigo.vida = enemigo.vida_max


# -----------------------------
# ATAQUE COMPLETO (suerte -> defensa -> armadura -> vida)
# -----------------------------
def ataque_turno(atacante, defensor):
    daño = golpe_suerte(atacante)              # fallo/normal/crítico
    daño = defensa_on(defensor, daño)          # si defensor estaba defendiendo
    daño = reducir_daño(defensor.armadura, daño)  # si tiene armadura
    newhp(defensor, daño)                      # aquí se asegura vida >= 0
    return daño


# -----------------------------
# MOSTRAR INFO DE TURNO
# -----------------------------
def mostrar_estado_combate(oleada, heroe, enemigo, record):
    print("\n" + "=" * 30)
    print(f"OLEADA: {oleada}   |   RÉCORD: {record}")
    print("=" * 30)

    print("\n[HÉROE]")
    estado_actual(heroe)
    estado_armadura(heroe.armadura)

    print("\n[ENEMIGO]")
    estado_actual(enemigo)
    estado_armadura(enemigo.armadura)


# -----------------------------
# PROGRAMA PRINCIPAL
# -----------------------------
def main():
    record = leer_record()

    # Crear héroe
    heroe = Personaje("Héroe", 100, 100, 10, False, None)
    heroe.armadura = copy.deepcopy(armadura_ligera)   # cámbiala si quieres

    oleada = 1

    print("=== JUEGO DE OLEADAS ===")
    print("Cada 3 oleadas aparece el JEFE.")
    print("La dificultad sube cada oleada.\n")

    while sigue_vivo(heroe):
        # Crear enemigo según oleada y aplicar dificultad
        enemigo = crear_enemigo_por_oleada(oleada)
        aplicar_dificultad(enemigo, oleada)

        print(f"\n>>> Entra un {enemigo.nombre} (Oleada {oleada}) <<<")

        # Combate de esta oleada
        while sigue_vivo(heroe) and sigue_vivo(enemigo):
            mostrar_estado_combate(oleada, heroe, enemigo, record)

            # Turno jugador
            op = pedir_opcion()

            if op == 1:
                daño = ataque_turno(heroe, enemigo)
                print(f"\n{heroe.nombre} ataca e hizo {daño} de daño.")
            elif op == 2:
                heroe.defenderse = True
                print(f"\n{heroe.nombre} se defiende (solo para el próximo golpe).")
            else:
                curar(heroe, 15)
                print(f"\n{heroe.nombre} se cura +15.")

            # Si el enemigo murió, se pasa de oleada
            if not sigue_vivo(enemigo):
                print(f"\n✅ Has derrotado al {enemigo.nombre}.")

                # recompensa simple opcional:
                # al derrotar al jefe, curación extra
                if oleada % 3 == 0:
                    curar(heroe, 10)
                    print("🎁 Recompensa por jefe: +10 de vida.")

                oleada += 1
                break

            # Turno enemigo (IA simple: siempre ataca)
            daño = ataque_turno(enemigo, heroe)
            print(f"\n{enemigo.nombre} ataca e hizo {daño} de daño.")

        # Si el héroe murió, salir
        if not sigue_vivo(heroe):
            break

    # FIN
    oleada_superada = oleada - 1
    print("\n=== FIN DE PARTIDA ===")
    print(f"Has llegado hasta la oleada: {oleada_superada}")

    if oleada_superada > record:
        print("🏆 ¡Nuevo récord!")
        guardar_record(oleada_superada)
    else:
        print(f"Récord actual: {record}")


if __name__ == "__main__":
    main()
