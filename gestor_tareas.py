import tkinter as tk
from tkinter import messagebox
import sqlite3

# BASE DE DATOS 
conexion = sqlite3.connect("tareas_grafico.db")
cursor = conexion.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS tareas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                tarea TEXT,
                completada BOOLEAN DEFAULT 0)''')
conexion.commit()

#  FUNCIONES
def agregar_tarea():
    tarea = entrada.get()
    if tarea:
        cursor.execute("INSERT INTO tareas (tarea) VALUES (?)", (tarea,))
        conexion.commit()
        entrada.delete(0, tk.END)
        actualizar_lista()
    else:
        messagebox.showwarning("Atencion", "Escribe una tarea!")

def actualizar_lista():
    lista.delete(0, tk.END)
    cursor.execute("SELECT rowid, tarea, completada FROM tareas")
    for tarea in cursor.fetchall():
        estado = "[X]" if tarea[2] else "[ ]"
        lista.insert(tk.END, f"{tarea[0]}. {tarea[1]:<30} {estado}")

def cambiar_estado():
    try:
        seleccion = lista.curselection()[0]
        num_tarea = lista.get(seleccion).split(".")[0]
        cursor.execute("UPDATE tareas SET completada = NOT completada WHERE rowid = ?", (num_tarea,))
        conexion.commit()
        actualizar_lista()
    except:
        messagebox.showwarning("Atencion", "Selecciona una tarea primero")

#  INTERFAZ CON COLORES 
ventana = tk.Tk()
ventana.title("Lista de Tareas")
ventana.geometry("700x400")
ventana.configure(bg="#333333")  # Fondo gris oscuro

# Frame izquierdo (Botones y entrada)
frame_izq = tk.Frame(ventana, bg="#444444", padx=10, pady=10)  # Gris medio
frame_izq.pack(side="left", fill="y")

tk.Label(frame_izq, text="Nueva Tarea:", bg="#444444", fg="#FFD700", font=('Arial', 10)).pack(pady=5)
entrada = tk.Entry(frame_izq, width=25, bg="#555555", fg="white", insertbackground="white")
entrada.pack(pady=5)

tk.Button(frame_izq, text="Agregar (+)", command=agregar_tarea, bg="#FFD700", fg="black", padx=10).pack(pady=5)
tk.Button(frame_izq, text="Cambiar Estado (X)", command=cambiar_estado, bg="#FFD700", fg="black", padx=10).pack(pady=5)

# Frame derecho (Lista de tareas)
frame_der = tk.Frame(ventana, bg="#333333", padx=10, pady=10)
frame_der.pack(side="right", expand=True, fill="both")

lista = tk.Listbox(frame_der, width=50, height=20, font=("Arial", 10), bg="#555555", fg="white", selectbackground="#FFD700")
lista.pack(fill="both", expand=True)

actualizar_lista()

ventana.mainloop()
conexion.close()