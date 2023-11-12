import tkinter as tk
from tkinter import messagebox


class CrearGuardarDevolucion:
    def __init__(self, root, ventana_principal, db) -> None:
        self.db = db
        self.root = root
        self.root.title("Devolucion")
        self.ventana_principal = ventana_principal
        
        
        self.id_prestamo_label = tk.Label(root, text="ID Prestamo: ")
        self.id_prestamo_label.pack()
        self.entry_id_prestamo = tk.Entry(root)
        self.entry_id_prestamo.pack()
        
        self.guardar_devolucion_button = tk.Button(root, text="Registrar Devolucion", command=self.guardar_devolucion)
        self.guardar_devolucion_button.pack()
        self.guardar_devolucion_ex_button = tk.Button(root, text="Registrar Devolucion extravio o daño", command=self.guardar_devolucion_extravio_danio)
        self.guardar_devolucion_ex_button.pack()
        
        self.volver_button = tk.Button(root, text="Volver a Registrar Devolucion", command=self.volver_a_reg_devolucion)
        self.volver_button.pack()
        
    def guardar_devolucion(self):
        id_prestamo = self.entry_id_prestamo.get()
        if not id_prestamo:
            messagebox.showerror("Error", "Por favor, complete todos los campos.")
            return
        self.db.terminar_prestamo(id_prestamo)
        
    def guardar_devolucion_extravio_danio(self):
        id_prestamo = self.entry_id_prestamo.get()
        if not id_prestamo:
            messagebox.showerror("Error", "Por favor, complete todos los campos.")
            return
        self.db.terminar_prestamo_extravio_danio(id_prestamo)