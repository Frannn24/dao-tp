# ui.py

import tkinter as tk
from tkinter import messagebox
from libro import Libro
from database import BibliotecaDB
import sqlite3

class CrearLibroWindow:
    def __init__(self, root, ventana_principal, db):
        self.root = root
        self.root.title("Crear Nuevo Libro")
        self.ventana_principal = ventana_principal
        self.db = db
        self.exito = False  # Variable para controlar si el libro se guardó con éxito

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

        self.crear_libro_button = tk.Button(root, text="Crear Libro", command=self.crear_libro)
        self.crear_libro_button.pack()

        self.volver_button = tk.Button(root, text="Volver a Guardar Libro", command=self.volver_a_guardar_libro)
        self.volver_button.pack()

    def crear_libro(self):
        codigo = self.codigo_entry.get()
        titulo = self.titulo_entry.get()
        precio_reposicion = self.precio_reposicion_entry.get()

        # Validaciones de datos aquí
        if not codigo.isdigit() or not titulo or not precio_reposicion.replace(".", "", 1).isdigit():
            mensaje_error = "Por favor, ingrese datos válidos."
            messagebox.showerror("Error", mensaje_error)
            return  # Detiene la ejecución en caso de error de validación

        codigo = int(codigo)
        precio_reposicion = float(precio_reposicion)

        if codigo < 1:
            mensaje_error = "El código debe ser un número entero positivo."
            messagebox.showerror("Error", mensaje_error)
            return  # Detiene la ejecución en caso de error de validación

        if precio_reposicion < 0:
            mensaje_error = "El precio de reposición debe ser un número real no negativo."
            messagebox.showerror("Error", mensaje_error)
            return  # Detiene la ejecución en caso de error de validación

        try:
            nuevo_libro = Libro(codigo, titulo, precio_reposicion)
            self.db.guardar_libro(nuevo_libro)
            self.exito = True
        except sqlite3.IntegrityError:
            mensaje_error = "El código ya existe en la base de datos. Por favor, ingrese un código único."
            messagebox.showerror("Error", mensaje_error)
            self.exito = False
            return

        if self.exito:
            messagebox.showinfo("Éxito", "Libro guardado con éxito")

    def volver_a_guardar_libro(self):
        self.root.destroy()  # Cierra la ventana actual
        self.ventana_principal.volver_a_ventana_guardar_libro()  # Llama al método de la ventana principal para volver a la ventana "Guardar Libro"

class VentanaPrincipal:
    def __init__(self, root, db):
        self.root = root
        self.root.title("Biblioteca")
        self.db = db

        self.guardar_libro_button = tk.Button(root, text="Guardar Libro", command=self.abrir_ventana_guardar_libro)
        self.guardar_libro_button.pack()

    def abrir_ventana_guardar_libro(self):
        self.root.withdraw()
        ventana_guardar_libro = tk.Toplevel(self.root)
        app = CrearLibroWindow(ventana_guardar_libro, self, self.db)

    def volver_a_ventana_guardar_libro(self):
        self.root.deiconify()  # Muestra la ventana principal

if __name__ == "__main__":
    root = tk.Tk()
    db = BibliotecaDB("biblioteca.db")
    app = VentanaPrincipal(root, db)
    root.mainloop()
