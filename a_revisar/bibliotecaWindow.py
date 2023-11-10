"""from bibliotecaBD import *
import tkinter as tk
from tkinter import messagebox

class BibliotecaWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Registro de Libros")

        self.codigo_label = tk.Label(root, text="Código:")
        self.codigo_label.pack()
        self.codigo_entry = tk.Entry(root)
        self.codigo_entry.pack()

        self.titulo_label = tk.Label(root, text="Título:")
        self.titulo_label.pack()
        self.titulo_entry = tk.Entry(root)
        self.titulo_entry.pack()

        self.precio_reposicion_label = tk.Label(root, text="Precio de Reposición:")
        self.precio_reposicion_label.pack()
        self.precio_reposicion_entry = tk.Entry(root)
        self.precio_reposicion_entry.pack()

        self.guardar_button = tk.Button(root, text="Guardar Libro", command=self.guardar_libro)
        self.guardar_button.pack()

        self.db = BibliotecaDB("biblioteca.db")

    def guardar_libro(self):
        codigo = self.codigo_entry.get()
        titulo = self.titulo_entry.get()
        precio_reposicion = self.precio_reposicion_entry.get()

        # Validaciones de datos 
        
        if not codigo.isdigit():
            messagebox.showerror("Error", "El código debe ser un número entero.")
            return

        if not titulo:
            messagebox.showerror("Error", "El título no puede estar en blanco.")
            return

        try:
            precio_reposicion = float(precio_reposicion)
            if precio_reposicion < 0:
                raise ValueError("Precio de reposición negativo")
        except ValueError:
            messagebox.showerror("Error", "El precio de reposición debe ser un número real no negativo.")
            return

        self.db.guardar_libro(codigo, titulo, precio_reposicion)
        messagebox.showinfo("Éxito", "Libro guardado con éxito")

    def cerrar_ventana(self):
        self.db.cerrar()
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = BibliotecaWindow(root)
    root.protocol("WM_DELETE_WINDOW", app.cerrar_ventana)  # Para cerrar la base de datos antes de salir
    root.mainloop()
    """