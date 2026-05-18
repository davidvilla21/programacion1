"""Universidad de Manizales
Facultad de Ciencias e Ingenierías
Asignatura: Programación I
Actividad colaborativa: Taller práctico

Ejercicios 2 y 3: Encapsulamiento y Constructores
Integrantes del equipo:
- [Luis David Villa López]
- [Brayan Horacio Romero Ariza]

Descripción: Modifica la clase Coche para hacer uso del método constructor (__init__)
para inicializar los objetos, y aplica encapsulamiento haciendo los atributos privados,
exponiendo métodos getter y setter para su manipulación segura."""

class Coche:
    """Clase que representa un automóvil utilizando encapsulamiento y un constructor."""

    def __init__(self, marca, modelo, ano):
        """Método constructor que inicializa los atributos del coche.
        Parámetros:
        marca : str
        modelo : str
        ano : int
        
        Se utiliza el doble guion bajo (__) para definir los atributos
        como privados (encapsulamiento)."""
        self.__marca = marca
        self.__modelo = modelo
        self.__ano = ano

    # Métodos Getter
    def get_marca(self):
        """Retorna la marca del coche."""
        return self.__marca

    def get_modelo(self):
        """Retorna el modelo del coche."""
        return self.__modelo

    def get_ano(self):
        """Retorna el año de fabricación del coche."""
        return self.__ano

    # Métodos Setter (para modificar datos encapsulados)
   
    def set_marca(self, marca):
        """Modifica la marca del coche."""
        self.__marca = marca

    def set_modelo(self, modelo):
        """Modifica el modelo del coche."""
        self.__modelo = modelo

    def set_ano(self, ano):
        """Modifica el año de fabricación del coche."""
        self.__ano = ano

    def describir(self):
        """Imprime los detalles del coche accediendo a los atributos privados."""
        return f"Coche: {self.__marca}, Modelo: {self.__modelo}, Año: {self.__ano}"

# Creacióny uso de objetos

# Creación de objetos usando el constructor con diferentes parámetros
coche1 = Coche("Ford", "Mustang", 2023)
coche2 = Coche("Chevrolet", "Camaro", 2021)

print(coche1.describir())
print(coche2.describir())

# Uso de un método setter para modificar un atributo privado de forma segura
coche1.set_ano(2024)
print(f"Tras la actualización, el nuevo año del {coche1.get_marca()} es {coche1.get_ano()}")