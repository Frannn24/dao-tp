#ui_guardar_libro.py

import tkinter as tk
from tkinter import messagebox
from models.libro import Libro
import sqlite3


class RegistrarLibroWindow:
    def __init__(self, root, ventana_principal, db):
        self.root = root
        self.root.title("Registrar Nuevo Libro")
        self.ventana_principal = ventana_principal
        self.db = db
        self.exito = False  # Variable para controlar si el libro se guardó con éxito

        # Configuración de estilo
        self.root.configure(bg='#EFEFEF')  # Color de fondo
        label_style = {'bg': '#EFEFEF', 'fg': '#333333', 'font': ('Arial', 12)}
        entry_style = {'bg': '#FFFFFF', 'fg': '#333333', 'font': ('Arial', 12)}
        button_style = {'bg': '#4CAF50', 'fg': 'white', 'font': ('Arial', 12)}

        self.codigo_label = tk.Label(root, text="Código:", **label_style)
        self.codigo_label.pack(pady=5)
        self.codigo_entry = tk.Entry(root, **entry_style)
        self.codigo_entry.pack(pady=5)

        self.titulo_label = tk.Label(root, text="Título:", **label_style)
        self.titulo_label.pack(pady=5)
        self.titulo_entry = tk.Entry(root, **entry_style)
        self.titulo_entry.pack(pady=5)

        self.precio_reposicion_label = tk.Label(root, text="Precio de Reposición:", **label_style)
        self.precio_reposicion_label.pack(pady=5)
        self.precio_reposicion_entry = tk.Entry(root, **entry_style)
        self.precio_reposicion_entry.pack(pady=5)

        self.crear_libro_button = tk.Button(root, text="Registrar Libro", command=self.registrar_libro, **button_style)
        self.crear_libro_button.pack(pady=10)

        self.volver_button = tk.Button(root, text="Volver a Administración de Libros", command=self.volver_a_admin_socios, **button_style)
        self.volver_button.pack(pady=10)

        self.exito_label = tk.Label(root, text="", **label_style)
        self.exito_label.pack()

        # Configurar tamaño de la ventana y centrar en la pantalla
        self.root.geometry("400x300")  # Puedes ajustar este tamaño según tus preferencias
        self.center_window()

        # Manejar eventos de cambio de tamaño de la ventana
        self.root.bind("<Configure>", self.on_resize)

    def center_window(self):
        # Centrar la ventana en la pantalla
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        window_width = self.root.winfo_reqwidth()
        window_height = self.root.winfo_reqheight()
        x = int((screen_width - window_width) / 2)
        y = int((screen_height - window_height) / 2)
        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    def on_resize(self, event):
        # Manejar evento de cambio de tamaño de la ventana
        self.center_window()


    def registrar_libro(self):
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

        nuevo_libro = Libro(codigo, titulo, precio_reposicion)
        self.db.registrar_libro(nuevo_libro)
        
   
    def volver_a_admin_socios(self):
        self.root.destroy()  # Cierra la ventana actual
        self.ventana_principal.root.deiconify()