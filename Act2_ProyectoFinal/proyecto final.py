class Medico:
    # 1. El método constructor
    def __init__(self, nombre, especialidad, turnos_disponibles):
        self.nombre = nombre
        self.especialidad = especialidad
        self.turnos_disponibles = turnos_disponibles
        
    # 2. Mostrar la información
    def mostrar_info(self):
        print("----- MÉDICO -----")
        print(f"Nombre: {self.nombre}")
        print(f"Especialidad: {self.especialidad}")
        print(f"Turnos restantes: {self.turnos_disponibles}") # Corregido el nombre del atributo

    # 3. Verifica de disponibilidad de agenda
    def reducir_disponibilidad(self):
        if self.turnos_disponibles > 0:
            self.turnos_disponibles -= 1
            print("Cita agendada correctamente.")
            print(f"Turnos restantes: {self.turnos_disponibles}")
        else:
            print("No hay disponibilidad para este médico.")


class Paciente:
    # Método constructor
    def __init__(self, nombre, documento):
        self.nombre = nombre
        self.documento = documento
        self.historial_clinico = []

    # Agrega notas a la HC
    def agregar_al_historial(self, anotacion):
        self.historial_clinico.append(anotacion)

    # Mostrar la HC
    def mostrar_historial(self):
        # Validar si la lista está vacía
        if not self.historial_clinico:
            print("El paciente aún no tiene registros médicos.")
        else:
            print(f"Historial clínico de {self.nombre}:")
            # Recorrer e imprimir cada anotación
            for anotacion in self.historial_clinico:
                print(f"- {anotacion}")


class Cita:
    # Método constructor
    def __init__(self, medico_asignado, paciente, fecha):
        # Atributos de la cita
        self.medico_asignado = medico_asignado
        self.paciente = paciente
        self.fecha = fecha

        # La cita inicia activa
        self.estado_activa = True

        # Reduce automáticamente la disponibilidad en la agenda del médico
        self.medico_asignado.reducir_disponibilidad()

    # Método para agendar la cita
    def realizar_cita(self, diagnostico):
        # Verifica si la cita sigue activa
        if self.estado_activa:
            # Agregar diagnóstico a la HC
            self.paciente.agregar_al_historial(diagnostico)
            # Cambia estado de la cita
            self.estado_activa = False
            print("La cita fue realizada correctamente.")
        else:
            print("La cita ya fue atendida o cancelada.")

    # Método para cancelar la cita
    def cancelar_cita(self):
        # Cambia estado de la cita
        self.estado_activa = False
        print("La cita ha sido cancelada.")