"""Universidad de Manizales
Facultad de Ciencias e Ingenierías
Asignatura: Programación I 
Actividad colaborativa: Taller práctico

Ejercicio 9: Composición 
Integrantes del equipo:
- [Luis David Villa López]
- [Brayan Horacio Romero Ariza]

Descripción: Demuestra el concepto de composición al integrar una clase 'Motor' 
como parte de los atributos de una clase más compleja llamada 'Coche', modelando 
una relación de tipo "tiene un" entre ambas clases."""

class Motor:
    """Clase que modela un motor independiente, que puede ser utilizado por diferentes coches"""
    def __init__(self, potencia, tipo):
        self.potencia = potencia
        self.tipo = tipo

    def describir_motor(self):
        """Retorna un string con la especificación del motor."""
        return f"{self.potencia} Caballos de Fuerza, de tipo {self.tipo}"


class Coche:
    """Clase que modela un automóvil. Utiliza composición al incluir un objeto 'Motor' como parte de su estructura."""
    def __init__(self, marca, modelo, motor):
        """Constructor de Coche.
        Parámetros:
      
        marca : str
        modelo : str
        motor : Motor
            Objeto instanciado de la clase Motor, demostrando la relación de composición."""
        self.marca = marca
        self.modelo = modelo
        self.motor = motor

    def describir(self):
        """
        Describe el coche, delegando la descripción del motor al objeto interno.
        """
        print(f"Vehículo: {self.marca} {self.modelo}")
        # Acceso al método de la clase compuesta para describir el motor
        print(f"  └─ Especificaciones de motor: {self.motor.describir_motor()}")


# Ejecución

# 1. Se crea la parte independiente (Motor)
motor_v8 = Motor(450, "V8 Gasolina")

# 2. Se compone el objeto principal (Coche) pasándole el objeto Motor
coche_deportivo = Coche("Ford", "Mustang GT", motor_v8)

coche_deportivo.describir()