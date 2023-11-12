#ui_administracion_recalmos.py

import tkinter as tk
from tkinter import ttk


class AdministracionReportesWindow:
    def __init__(self, root, ventana_principal, db):
        self.root = root
        self.ventana_principal = ventana_principal
        self.root.title("Administración de Reportes")
        self.db = db

  
        self.volver_button = tk.Button(root, text="Volver a inicio", command=self.volver_a_inicio)
        self.volver_button.pack()

       
    
    def volver_a_inicio(self):
        self.root.destroy()  # Cierra la ventana actual
        self.ventana_principal.volver_a_inicio()