# proyecto_historial_medico

historial_medico = []

def agregar_paciente():
    nombre = input("Nombre del paciente: ")
    edad = input("Edad: ")
    genero = input("Género: ")
    diagnostico = input("Diagnóstico: ")

    paciente = {
        "nombre": nombre,
        "edad": edad,
        "genero": genero,
        "diagnostico": diagnostico
    }

    historial_medico.append(paciente)
    print("Paciente agregado correctamente.\n")


def mostrar_pacientes():
    if not historial_medico:
        print("No hay pacientes registrados.\n")
        return

    for i, paciente in enumerate(historial_medico, start=1):
        print(f"\n--- Paciente {i} ---")
        print(f"Nombre: {paciente['nombre']}")
        print(f"Edad: {paciente['edad']}")
        print(f"Género: {paciente['genero']}")
        print(f"Diagnóstico: {paciente['diagnostico']}")


def buscar_paciente():
    nombre_buscar = input("Ingrese el nombre del paciente a buscar: ")

    for paciente in historial_medico:
        if paciente["nombre"].lower() == nombre_buscar.lower():
            print("\nPaciente encontrado:")
            print(f"Nombre: {paciente['nombre']}")
            print(f"Edad: {paciente['edad']}")
            print(f"Género: {paciente['genero']}")
            print(f"Diagnóstico: {paciente['diagnostico']}")
            return

    print("Paciente no encontrado.\n")


def menu():
    while True:
        print("\n--- MENÚ HISTORIAL MÉDICO ---")
        print("1. Agregar paciente")
        print("2. Mostrar pacientes")
        print("3. Buscar paciente")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_paciente()
        elif opcion == "2":
            mostrar_pacientes()
        elif opcion == "3":
            buscar_paciente()
        elif opcion == "4":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida.\n")


if __name__ == "__main__":
    menu()
