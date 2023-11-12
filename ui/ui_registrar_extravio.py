import tkinter as tk
from tkinter import messagebox

class RegistrarExtravioWindow:
    def __init__(self, root, ventana_principal, db) -> None:
        self.db = db
        self.root = root
        self.root.title("Extravio")
        self.ventana_principal = ventana_principal
        
        self.id_prestamo_label = tk.Label(root, text="ID Prestamo: ")
        self.id_prestamo_label.pack()
        self.entry_id_prestamo = tk.Entry(root)
        self.entry_id_prestamo.pack()
        
        self.guardar_extravio_button = tk.Button(root, text="Registrar Extravio", command=self.registrar_extravio)
        self.guardar_extravio_button.pack()
        
        self.volver_button = tk.Button(root, text="Volver a Administracion Extravios", command=self.volver_a_admin_extravios)
        self.volver_button.pack()
        
        
    def registrar_extravio(self):
        id_prestamo = self.entry_id_prestamo.get()
        if not id_prestamo:
            messagebox.showerror("Error", "Por favor, complete el campo ID Prestamo.")
            return
        self.db.registrar_extraviados(id_prestamo)
    
    
    def volver_a_admin_extravios(self):
        self.root.destroy()  # Cierra la ventana actual
        self.ventana_principal.root.deiconify()
        
