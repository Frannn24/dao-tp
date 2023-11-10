#ventana_principal.py
import tkinter as tk
#from tkinter import messagebox
#from models.socio import Socio
#from models.libro import Libro
#from database.database import BibliotecaDB
#from ui.ui_guardar_socio import *
#from ui.ui_guardar_libro import *
from ui.utilidades import volver_a_ventana_inicio



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
        from ui.ui_guardar_libro import CrearLibroWindow
        app = CrearLibroWindow(ventana_guardar_libro, self, self.db)

    def abrir_ventana_guardar_socio(self):
        self.root.withdraw()
        ventana_guardar_socio = tk.Toplevel(self.root)
        from ui.ui_guardar_socio import CrearSocioWindow
        app = CrearSocioWindow(ventana_guardar_socio, self, self.db)
    
    def volver_a_ventana_inicio(self):
        volver_a_ventana_inicio(self.root)

def volver_a_ventana_inicio(root):
    root.deiconify()