"""Universidad de Manizales
Facultad de Ciencias e Ingenierías
Asignatura: Programación I
Actividad colaborativa: Taller práctico

Ejercicio 7: Clases Abstractas
Integrantes del equipo:
- [Luis David Villa López]
- [Brayan Horacio Romero Ariza]

Descripción: Implementa la clase abstracta 'Animal' utilizando el módulo ABC de Python,
obligando a las clases concretas derivadas a implementar el método 'hacerSonido'. Luego, crea clases concretas como 'Perro' 
y 'Gato' que hereden de 'Animal' y proporcionen su propia implementación del método 'hacerSonido'"""

from abc import ABC, abstractmethod

class Animal(ABC):
    """Clase abstracta que sirve como plantilla para distintos tipos de animales.Al heredar de ABC (Abstract Base Class), no puede ser instanciada directamente."""

    @abstractmethod
    def hacer_sonido(self):
        """Método abstracto. Toda clase concreta que herede de Animal debe implementar obligatoriamente este método"""
        pass


class Perro(Animal):
    """Clase concreta que implementa el comportamiento de un Perro"""
    def hacer_sonido(self):
        return "¡Guau, guau!"


class Gato(Animal):
    """Clase concreta que implementa el comportamiento de un Gato"""
    def hacer_sonido(self):
        return "¡Miau, miau!" 
    

# Ejecución
# Lista de animales creados a partir de las clases concretas Perro y Gato, 
# demostrando el uso de polimorfismo al tratar ambos objetos como instancias de la clase abstracta Animal
animales = [Perro(), Gato()]

# Se llama al método hacer_sonido en cada objeto de la lista, 
# demostrando que cada clase concreta tiene su propia implementación del método,
for animal in animales:
    # Se utiliza type(animal).__name__ para obtener el nombre de la clase de forma dinámica
    print(f"El {type(animal).__name__} hace: {animal.hacer_sonido()}")