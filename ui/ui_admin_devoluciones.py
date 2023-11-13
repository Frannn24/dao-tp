#ui_admin_devoluciones.py

import tkinter as tk
from tkinter import ttk
from ui.ui_registrar_devolucion import RegistrarDevolucionWindow


class AdministradorDevolucionesWindow():
    def __init__(self, root, ventana_principal, db) -> None:
        self.root = root
        self.ventana_principal = ventana_principal
        self.root.title("Administrados Devoluciones")
        self.db = db
        
        # Configuración de estilo
        self.root.configure(bg='#EFEFEF')  # Color de fondo
        button_style = {'bg': '#4CAF50', 'fg': 'white', 'font': ('Arial', 12)}
        title_style = {'bg': '#EFEFEF', 'fg': '#333333', 'font': ('Arial', 20, 'bold')}

        # División en dos frames
        self.frame_botones = tk.Frame(root, bg='#EFEFEF')
        self.frame_botones.pack(side=tk.LEFT, padx=10, pady=10)

        # Botones
        self.guardar_devolucion_button = tk.Button(self.frame_botones, text="Registrar Devolución", command=self.abrir_ventana_registrar_devolucion, **button_style)
        self.guardar_devolucion_button.pack(pady=5, fill=tk.X)

        self.volver_button = tk.Button(self.frame_botones, text="Volver a inicio", command=self.volver_a_inicio, **button_style)
        self.volver_button.pack(pady=5, fill=tk.X)
        
    def abrir_ventana_registrar_devolucion(self):
        self.root.withdraw()
        ventana_registrar_devolucion= tk.Toplevel(self.root)
        app = RegistrarDevolucionWindow(ventana_registrar_devolucion, self, self.db)
        
    def volver_a_inicio(self):
        self.root.destroy()  # Cierra la ventana actual
        self.ventana_principal.volver_a_inicio()