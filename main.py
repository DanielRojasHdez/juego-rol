import random
import copy

# Importamos las clases y las armaduras predefinidas
from personajes import Heroe, Enemigo, crear_enemigo
from armaduras import armadura_ligera, armadura_media, armadura_pesada

# Importamos tus funciones de combate
from combate import ejecutar_ataque
from funciones_alternativas import leer_record, guardar_record, limpiar_pantalla, pedir_opcion, tienda, catalogo


# --- PROGRAMA PRINCIPAL ---
def main():
    record = leer_record()
    heroe = Heroe("Héroe", 100, 12, copy.deepcopy(armadura_media))
    oleada = 1

    print("\n======= INICIO DEL RPG POR OLEADAS =======")

    while heroe.esta_vivo():
    
        enemigo = crear_enemigo(oleada)
        print(f"\n>>> Oleada {oleada}: Aparece un {enemigo.nombre} <<<\n")

        while heroe.esta_vivo() and enemigo.esta_vivo():
            # Mostrar estados
            print("Estadísticas Héroe:")
            heroe.mostrar_estado()
            print()
            # if heroe.armadura: print(f"Defensa: {heroe.armadura}")
            print("Estadísticas Enemigo:")
            enemigo.mostrar_estado()

            # Turno Jugador
            opcion = pedir_opcion()
            print("\n--------------- ESTADÍSTICAS DE LA RONDA ---------------")
            print("Turno Héroe:")
            if opcion == 1:
                daño_heroe = ejecutar_ataque(heroe, enemigo)
                print(f"Hiciste {daño_heroe} de daño.\n")
            elif opcion == 2:
                heroe.defenderse = True
                print("Te pones en guardia...\n")
            elif opcion == 3:
                if heroe.curas_disponibles > 0:
                    heroe.curar(15)
                    heroe.curas_disponibles -= 1
                    print(f"Te has curado. Te quedan {heroe.curas_disponibles} disponibles.\n")
                else:
                    print("Has llegado al límite de curas.\n")
                    continue
            elif opcion == 4:
                if heroe.reparaciones_disponibles > 0:
                    heroe.armadura.reparar(3)
                    heroe.reparaciones_disponibles -= 1
                    print(f"Has reparado tu armadura. Te quedan {heroe.reparaciones_disponibles} disponibles\n")
                else:
                    print("Has llegado al límite de reparaciones.\n")
                    continue
            else:
                print("\n******** BIENVENIDO A LA TIENDA ********\n")
                print("- Pulsa 1 para comprar 1 cura")
                print("- Pulsa 2 para comprar 2 curas")
                print("- Pulsa 3 para comprar 1 reparación de armadura")
                print("- Pulsa 4 para comprar 2 reparaciones de armadura\n")
                catalogo()
                opcion = input("¿Que deseas comprar?: ")
                tienda(heroe, opcion)
                continue

            if not enemigo.esta_vivo():
                print(f"¡{enemigo.nombre} derrotado!")
                oleada += 1
                heroe.increment_nivel()
                heroe.aumento_oro(enemigo)
                break

            # Turno Enemigo
            print("Turno Enemigo:")
            daño_enemigo = ejecutar_ataque(enemigo, heroe)
            print(f"El enemigo te hizo {daño_enemigo} de daño.\n")

            # Separador de turnos
            print("-------------------- NUEVO TURNO --------------------")

        # Limpiamos la terminal
        limpiar_pantalla()
    print(f"\n--- FIN --- Oleadas superadas: {oleada-1}")
    if (oleada-1) > record:
        guardar_record(oleada-1)
        print("¡Nuevo récord guardado!")

if __name__ == "__main__":
    main()