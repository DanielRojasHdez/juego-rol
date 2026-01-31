import random
import copy

# Importamos las clases y las armaduras predefinidas
from personajes import Heroe, Enemigo, crear_enemigo, asignar_armadura
from armaduras import armadura_ligera, armadura_media, armadura_pesada

# Importamos tus funciones de combate
from combate import ejecutar_ataque
from funciones_alternativas import leer_record, guardar_record, limpiar_pantalla, pedir_opcion, tienda, catalogo


# --- PROGRAMA PRINCIPAL ---
def main():
    record = leer_record()
    armadura_heroe = asignar_armadura()
    heroe = Heroe("Héroe", 100, 12, copy.deepcopy(armadura_heroe))
    oleada = 1

    print("\n======= INICIO DEL RPG POR OLEADAS =======\n")

    while heroe.esta_vivo():
    
        enemigo = crear_enemigo(oleada)
        heroe.curas_combate = 0
        heroe.reparaciones_combate = 0
        print(f"********** Record actual: {record} **********")
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
                if heroe.curas_disponibles > 0 and heroe.curas_combate < 2:
                    heroe.curar(15)
                    heroe.curas_disponibles -= 1
                    heroe.curas_combate += 1
                    print(f"Te has curado ({heroe.curas_combate}/2 este combate).\n")
                    continue
                else:
                    print("No puedes curarte más en este combate.\n")
                    continue
            elif opcion == 4:
                if heroe.reparaciones_disponibles > 0 and heroe.reparaciones_combate < 1:
                    heroe.armadura.reparar(3)
                    heroe.reparaciones_disponibles -= 1
                    heroe.reparaciones_combate += 1
                    print("Has reparado tu armadura (1/1 este combate).\n")
                    continue
                else:
                    print("No puedes reparar más la armadura en este combate.\n")
                    continue
            else:
                while True:
                    print("\n******** BIENVENIDO A LA TIENDA ********\n")
                    print(f"🪙  Oro disponible: {heroe.oro}\n")

                    print("- Pulsa 0 para salir sin comprar")
                    print("- Pulsa 1 para comprar 1 cura")
                    print("- Pulsa 2 para comprar 2 curas")
                    print("- Pulsa 3 para comprar 1 reparación de armadura")
                    print("- Pulsa 4 para comprar 2 reparaciones de armadura\n")

                    catalogo()

                    opcion_tienda = input("¿Qué deseas comprar?: ").strip()

                    # Validación de entrada
                    if opcion_tienda not in ("0", "1", "2", "3", "4"):
                        print("Opción no válida. Elige un número entre 0 y 4.\n")
                        continue

                    # Salir de la tienda
                    if opcion_tienda == "0":
                        print("Sales de la tienda sin comprar nada.\n")
                        break

                    tienda(heroe, opcion_tienda)
                continue


            if not enemigo.esta_vivo():
                print(f"¡{enemigo.nombre} derrotado!")
                heroe.aumento_oro(enemigo, oleada)

                # TIENDA SOLO TRAS JEFE
                if enemigo.nombre == "Jefe Orco":
                    while True:
                        print("\n🛒 MERCADER TRAS LA BATALLA 🛒\n")
                        print(f"🪙   Oro disponible: {heroe.oro}\n")
                        print("0) Salir")
                        print("1) 1 Cura -> 20 oro")
                        print("2) 2 Curas -> 30 oro")
                        print("3) 1 Reparación -> 5 oro")
                        print("4) 2 Reparaciones -> 8 oro\n")

                        opcion_tienda = input("Elige opción: ").strip()

                        if opcion_tienda not in ("0", "1", "2", "3", "4"):
                            print("Opción no válida.\n")
                            continue

                        if opcion_tienda == "0":
                            break

                        tienda(heroe, opcion_tienda)

                oleada += 1
                heroe.increment_nivel()
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