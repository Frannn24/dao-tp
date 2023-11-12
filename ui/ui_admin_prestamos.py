import tkinter as tk
from tkinter import ttk
from ui.ui_registrar_prestamo import RegistrarPrestamosWindow


class AdministracionPrestamosWindow:
    def __init__(self, root, ventana_principal, db):
        self.root = root
        self.ventana_principal = ventana_principal
        self.root.title("Registrar Prestamo")
        self.db = db
        
        self.registrar_prestamo_button = tk.Button(root, text="Registrar Prestamo", command=self.abrir_ventana_registrar_prestamo)
        self.registrar_prestamo_button.pack()
        
        self.volver_button = tk.Button(root, text="Volver a inicio", command=self.volver_a_inicio)
        self.volver_button.pack()
        
    def abrir_ventana_registrar_prestamo(self):
        self.root.withdraw()
        ventana_registrar_prestamo = tk.Toplevel(self.root)
        app = RegistrarPrestamosWindow(ventana_registrar_prestamo, self, self.db)
        
        
    def volver_a_inicio(self):
        self.root.destroy()  # Cierra la ventana actual
        self.ventana_principal.volver_a_inicio()