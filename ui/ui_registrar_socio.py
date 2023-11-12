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

        self.id_socio_label = tk.Label(root, text="ID:")
        self.id_socio_label.pack()
        self.id_socio_entry = tk.Entry(root)
        self.id_socio_entry.pack()

        self.nombre_label = tk.Label(root, text="Nombre:")
        self.nombre_label.pack()
        self.nombre_entry = tk.Entry(root)
        self.nombre_entry.pack()


        self.registrar_socio_button = tk.Button(root, text="Registrar Socio", command=self.registrar_socio)
        self.registrar_socio_button.pack()

        self.volver_button = tk.Button(root, text="Volver a Administración de Socios", command=self.volver_a_admin_socios)
        self.volver_button.pack()

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