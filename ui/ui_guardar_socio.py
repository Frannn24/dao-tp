import tkinter as tk
from tkinter import messagebox
from models.socio import Socio
#from database.database import BibliotecaDB
import sqlite3
from ui.utilidades import *

class CrearSocioWindow:
    def __init__(self, root, ventana_principal, db):
        self.root = root
        self.root.title("Crear Nuevo Socio")
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


        self.crear_socio_button = tk.Button(root, text="Crear Socio", command=self.crear_socio)
        self.crear_socio_button.pack()

        self.volver_button = tk.Button(root, text="Volver a inicio", command=self.volver_a_inicio)
        self.volver_button.pack()

    def crear_socio(self):
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

        try:
            nuevo_socio = Socio(id_socio, nombre)
            self.db.guardar_socio(nuevo_socio)
            # Solo establecer 'exito' en True si no se lanzó ninguna excepción
            self.exito = True
        except ValueError:
            mensaje_error = "El ID de socio debe ser un número entero."
            messagebox.showerror("Error", mensaje_error)
            self.exito = False
            return
        except sqlite3.IntegrityError:
            mensaje_error = "El ID de socio ya existe en la base de datos. Por favor, ingrese un ID único."
            messagebox.showerror("Error", mensaje_error)
            self.exito = False
            return

        # Muestra el mensaje de éxito solo si no se lanzó ninguna excepción
        if self.exito:
            messagebox.showinfo("Éxito", "Socio guardado con éxito")
            
    def volver_a_inicio(self):
        
        volver_a_ventana_inicio(self.root)
        self.ventana_principal.volver_a_ventana_inicio()
