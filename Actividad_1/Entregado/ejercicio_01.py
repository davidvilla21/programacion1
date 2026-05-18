"""Universidad de Manizales
Facultad de Ciencias e Ingenierías
Asignatura: Programación I
Actividad colaborativa: Taller práctico

Ejercicio 1: Creación de una Clase Básica
Integrantes:
- [Luis David Villa López]
- [Brayan Horacio Romero Ariza]

Descripción: Este script define la estructura básica de una clase llamada 'Coche',
establece sus atributos por defecto, y realiza la creación de varios objetos 
para demostrar la modificación de su estado y el uso de sus métodos.
"""

""" Clase que modela un automóvil básico.
    Atributos:
    marca : str          La marca fabricante del automóvil.
    modelo : str         El modelo específico del automóvil.
    ano : int            El año de fabricación del automóvil.
    """

class Coche:
    # Inicialización de atributos con valores por defecto
    marca = "Sin marca"
    modelo = "Sin modelo"
    ano = 0

    """Imprime la información actual del objeto instanciado."""
    def describir(self):
        print(f"Coche: {self.marca} {self.modelo}, Año: {self.ano}")

# Creación del primer objeto de la clase Coche y asignación de valores a sus atributos
coche1 = Coche()
coche1.marca = "Toyota"
coche1.modelo = "Corolla"
coche1.ano = 2021
# Creación del segundo objeto de la clase Coche y asignación de valores a sus atributos
coche2 = Coche()
coche2.marca = "Honda"
coche2.modelo = "Civic"
coche2.ano = 2022

# Llamada al método describir para mostrar la información de ambos objetos
coche1.describir()
coche2.describir()