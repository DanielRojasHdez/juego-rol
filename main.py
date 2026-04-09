import random
import copy

# Importamos las clases y las armaduras predefinidas
from personajes import Heroe, Enemigo, crear_enemigo, mejorar_armadura
from armaduras import armadura_ligera, armadura_media, armadura_pesada

# Importamos tus funciones de combate
from combate import ejecutar_ataque
from funciones_alternativas import leer_record, guardar_record, limpiar_pantalla, pedir_opcion, tienda


# --- PROGRAMA PRINCIPAL ---
def main():
    record = leer_record()
    # armadura_heroe = asignar_armadura()
    heroe = Heroe("Héroe", 100, 12, copy.deepcopy(armadura_ligera))
    oleada = 1

    print("\n======= INICIO DEL RPG POR OLEADAS =======\n")
    turno = 1
    while heroe.esta_vivo():
    
        enemigo = crear_enemigo(oleada)

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
            print()
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
                turnos_restantes = 4 - (turno - heroe.ultimo_turno_cura)

                if heroe.curas_disponibles == 0:
                    print("No hay curas disponibles.\n")
                    continue

                elif heroe.curas_disponibles > 0 and turno - heroe.ultimo_turno_cura >= 4:
                    heroe.curar(15)
                    heroe.curas_disponibles -= 1
                    heroe.ultimo_turno_cura = turno
                    print("Te has curado (+15). Próxima cura disponible en 4 turnos.\n")
                    continue

                else:
                    print(f"La cura está en enfriamiento ({turnos_restantes} turnos restantes).\n")
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

            if not enemigo.esta_vivo():
                print(f"¡{enemigo.nombre} derrotado!")
                heroe.aumento_oro(enemigo, oleada)

                if enemigo.nombre == "Jefe Orco":
                    while True:
                        print("\n🛒 MERCADER TRAS LA BATALLA 🛒\n")
                        print(f"🪙   Oro disponible: {heroe.oro}\n")

                        print("0) Salir")
                        print("1) 1 Cura -> 35 oro")
                        print("2) 2 Curas -> 60 oro")
                        print("3) 1 Reparación -> 20 oro")
                        print("4) 2 Reparaciones -> 35 oro")
                        print("5) Mejora de Armadura -> 100 oro\n")

                        opcion_tienda = input("Elige opción: ").strip()

                        # Validación
                        if opcion_tienda not in ("0", "1", "2", "3", "4", "5"):
                            print("❌ Opción no válida.\n")
                            continue

                        # Salir de la tienda
                        if opcion_tienda == "0":
                            print("Sales de la tienda.\n")
                            break

                        # Mejora de armadura
                        if opcion_tienda == "5":
                            if heroe.oro < 100:
                                print("❌ No tienes suficiente oro para mejorar la armadura.\n")
                                continue

                            if heroe.armadura.tipo == "pesada":
                                print("❌ Ya tienes la armadura máxima.\n")
                                continue

                            heroe.oro -= 100
                            mejorar_armadura(heroe)
                            continue

                        # Compras normales (1–4)
                        tienda(heroe, opcion_tienda)

                oleada += 1
                heroe.increment_nivel()
                break
            
            # Turno Enemigo
            print("Turno Enemigo:")
            daño_enemigo = ejecutar_ataque(enemigo, heroe)
            print(f"El enemigo te hizo {daño_enemigo} de daño.\n")
            turno += 1
            # Separador de turnos
            print("-------------------- NUEVO TURNO --------------------")

        # Limpiamos la terminal
        limpiar_pantalla()
    print(f"\n--- FIN --- \n Oleadas superadas: {oleada-1}")
    if (oleada-1) > record:
        guardar_record(oleada-1)
        print("¡Nuevo récord guardado!")

if __name__ == "__main__":
    main()