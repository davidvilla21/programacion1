"""Universidad de Manizales
Facultad de Ciencias e Ingenierías
Asignatura: Programación I
Actividad colaborativa: Taller práctico

Ejercicio 8: Interfaces
Integrantes del equipo:
- [Luis David Villa López]
- [Brayan Horacio Romero Ariza]

Descripción: Python no posee una palabra clave 'interface' nativa. Para simularla, 
se crean clases abstractas puras (módulo ABC) donde todos sus métodos son abstractos,
definiendo así un comportamiento común que otras clases deben implementar"""

from abc import ABC, abstractmethod

class Volador(ABC):
    """Interfaz simulada mediante una clase abstracta pura.
    Define el contrato 'volar' que deben cumplir las clases que la implementen"""

    @abstractmethod
    def volar(self):
        """Método abstracto que representa la acción de volar. 
        Las clases que implementen esta interfaz deben proporcionar su propia implementación."""
        pass

class Pajaro(Volador):
    """Implementa la interfaz Volador para el contexto de un ser vivo"""
    def volar(self):
        """Implementación específica del vuelo de un pájaro"""
        print("El pájaro alza el vuelo batiendo fuertemente sus alas.")

class Avion(Volador):
    """Implementa la interfaz Volador para el contexto de una máquina"""
    def volar(self):
        """Implementación específica del vuelo de un avión"""
        print("El avión despega encendiendo sus motores a reacción y generando sustentación.")

# Ejecución

pajaro = Pajaro()
avion = Avion()

pajaro.volar()
avion.volar()