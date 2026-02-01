import random
import copy
from armaduras import armadura_ligera, armadura_media, armadura_pesada

# CLASE PERSONAJE
class Personaje:
    # Constructor: se ejecuta en el momento en el que se crea un personaje
    def __init__(self, nombre, vida_max, ataque_base, armadura):
        self.nombre = nombre
        self.vida_max = vida_max
        self.vida = vida_max # Empezamos con la vida al máximo
        self.ataque_base = ataque_base
        self.armadura = armadura
        self.ultimo_turno_cura = -4
        self.reparaciones_combate = 0

    # Este metodo es el que actualiza el estado del personaje cuando es golpeado en combate
    def recibir_daño(self, cantidad):
        """Resta vida y asegura que no baje de 0."""
        self.vida -= cantidad
        if self.vida < 0:
            self.vida = 0

    # Este metodo es de tipo booleano, desterminará si el personaje está vivo o no, devuelve true o false
    def esta_vivo(self):
        return self.vida > 0


    # Este metodo permite que los enemigos suban de nivel en el sistema de oleadas
    def increment_nivel(self):
        # Si el nombre del enemigo es 'Jefe Orco' aumentará sus caráctristicas de una forma determinada
        if self.nombre == 'Jefe Orco':
            self.ataque_base += 5
            self.vida_max += 10
            self.vida = self.vida_max
        elif self.nombre == 'Héroe':
            self.ataque_base += 3
            self.vida_max += 2
            self.vida += 10
            if self.vida > self.vida_max:
                self.vida = self.vida_max
        # Si el personaje no es 'Jefe Orco' ni 'Héroe' aumentará sus carácteristicas de otra forma determinada
        else:
            self.ataque_base += 2
            self.vida_max += 5
            self.vida = self.vida_max 


    
# CLASE HÉROE (hereda de Personaje)
class Heroe(Personaje):
    def __init__(self, nombre, vida_max, ataque_base, armadura):
        # Llamamos al contructor de Personaje
        super().__init__(nombre, vida_max, ataque_base, armadura)
        # Atriibutos exclusivos de Heroe
        self.defenderse = False
        self.reparaciones_disponibles = 3
        self.curas_disponibles = 3
        self.oro = 20
    
    # Metodos exclusivos del Heroe
    # Este metodo nos permite recuperar salud
    def curar(self, cantidad):
        self.vida += cantidad
        if self.vida > self.vida_max:
            self.vida = self.vida_max

    # Metodo para comprar curas en la tienda
    def comprar_curas(self, cantidad):
        self.curas_disponibles += cantidad
        print(f"Has comprado {cantidad} cura/s. Tienes {self.curas_disponibles} curas disponibles.")

    # Metodo para comprar reparaciones en la tienda
    def comprar_reparaciones(self, cantidad):
        self.reparaciones_disponibles += cantidad
        print(f"Has comprado {cantidad} reparacion/es. Tienes {self.reparaciones_disponibles} reparaciones de armadura disponibles.")

    # Metodo para aumentar el oro cuando derrotemos una oleada 
    def aumento_oro(self, enemigo, oleada):
        if oleada > 1:
            incremento_oro_por_oleada = 4
            if enemigo.nombre == 'Jefe Orco':
                aumento_oro_por_oleada = incremento_oro_por_oleada * (oleada -1)
                self.oro += (20 + aumento_oro_por_oleada)    
            else:
                aumento_oro_por_oleada = incremento_oro_por_oleada * (oleada -1)
                self.oro += (8 + aumento_oro_por_oleada)
        else:
            if enemigo.nombre == 'Jefe Orco':
                self.oro += 20     
            else:
                self.oro += 8 

    # Este metodo muestra el estado del Heroe, mostrando la vida que queda
    def mostrar_estado(self):
        print(f"{self.nombre} | Vida: {self.vida}/{self.vida_max} | {self.armadura} | Ataque base: {self.ataque_base} | Oro: {self.oro} | Curas Disponibles: {self.curas_disponibles} | Reparaciones Disponibles: {self.reparaciones_disponibles}")



# CLASE ENEMIGO (hereda de Personaje)
class Enemigo(Personaje):
    def __init__(self, nombre, vida_max, ataque_base, armadura):
        super().__init__(nombre, vida_max, ataque_base, armadura)

    # Este metodo muestra el estado del Enemigo, mostrando la vida que queda
    def mostrar_estado(self):
        print(f"{self.nombre} | Vida: {self.vida}/{self.vida_max} | {self.armadura} | Ataque base: {self.ataque_base}")



# FUNCIONES ADICIONALES
# Función para devolver un tipo de armadura concreta
# def asignar_armadura():
#     # Bucle infinito controlado para que la elección sea válida
#     while True: 
#         # Elecciones
#         print("\nIntroduce el número de la armadura que quieres utilizar:")
#         print("1. Armadura ligera: Protección(2), Duración(10)")
#         print("2. Armadura media: Protección(4), Duración(8)")
#         print("3. Armadura pesada: Protección(6), Duración(6)\n")
        
#         armadura_heroe = input("Elección (1, 2 o 3): ")

#         if armadura_heroe == "1": return armadura_ligera
#         elif armadura_heroe == "2": return armadura_media
#         elif armadura_heroe == "3": return armadura_pesada
#         else: print("\n❌ Elección incorrecta. Por favor, introduce 1, 2 o 3.")

# Función para crear un enemigo según la oleada a la que nos enfrentemos
def crear_enemigo(oleada):
    # Si el resto de oleada dividido entre 3 es 0 creamos un jefe
    if oleada % 3 == 0:
        # Creación del objeto enemigo con características de jefe
        # enemigo = Enemigo("Jefe Orco", 60, random.randint(8,10), copy.deepcopy(armadura_media))
        enemigo = Enemigo("Jefe Orco", 60, 8, copy.deepcopy(armadura_media))
        # Cáculo para determinar porque jefe vamos en la partida
        numero_jefe = int(oleada / 3)
        # Aumento del nivel del jefe (Ejemplo: si vamos porel jefe numero 2 aumentará de nivel 1 vez)
        for _ in range(numero_jefe - 1):
            enemigo.increment_nivel()
        return enemigo
    # Si el resto de oleada entre 3 no es 0 creamos un soldado normal
    else:
        # Creación del objeto enemigo con características de soldado
        # enemigo = Enemigo("Soldado", 35, random.randint(4,6), copy.deepcopy(armadura_ligera))
        enemigo = Enemigo("Soldado", 35, 4, copy.deepcopy(armadura_ligera))
        # Aumento de nivel de soldado según la oleada (Ejemplo: si vamos por la oleada 3 el enemigo aumenta 2 veces su nivel)
        for _ in range(oleada - 1):
            enemigo.increment_nivel()
        return enemigo
    