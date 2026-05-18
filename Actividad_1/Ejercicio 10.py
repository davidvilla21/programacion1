"""Universidad de Manizales
Facultad de Ciencias e Ingenierías
Asignatura: Programación I
Actividad colaborativa: Taller práctico

Ejercicio 10: Manejo de Excepciones y Clases Personalizadas
Integrantes del equipo:
- [Luis David Villa López]
- [XXXXXXXXXXXXXXXXXXXXXX]

Descripción: Crea una excepción personalizada que se lanza cuando la velocidad 
de un objeto Coche supera un límite establecido, e implementa un bloque try-except 
para capturar y manejar dicho error en el programa principal"""

class ExcesoVelocidadException(Exception):
    """ Excepción personalizada que hereda de la clase base Exception de Python.
    Se utiliza para señalar una infracción velocidad excesiva."""
    def __init__(self, mensaje="Se ha detectado un exceso de velocidad no permitido."):
        self.mensaje = mensaje
        super().__init__(self.mensaje)


class Coche:
    """Clase que simula un vehículo que puede acelerar."""
    def __init__(self, marca):
        self.marca = marca
        self.velocidad = 0

    def incrementar_velocidad(self, incremento):
        """Aumenta la velocidad actual. Si supera los 200 km/h, lanza una excepción.
           Parámetros:
           incremento : int
           Cantidad de velocidad a sumar."""
        self.velocidad += incremento
        print(f"El {self.marca} aceleró. Velocidad actual: {self.velocidad} km/h")
        
        # Validación de la regla de negocio
        if self.velocidad > 200:
            # Se lanza la excepción personalizada
            raise ExcesoVelocidadException(f"¡Alerta máxima! {self.velocidad} km/h supera el límite de 200 km/h.")

# Ejecución

coche_rapido = Coche("Ferrari")

# Bloque try-except para capturar la excepción controlada
try:
    coche_rapido.incrementar_velocidad(100) # Velocidad: 100
    coche_rapido.incrementar_velocidad(80)  # Velocidad: 180
    coche_rapido.incrementar_velocidad(50)  # Velocidad: 230 - debe Llanzar la excepción
except ExcesoVelocidadException as error:
    # Captura específica de nuestra excepción personalizada y muestra el mensaje de error
    print(f"\033[1;91m[ERROR CONTROLADO]: {error}\033[0m")
   
except Exception as e:
    # Captura genérica por si ocurre otro error imprevisto
    print(f"\033[93m\n[ERROR GENÉRICO]: Ocurrió un error inesperado: {e}\033[0m")
finally:
    # Este bloque siempre se ejecuta, haya o no error
    print("\n--- Finalización del diagnóstico del vehículo ---")