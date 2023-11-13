#ui_guardar_socio.py

import tkinter as tk
from tkinter import messagebox
from models.socio import Socio
import sqlite3


class RegistrarSocioWindow:
    def __init__(self, root, ventana_principal, db):
        self.root = root
        self.root.title("Registrar Nuevo Socio")
        self.ventana_principal = ventana_principal
        self.db = db
        self.exito = False  # Variable para controlar si el socio se guardó con éxito

        # Configuración de estilo
        self.root.configure(bg='#EFEFEF')  # Color de fondo
        label_style = {'bg': '#EFEFEF', 'fg': '#333333', 'font': ('Arial', 12)}
        entry_style = {'bg': '#FFFFFF', 'fg': '#333333', 'font': ('Arial', 12)}
        button_style = {'bg': '#4CAF50', 'fg': 'white', 'font': ('Arial', 12)}

        self.id_socio_label = tk.Label(root, text="ID:", **label_style)
        self.id_socio_label.pack(pady=5)
        self.id_socio_entry = tk.Entry(root, **entry_style)
        self.id_socio_entry.pack(pady=5)

        self.nombre_label = tk.Label(root, text="Nombre:", **label_style)
        self.nombre_label.pack(pady=5)
        self.nombre_entry = tk.Entry(root, **entry_style)
        self.nombre_entry.pack(pady=5)

        self.registrar_socio_button = tk.Button(root, text="Registrar Socio", command=self.registrar_socio, **button_style)
        self.registrar_socio_button.pack(pady=10)

        self.volver_button = tk.Button(root, text="Volver a Administración de Socios", command=self.volver_a_admin_socios, **button_style)
        self.volver_button.pack(pady=10)

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
        
    def registrar_socio(self):
        id_socio = self.id_socio_entry.get()
        nombre = self.nombre_entry.get()

        # Validaciones de datos aquí
        if not id_socio.isdigit() or not nombre:
            mensaje_error = "Por favor, ingrese datos válidos."
            messagebox.showerror("Error", mensaje_error)
            return  # Detiene la ejecución en caso de error de validación

        id_socio = int(id_socio)

        if id_socio < 1:
            mensaje_error = "El ID debe ser números enteros positivos."
            messagebox.showerror("Error", mensaje_error)
            return  # Detiene la ejecución en caso de error de validación
        nuevo_socio = Socio(id_socio, nombre)
        self.db.registrar_socio(nuevo_socio)
        
               
    def volver_a_admin_socios(self):
        self.root.destroy()  # Cierra la ventana actual
        self.ventana_principal.root.deiconify()