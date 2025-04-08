# Lista de tareas

tareas = []
id_actual = 1  # Contador para IDs

# Cargar tareas desde el archivo
def cargar_tareas():
    global tareas, id_actual
    try:
        with open("tareas1.txt", "r") as archivo:
            for linea in archivo:
                id_tarea, tarea, completada = linea.strip().split(" | ")
                tareas.append({"id": int(id_tarea), "tarea": tarea, "completada": completada == "True"})
                id_actual = max(id_actual, int(id_tarea) + 1)
    except FileNotFoundError:
        pass

# Guardar tareas en el archivo
def guardar_tareas():
    with open("tareas1.txt", "w") as archivo:
        for tarea in tareas:
            archivo.write(f"{tarea['id']} | {tarea['tarea']} | {tarea['completada']}\n")

def agregar_tarea():
    global id_actual
    tarea = input("Ingrese la tarea: ")
    tareas.append({"id": id_actual, "tarea": tarea, "completada": False})
    id_actual += 1
    guardar_tareas()
    print("Tarea agregada.")

def ver_tareas():
    if not tareas:
        print("No hay tareas.")
    else:
        for tarea in tareas:
            estado = "[X]" if tarea["completada"] else "[ ]"
            print(f"{estado} {tarea['id']}. {tarea['tarea']}")

def marcar_completada():
    try:
        id_tarea = int(input("Ingrese el ID de la tarea a completar: "))
        for tarea in tareas:
            if tarea["id"] == id_tarea:
                tarea["completada"] = True
                guardar_tareas()
                print("Tarea completada.")
                return
        print("ID no encontrado.")
    except ValueError:
        print("Ingrese un número válido.")

def eliminar_tarea():
    global tareas
    try:
        id_tarea = int(input("Ingrese el ID de la tarea a eliminar: "))
        tareas = [tarea for tarea in tareas if tarea["id"] != id_tarea]
        guardar_tareas()
        print("Tarea eliminada.")
    except ValueError:
        print("Ingrese un número válido.")

def menu():
    cargar_tareas()
    while True:
        print("\nMenú:")
        print("1. Agregar tarea")
        print("2. Ver tareas")
        print("3. Marcar tarea como completada")
        print("4. Eliminar tarea")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_tarea()
        elif opcion == "2":
            ver_tareas()
        elif opcion == "3":
            marcar_completada()
        elif opcion == "4":
            eliminar_tarea()
        elif opcion == "5":
            guardar_tareas()
            print("Saliendo...")
            break
        else:
            print("Opción no válida.")

menu()
