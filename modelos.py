class Perro:
    def __init__(self, nombre, color, edad):
        self.nombre = nombre
        self.color = color
        self.edad = edad

    def cartilla (self):
        return f"El cliente se llama {self.nombre}, es color {self.color}, y tiene {self.edad} años"
