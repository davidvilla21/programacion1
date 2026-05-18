"""Universidad de Manizales
Facultad de Ciencias e Ingenierías
Asignatura: Programación I
Actividad colaborativa: Taller práctico

Ejercicios 4, 5 y 6: Herencia, Sobreescritura y Polimorfismo
Integrantes del equipo:
- [Luis David Villa López]
- [Brayan Horacio Romero Ariza]

Descripción: Implementa una jerarquía de clases donde 'Coche' y 'Bicicleta' heredan de 'Vehículo'. Se sobreescribe el método 'acelerar' y se demuestra el 
polimorfismo iterando sobre una lista de diferentes objetos."""

class Vehiculo:
    """ Clase padre que define el comportamiento común para todos los vehículos."""
    def __init__(self, velocidad=0):
        self.velocidad = velocidad

    def acelerar(self):
        """Método base para incrementar la velocidad."""
        self.velocidad += 5
        print(f"El vehículo genérico acelera a {self.velocidad} km/h")


class Coche(Vehiculo):
    """ Clase hija que hereda de Vehiculo."""
    def __init__(self, marca, velocidad=0):
        super().__init__(velocidad)  # Llama al constructor de la clase padre
        self.marca = marca           # Atributo específico de Coche

    def acelerar(self):
        """Sobreescritura del método padre. Define una aceleración específica para Coche."""
        self.velocidad += 30
        print(f"El coche {self.marca} acelera con motor a {self.velocidad} km/h")


class Bicicleta(Vehiculo):
    """Clase hija que hereda de Vehiculo."""
    def __init__(self, tipo, velocidad=0):
        super().__init__(velocidad)  # Llama al constructor de la clase padre
        self.tipo = tipo             # Atributo específico de Bicicleta

    def acelerar(self):
        """Sobreescritura del método padre. Define una aceleración específica para Bicicleta"""
        self.velocidad += 2
        print(f"La bicicleta de {self.tipo} pedalea y acelera a {self.velocidad} km/h")

# Demostración de Polimorfismo
# Creación de objetos de las clases hijas
mi_coche = Coche("Mazda")
mi_bici = Bicicleta("Montaña")

# Se crea una lista que agrupa distintos tipos de objetos bajo la misma interfaz o polimorfismo
lista_vehiculos = [mi_coche, mi_bici]

print("--- Ejecución Polimórfica ---")
# Recorrido de la lista e invocación del mismo método en cada objeto
for v in lista_vehiculos:
    # Aunque ambos son tipos distintos, Python llama a la versión correspondiente del método
    v.acelerar()  # Llama al método acelerar según el tipo real del objeto