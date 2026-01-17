class Armadura:
    def __init__(self, tipo):
        """
        Esta función se ejecuta cuando se crea una armadura.
        Aquí decidimos sus características según el tipo.
        """

        # Guardamos el tipo de armadura (ligera, media, pesada)
        self.tipo = tipo

        # Asignamos valores según el tipo elegido
        if tipo == "ligera":
            self.nombre = "Armadura ligera"
            self.reduccion = 2            # Cuánto daño reduce
            self.durabilidad_max = 50     # Durabilidad máxima
            self.durabilidad = 50         # Durabilidad actual

        elif tipo == "media":
            self.nombre = "Armadura media"
            self.reduccion = 4
            self.durabilidad_max = 40
            self.durabilidad = 40

        elif tipo == "pesada":
            self.nombre = "Armadura pesada"
            self.reduccion = 6
            self.durabilidad_max = 30
            self.durabilidad = 30

        else:
            # Si el tipo no es válido, no hay armadura
            self.nombre = "Sin armadura"
            self.reduccion = 0
            self.durabilidad_max = 0
            self.durabilidad = 0

        # Mensaje informativo al crear la armadura
        print(f"Has elegido: {self.nombre}")

    def reducir_daño(self, daño):
        """
        Recibe un daño y devuelve el daño final
        después de aplicar la protección de la armadura.
        """

        # Solo protege si la armadura no está rota
        if self.durabilidad > 0:
            daño_final = daño - self.reduccion

            # El daño nunca puede ser negativo
            if daño_final < 0:
                daño_final = 0

            # La armadura pierde durabilidad SOLO si protege
            self.perder_durabilidad()

            return daño_final
        else:
            # Si está rota, no reduce daño
            return daño

    def perder_durabilidad(self):
        """
        Reduce la durabilidad de la armadura en 1.
        Muestra un aviso si la armadura se rompe.
        """

        if self.durabilidad > 0:
            self.durabilidad -= 1

            # Aviso cuando la armadura se rompe
            if self.durabilidad == 0:
                print("⚠️ La armadura se ha roto")

    def reparar(self, cantidad):
        """
        Repara la armadura aumentando su durabilidad.
        No puede superar la durabilidad máxima.
        """

        self.durabilidad += cantidad

        if self.durabilidad > self.durabilidad_max:
            self.durabilidad = self.durabilidad_max

    def esta_rota(self):
        """
        Devuelve True si la armadura está rota.
        Devuelve False si todavía funciona.
        """

        return self.durabilidad == 0

    def ver_estado(self):
        """
        Muestra por pantalla el estado actual de la armadura.
        """

        print(f"{self.nombre} - Durabilidad: {self.durabilidad}/{self.durabilidad_max}")
