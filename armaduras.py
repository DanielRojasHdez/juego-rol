class Armadura:
    # Constructor: se ejecuta en el momento en el que se crea una armadura
    def __init__(self, tipo, nombre, reduccion, durabilidad_max):
        self.tipo = tipo
        self.nombre = nombre
        self.reduccion = reduccion
        self.durabilidad_max = durabilidad_max
        self.durabilidad = durabilidad_max

    def reducir_daño(self, daño):
        """Devuelve el daño tras aplicar la reducción y desgastar la armadura."""
        # Si la durabilidad es menor o igual a 0 significa que está rota, es decir, no tenemos proteccion de armadura, entonces devolvemos el daño tal cual.
        if self.durabilidad <= 0:
            return daño
        
        # Si la armadura es mayor a 0 restamos su valor de reducción al daño que hará el atacante
        daño_final = daño - self.reduccion
        # Como no queremos que el golpe recibido nos cure, bloqueamos en 0 si el resultado de el daño menos la reduccion nos da numeros negativos (ejemplo: si el daño recibido es 2 y la armadura nos reduce 5 el resultado sería -3, lo que hacemos es que dejamos el daño recibido en 0)
        if daño_final < 0:
            daño_final = 0
        
        # Llamamos al metodo perder_durabilidad para que nos reduzca la durabilidad de la armadura.
        self.perder_durabilidad()
        return daño_final

    # Cada vez que recibamos un golpe la armadura se deteriora perdiendo 1 punto 
    def perder_durabilidad(self):
        """Baja la durabilidad en 1."""
        if self.durabilidad > 0:
            self.durabilidad -= 1

    # Metodo de reparación de la armadura, cuando llamemos a este metodo la armadura se reparará la cantidad de puntos que le hallamos pasado por el argumento
    def reparar(self, cantidad):
        """Sube la durabilidad sin pasar del máximo."""
        self.durabilidad += cantidad
        if self.durabilidad > self.durabilidad_max:
            self.durabilidad = self.durabilidad_max

    # Metodo para detectar si la armadura está rota, si el metodo nos devuelve true significa que está rota
    def esta_rota(self):
        return self.durabilidad == 0

    def __str__(self):
        """Este método especial permite que al hacer print(armadura) salga el texto formateado."""
        return f"{self.nombre} ({self.durabilidad}/{self.durabilidad_max})"

# Estos se quedan fuera porque son "moldes" predefinidos
armadura_ligera = Armadura("ligera", "Armadura ligera", 2, 50)
armadura_media = Armadura("media", "Armadura media", 4, 40)
armadura_pesada = Armadura("pesada", "Armadura pesada", 6, 30)