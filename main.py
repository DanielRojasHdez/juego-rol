import random
import copy

# Importamos las clases y las armaduras predefinidas
from personajes import Personaje, crear_enemigo
from armaduras import armadura_ligera, armadura_media, armadura_pesada

# Importamos tus funciones de combate
from combate import ejecutar_ataque
from funciones_alternativas import leer_record, guardar_record, limpiar_pantalla, pedir_opcion


# --- PROGRAMA PRINCIPAL ---
def main():
    record = leer_record()
    heroe = Personaje("Héroe", 100, 12, False, copy.deepcopy(armadura_media))
    oleada = 1

    print("=== INICIO DEL RPG POR OLEADAS ===")

    while heroe.esta_vivo():
        
        enemigo = crear_enemigo(oleada)
        print(f"\n>>> Oleada {oleada}: Aparece un {enemigo.nombre} <<<")

        while heroe.esta_vivo() and enemigo.esta_vivo():
            # Mostrar estados
            heroe.mostrar_estado()
            if heroe.armadura: print(f"Defensa: {heroe.armadura}")
            enemigo.mostrar_estado()

            # Turno Jugador
            opcion = pedir_opcion()
            if opcion == 1:
                daño_heroe = ejecutar_ataque(heroe, enemigo)
                print(f"Hiciste {daño_heroe} de daño.")
            elif opcion == 2:
                heroe.defenderse = True
                print("Te pones en guardia...")
            else:
                heroe.curar(15)
                print("Te has curado.")

            if not enemigo.esta_vivo():
                print(f"¡{enemigo.nombre} derrotado!")
                oleada += 1
                break

            # Turno Enemigo
            daño_enemigo = ejecutar_ataque(enemigo, heroe)
            print(f"El enemigo te hizo {daño_enemigo} de daño.")
        limpiar_pantalla()
    print(f"\n--- FIN --- Oleadas superadas: {oleada-1}")
    if (oleada-1) > record:
        guardar_record(oleada-1)
        print("¡Nuevo récord guardado!")

if __name__ == "__main__":
    main()