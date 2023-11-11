import tkinter as tk
from tkinter import ttk
from ui.ui_guardar_prestamo import CrearGuardarPrestamo


class RegistrarPrestamoWindow:
    def __init__(self, root, ventana_principal, db):
        self.root = root
        self.ventana_principal = ventana_principal
        self.root.title("Registrar Prestamo")
        self.db = db
        
        self.guardar_prestamo_button = tk.Button(root, text="Guardar Prestamo", command=self.abrir_ventana_guardar_prestamo)
        self.guardar_prestamo_button.pack()
        
        self.volver_button = tk.Button(root, text="Volver a inicio", command=self.volver_a_inicio)
        self.volver_button.pack()
        
    def abrir_ventana_guardar_prestamo(self):
        self.root.withdraw()
        ventana_guardar_prestamo = tk.Toplevel(self.root)
        app = CrearGuardarPrestamo(ventana_guardar_prestamo, self, self.db)
        
        
    def volver_a_inicio(self):
        self.root.destroy()  # Cierra la ventana actual
        self.ventana_principal.volver_a_inicio()