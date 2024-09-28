import tkinter as tk
from tkinter import messagebox

# Crear la ventana principal
root = tk.Tk()
root.title("Lista de Tareas")

# Lista de tareas (almacenada en memoria)
tasks = []

# Función para actualizar la lista visualmente
def update_task_list():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        task_listbox.insert(tk.END, task)

# Función para añadir una nueva tarea
def add_task(event=None):
    task = entry_task.get()
    if task:
        tasks.append(task)
        entry_task.delete(0, tk.END)
        update_task_list()
    else:
        messagebox.showwarning("Advertencia", "No puedes añadir una tarea vacía.")

# Función para marcar una tarea como completada
def mark_completed():
    try:
        selected_task_index = task_listbox.curselection()[0]
        tasks[selected_task_index] = f"{tasks[selected_task_index]} (completada)"
        update_task_list()
    except IndexError:
        messagebox.showwarning("Advertencia", "Por favor, selecciona una tarea.")

# Función para eliminar una tarea
def delete_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        tasks.pop(selected_task_index)
        update_task_list()
    except IndexError:
        messagebox.showwarning("Advertencia", "Por favor, selecciona una tarea.")

# Elementos de la interfaz gráfica
entry_task = tk.Entry(root, width=40)
entry_task.pack(pady=10)

# Asociar la tecla 'Enter' con la función de añadir tarea
entry_task.bind("<Return>", add_task)

# Botón para añadir tarea
button_add = tk.Button(root, text="Añadir Tarea", command=add_task)
button_add.pack(pady=5)

# Lista de tareas
task_listbox = tk.Listbox(root, width=50, height=10)
task_listbox.pack(pady=10)

# Botón para marcar como completada
button_complete = tk.Button(root, text="Marcar como Completada", command=mark_completed)
button_complete.pack(pady=5)

# Botón para eliminar tarea
button_delete = tk.Button(root, text="Eliminar Tarea", command=delete_task)
button_delete.pack(pady=5)

# Ejecutar la aplicación
root.mainloop()
