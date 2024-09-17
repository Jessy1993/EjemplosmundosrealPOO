import tkinter as tk
from tkinter import ttk, messagebox
# Función para agregar un evento
def agregar_evento():
    fecha = date_entry.get()
    hora = entry_hora.get()
    descripcion = entry_descripcion.get()

    if fecha and hora and descripcion:
        tree.insert('', 'end', values=(fecha, hora, descripcion))
        entry_hora.delete(0, tk.END)
        entry_descripcion.delete(0, tk.END)
    else:
        messagebox.showwarning("Datos incompletos", "Por favor, completa todos los campos.")

# Función para eliminar un evento
def eliminar_evento():
    selected_item = tree.selection()
    if selected_item:
        tree.delete(selected_item)
    else:
        messagebox.showwarning("No seleccionado", "Por favor, selecciona un evento para eliminar.")

# Configuración de la ventana principal
root = tk.Tk()
root.title("Agenda Personal")

# Contenedor de entrada de datos
frame_inputs = tk.Frame(root)
frame_inputs.pack(pady=10)

# Etiquetas y campos de entrada
tk.Label(frame_inputs, text="Fecha:").grid(row=0, column=0, padx=10, pady=5)

tk.Label(frame_inputs, text="Hora:").grid(row=1, column=0, padx=10, pady=5)
entry_hora = tk.Entry(frame_inputs)
entry_hora.grid(row=1, column=1, padx=10, pady=5)

tk.Label(frame_inputs, text="Descripción:").grid(row=2, column=0, padx=10, pady=5)
entry_descripcion = tk.Entry(frame_inputs)
entry_descripcion.grid(row=2, column=1, padx=10, pady=5)

# Botones de acción
frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=10)

btn_agregar = tk.Button(frame_buttons, text="Agregar Evento", command=agregar_evento)
btn_agregar.grid(row=0, column=0, padx=10)

btn_eliminar = tk.Button(frame_buttons, text="Eliminar Evento", command=eliminar_evento)
btn_eliminar.grid(row=0, column=1, padx=10)

btn_salir = tk.Button(frame_buttons, text="Salir", command=root.quit)
btn_salir.grid(row=0, column=2, padx=10)

# TreeView para mostrar los eventos
frame_tree = tk.Frame(root)
frame_tree.pack(pady=10)

columns = ("Fecha", "Hora", "Descripción")
tree = ttk.Treeview(frame_tree, columns=columns, show="headings")
tree.heading("Fecha", text="Fecha")
tree.heading("Hora", text="Hora")
tree.heading("Descripción", text="Descripción")
tree.pack()

root.mainloop()
