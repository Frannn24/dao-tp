#ui_administracion_libros.py
import tkinter as tk
from tkinter import ttk
from ui.ui_guardar_libro import CrearLibroWindow


class AdministracionLibrosWindow:
    def __init__(self, root, ventana_principal, db):
        self.root = root
        self.ventana_principal = ventana_principal
        self.root.title("Administración de Libros")
        self.db = db

        self.guardar_libro_button = tk.Button(root, text="Guardar Libro", command=self.abrir_ventana_guardar_libro)
        self.guardar_libro_button.pack()
        
        self.volver_button = tk.Button(root, text="Volver a inicio", command=self.volver_a_inicio)
        self.volver_button.pack()


    def abrir_ventana_guardar_libro(self):
        self.root.withdraw()
        ventana_guardar_libro = tk.Toplevel(self.root)
        app = CrearLibroWindow(ventana_guardar_libro, self, self.db)
       
    
    def volver_a_inicio(self):
        self.root.destroy()  # Cierra la ventana actual
        self.ventana_principal.volver_a_inicio()