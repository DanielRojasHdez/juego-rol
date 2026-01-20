import random
import copy
from armaduras import armadura_ligera, armadura_media, armadura_pesada

class Personaje:
    # Constructor: se ejecuta en el momento en el que se crea un personaje
    def __init__(self, nombre, vida_max, ataque_base, defenderse, armadura):
        self.nombre = nombre
        self.vida_max = vida_max
        self.vida = vida_max # Empezamos con la vida al máximo
        self.ataque_base = ataque_base
        self.defenderse = defenderse
        self.armadura = armadura

    # Este metodo es el que actualiza el estado del personaje cuando es golpeado en combate
    def recibir_daño(self, cantidad):
        """Resta vida y asegura que no baje de 0."""
        self.vida -= cantidad
        if self.vida < 0:
            self.vida = 0

    # Este metodo es de tipo booleano, desterminará si el personaje está vivo o no, devuelve true o false
    def esta_vivo(self):
        return self.vida > 0

    # Este metodo nos permite recuperar salud
    def curar(self, cantidad):
        self.vida += cantidad
        if self.vida > self.vida_max:
            self.vida = self.vida_max

    # Este metodo permite que los enemigos suban de nivel en el sistema de oleadas
    def increment_nivel(self):
        """Sube las estadísticas del personaje."""
        self.ataque_base += 2
        self.vida_max += 5
        self.vida = self.vida_max # Sanar al subir de nivel

    # Este metodo muestra el estado del personaje, mostrando la vida que queda
    def mostrar_estado(self):
        print(f"{self.nombre} | Vida: {self.vida}/{self.vida_max}")

# Función para crear un enemigo
def crear_enemigo(oleada):
    if oleada % 3 == 0:
        # El jefe tiene armadura media
        enemigo = Personaje("Jefe Orco", 60, random.randint(8,10), False, copy.deepcopy(armadura_media))
    else:
        # El soldado tiene armadura ligera
        enemigo = Personaje("Soldado", 35, random.randint(4,6), False, copy.deepcopy(armadura_ligera))
    
    # Aplicar dificultad según oleada
    for _ in range(oleada - 1):
        enemigo.increment_nivel()
    return enemigo