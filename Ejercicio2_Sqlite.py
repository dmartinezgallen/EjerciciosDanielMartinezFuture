import sqlite3

def conectar_db():
    conn = sqlite3.connect("tareaslite.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tareas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            descripcion TEXT NOT NULL,
            completada BOOLEAN NOT NULL DEFAULT 0
        )
    """)
    conn.commit()
    return conn, cursor

def agregar_tarea(descripcion):
    conn, cursor = conectar_db()
    cursor.execute("INSERT INTO tareas (descripcion, completada) VALUES (?, ?)", (descripcion, 0))
    conn.commit()
    conn.close()

def listar_tareas():
    conn, cursor = conectar_db()
    cursor.execute("SELECT id, descripcion, completada FROM tareas")
    tareas = cursor.fetchall()
    conn.close()
    return tareas

def marcar_completada(tarea_id):
    conn, cursor = conectar_db()
    cursor.execute("UPDATE tareas SET completada = 1 WHERE id = ?", (tarea_id,))
    conn.commit()
    conn.close()

def eliminar_tarea(tarea_id):
    conn, cursor = conectar_db()
    cursor.execute("DELETE FROM tareas WHERE id = ?", (tarea_id,))
    conn.commit()
    conn.close()

def mostrar_menu():
    print("\nGestor de Tareas")
    print("1. Agregar tarea")
    print("2. Ver lista de tareas")
    print("3. Marcar tarea como completada")
    print("4. Eliminar tarea")
    print("5. Salir")

def main():
    conectar_db()
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            tarea = input("Ingrese la nueva tarea: ")
            if tarea:
                agregar_tarea(tarea)
                print("Tarea agregada.")
        elif opcion == "2":
            tareas = listar_tareas()
            if not tareas:
                print("No hay tareas.")
            else:
                for tarea in tareas:
                    estado = "[X]" if tarea[2] else "[ ]"  # [X] para completada, [ ] para no completada
                    print(f"{estado} {tarea[0]}. {tarea[1]}")
        elif opcion == "3":
            try:
                num = int(input("Número de tarea a completar: "))
                marcar_completada(num)
                print("Tarea marcada como completada.")
            except ValueError:
                print("Ingrese un número válido.")
        elif opcion == "4":
            try:
                num = int(input("Número de tarea a eliminar: "))
                eliminar_tarea(num)
                print("Tarea eliminada.")
            except ValueError:
                print("Ingrese un número válido.")
        elif opcion == "5":
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
