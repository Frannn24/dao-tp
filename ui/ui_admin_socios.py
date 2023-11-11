# administracion_socios.py
import tkinter as tk
from tkinter import ttk
from ui.ui_guardar_socio import CrearSocioWindow


class AdministracionSociosWindow:
    def __init__(self, root, ventana_principal, db):
        self.root = root
        self.ventana_principal = ventana_principal
        self.root.title("Administración de Socios")
        self.db = db

        self.guardar_socio_button = tk.Button(root, text="Guardar Socio", command=self.abrir_ventana_guardar_socio)
        self.guardar_socio_button.pack()
        
        self.volver_button = tk.Button(root, text="Volver a inicio", command=self.volver_a_inicio)
        self.volver_button.pack()


    def abrir_ventana_guardar_socio(self):
        self.root.withdraw()
        ventana_guardar_socio = tk.Toplevel(self.root)
        app = CrearSocioWindow(ventana_guardar_socio, self, self.db)
       
    
    def volver_a_inicio(self):
        self.root.destroy()  # Cierra la ventana actual
        self.ventana_principal.volver_a_inicio()