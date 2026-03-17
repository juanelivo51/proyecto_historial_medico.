def hola():
    print("Hola mundo")

hola()  # llamando a la función

#git add archivo_01_medico.py
#git commit -m "Código inicial de archivo_01_medico.py"
     
def saludo(nombre):
    print(f"Hola {nombre}, bienvenido al historial médico")

saludo("Juan")  

   # archivo_01_medico.py
# Proyecto: Historial médico
# Autor: Juan Sebastián Elivo Ulloa

# Lista para almacenar pacientes
pacientes = []

def registrar_paciente(nombre: str, edad: int, sintomas: str):
    """
    Registra un paciente con su nombre, edad y síntomas.
    """
    paciente = {
        "nombre": nombre,
        "edad": edad,
        "sintomas": sintomas
    }
    pacientes.append(paciente)
    print(f"Paciente {nombre} registrado correctamente.")

def mostrar_pacientes():
    """
    Muestra la lista de pacientes registrados.
    """
    if not pacientes:
        print("No hay pacientes registrados.")
        return
    print("Lista de pacientes:")
    for idx, paciente in enumerate(pacientes, start=1):
        print(f"{idx}. Nombre: {paciente['nombre']}, Edad: {paciente['edad']}, Síntomas: {paciente['sintomas']}")

def saludo(nombre: str):
    """
    Función de saludo para el paciente.
    """
    print(f"Hola {nombre}, bienvenido al historial médico.")

# Ejemplo de uso
if __name__ == "__main__":
    saludo("Juan")
    registrar_paciente("Ana Pérez", 30, "Fiebre y dolor de cabeza")
    registrar_paciente("Carlos Gómez", 45, "Dolor de espalda")
    mostrar_pacientes()