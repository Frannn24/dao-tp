# ui.py
"""
import tkinter as tk
from tkinter import messagebox
from models.socio import Socio
from models.libro import Libro
from database.database import *
import sqlite3


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
        self.root.destroy()  # Cierra la ventana actual
        self.ventana_principal.volver_a_ventana_inicio()  # Llama al método de la ventana principal para volver a la ventana "Guardar Socio"



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

        self.volver_button = tk.Button(root, text="Volver a inicio", command=self.volver_a_inicio)
        self.volver_button.pack()
        
        self.exito_label = tk.Label(root, text="")
        self.exito_label.pack()


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

        if self.exito:
            messagebox.showinfo("Éxito", "Libro guardado con éxito")
        

    def volver_a_inicio(self):
        self.root.destroy()  # Cierra la ventana actual
        self.ventana_principal.volver_a_ventana_inicio()  # Llama al método de la ventana principal para volver a la ventana "Guardar Libro"

class VentanaPrincipal:
    def __init__(self, root, db):
        self.root = root
        self.root.title("Biblioteca")
        self.db = db

        self.guardar_libro_button = tk.Button(root, text="Guardar Libro", command=self.abrir_ventana_guardar_libro)
        self.guardar_libro_button.pack()
        
        self.guardar_socio_button = tk.Button(root, text="Guardar Socio", command=self.abrir_ventana_guardar_socio)
        self.guardar_socio_button.pack()

    def abrir_ventana_guardar_libro(self):
        self.root.withdraw()
        ventana_guardar_libro = tk.Toplevel(self.root)
        app = CrearLibroWindow(ventana_guardar_libro, self, self.db)

    def abrir_ventana_guardar_socio(self):
        self.root.withdraw()
        ventana_guardar_socio = tk.Toplevel(self.root)
        app = CrearSocioWindow(ventana_guardar_socio, self, self.db)

    def volver_a_ventana_inicio(self):
        self.root.deiconify()  # Muestra la ventana principal
"""
