import random

class Personaje:
    def __init__(self, nombre, vida_max, ataque_base, kits_reparacion=2):
        self.nombre = nombre
        self.vida_max = vida_max
        self.vida = vida_max
        self.ataque_base = ataque_base
        self.defendiendo = False
        self.armadura = None  # Se asignará en el main
        self.kits_reparacion = kits_reparacion

    def esta_vivo(self):
        return self.vida > 0

    def recibir_daño(self, cantidad):
        self.vida -= cantidad
        if self.vida < 0:
            self.vida = 0

    def curar(self, cantidad):
        self.vida += cantidad
        if self.vida > self.vida_max:
            self.vida = self.vida_max

    def mostrar_estado(self):
        return f"{self.nombre}: {self.vida}/{self.vida_max} HP"