import tkinter as tk
from tkinter import messagebox


class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Task Manager")

        # Lista de tareas (pendientes y completadas)
        self.tasks = []
        self.completed_tasks = []

        # Campo de entrada para agregar nuevas tareas
        self.task_entry = tk.Entry(root, width=40)
        self.task_entry.grid(row=0, column=0, padx=10, pady=10)
        self.task_entry.bind("<Return>", lambda event: self.add_task())

        # Botones para agregar, completar y eliminar tareas
        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.grid(row=0, column=1, padx=10)

        self.complete_button = tk.Button(root, text="Complete Task", command=self.complete_task)
        self.complete_button.grid(row=1, column=0, padx=10, pady=10)

        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_button.grid(row=1, column=1, padx=10)

        # Lista para mostrar las tareas
        self.task_listbox = tk.Listbox(root, width=50, height=10, selectmode=tk.SINGLE)
        self.task_listbox.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        # Asignar atajos de teclado
        root.bind("<c>", lambda event: self.complete_task())  # Atajo para completar tarea
        root.bind("<d>", lambda event: self.delete_task())  # Atajo para eliminar tarea
        root.bind("<Delete>", lambda event: self.delete_task())  # Otra opción para eliminar tarea
        root.bind("<Escape>", lambda event: self.root.quit())  # Atajo para cerrar la aplicación

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.update_task_list()
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Task cannot be empty!")

    def complete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            task = self.tasks.pop(selected_index)
            self.completed_tasks.append(task)
            self.update_task_list()
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task to complete!")

    def delete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            self.tasks.pop(selected_index)
            self.update_task_list()
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task to delete!")

    def update_task_list(self):
        # Limpiar la lista de tareas
        self.task_listbox.delete(0, tk.END)

        # Mostrar tareas pendientes
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

        # Mostrar tareas completadas (con estilo diferente)
        for task in self.completed_tasks:
            self.task_listbox.insert(tk.END, f"[Completed] {task}")


# Crear la ventana principal de la aplicación
root = tk.Tk()
app = TaskManagerApp(root)
root.mainloop()
