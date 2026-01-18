import personajes
import armaduras
import combate

def jugar():
    print("--- BIENVENIDO AL RPG DE PRUEBA ---")

    # 1. Configuramos al Héroe (Miembro A)
    heroe = personajes.Personaje("Guerrero Ágil", vida_max=100, ataque_base=12)
    
    # 2. Le ponemos una armadura (Miembro B)
    # Creamos un objeto Armadura y se lo asignamos al atributo .armadura del héroe
    heroe.armadura = armaduras.Armadura("media", "Cota de Malla", reduccion=4, durabilidad_max=20)
    
    # 3. Configuramos al Enemigo (Miembro A)
    enemigo = personajes.Personaje("Orco Gruñón", vida_max=60, ataque_base=8)

    print(f"¡Un {enemigo.nombre} aparece!")
    print(f"Vas equipado con {armaduras.resumen_armadura(heroe)}")
    print("-" * 30)

    # 4. Bucle de combate
    while heroe.esta_vivo() and enemigo.esta_vivo():
        # --- TURNO DEL JUGADOR ---
        print(f"\nESTADO: {heroe.mostrar_estado()} | {armaduras.resumen_armadura(heroe)}")
        print("1. Atacar | 2. Defender | 3. Reparar Armadura")
        opcion = input("Elige una acción: ")

        if opcion == "1":
            resumen = combate.hacer_ataque(heroe, enemigo)
            print(resumen)
        elif opcion == "2":
            combate.activar_defensa(heroe)
        elif opcion == "3":
            armaduras.reparar_armadura(heroe)
        else:
            print("Te quedas confundido y pierdes el turno...")

        # Comprobar si el enemigo murió
        if not enemigo.esta_vivo():
            print(f"\n¡Has derrotado al {enemigo.nombre}!")
            break

        # --- TURNO DEL ENEMIGO ---
        print(f"\nTurno de {enemigo.nombre}...")
        resumen_enemigo = combate.hacer_ataque(enemigo, heroe)
        print(resumen_enemigo)

        # Comprobar si el héroe murió
        if not heroe.esta_vivo():
            print("\nHas sido derrotado... GAME OVER.")
            break

    print("\n--- FIN DEL COMBATE ---")

if __name__ == "__main__":
    jugar()