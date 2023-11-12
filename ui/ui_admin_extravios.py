import tkinter as tk
from tkinter import ttk
from ui.ui_registrar_extravio import RegistrarExtravioWindow

class AdministracionExtraviosWindow:
    def __init__(self, root, ventana_principal, db) -> None:
        self.root = root
        self.ventana_principal = ventana_principal
        self.root.title("Administrar Extravios")
        self.db = db
        
        
        self.guardar_extravio_button = tk.Button(root, text="Registrar Extravio", command=self.abrir_ventana_registrar_extravio)
        self.guardar_extravio_button.pack()
        
        self.volver_button = tk.Button(root, text="Volver a inicio", command=self.volver_a_inicio)
        self.volver_button.pack()
        
    def abrir_ventana_registrar_extravio(self):
        self.root.withdraw()
        ventana_registrar_extravio = tk.Toplevel(self.root)
        app = RegistrarExtravioWindow(ventana_registrar_extravio, self, self.db)
    
    def volver_a_inicio(self):
        self.root.destroy()  # Cierra la ventana actual
        self.ventana_principal.volver_a_inicio()