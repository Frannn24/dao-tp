import tkinter as tk
from tkinter import ttk
from ui.ui_guardar_devolucion import CrearGuardarDevolucion


class RegistrarDevolucionWindow():
    def __init__(self, root, ventana_principal, db) -> None:
        self.root = root
        self.ventana_principal = ventana_principal
        self.root.title("Registrar Devolucion")
        self.db = db
        
        self.guardar_devolucion_button = tk.Button(root, text="Guardar Devolución", command=self.abrir_ventana_guardar_devolucion)
        self.guardar_devolucion_button.pack()
        
        self.volver_button = tk.Button(root, text="Volver a inicio", command=self.volver_a_inicio)
        self.volver_button.pack()
        
    def abrir_ventana_guardar_devolucion(self):
        self.root.withdraw()
        ventana_guardar_devolucion= tk.Toplevel(self.root)
        app = CrearGuardarDevolucion(ventana_guardar_devolucion, self, self.db)
        
    def volver_a_inicio(self):
        self.root.destroy()  # Cierra la ventana actual
        self.ventana_principal.volver_a_inicio()