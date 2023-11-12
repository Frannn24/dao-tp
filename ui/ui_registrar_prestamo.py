import tkinter as tk
from tkinter import messagebox
from logica.prestamo import Prestamo
import sqlite3


import tkinter as tk
from tkinter import messagebox

class RegistrarPrestamosWindow:
    def __init__(self,root, ventana_principal, db):
        self.db = db
        self.root = root
        self.root.title("Registrar Nuevo Prestamo")
        self.ventana_principal = ventana_principal


        self.id_socio_label = tk.Label(root, text="ID Socio:")
        self.id_socio_label.pack()
        self.entry_id_socio = tk.Entry(root)
        self.entry_id_socio.pack()
        
        
        self.id_libro_label =tk.Label(root, text="ID Libro:")
        self.id_libro_label.pack()
        self.entry_id_libro = tk.Entry(root)
        self.entry_id_libro.pack()
        
        
        self.fecha_prestamo_label=tk.Label(root, text="Fecha Préstamo:")
        self.fecha_prestamo_label.pack()
        self.entry_fecha_prestamo = tk.Entry(root)
        self.entry_fecha_prestamo.pack()
        
        
        self.fecha_devolucion_label=tk.Label(root, text="Fecha Devolución:")
        self.fecha_devolucion_label.pack()
        self.entry_fecha_devolucion = tk.Entry(root)
        self.entry_fecha_devolucion.pack()

        
        self.guardar_prestamo_button = tk.Button(root, text="Registrar Prestamo", command=self.registrar_prestamo)
        self.guardar_prestamo_button.pack()
        

        self.volver_button = tk.Button(root, text="Volver a Administración de Socios", command=self.volver_a_admin_prestamos)
        self.volver_button.pack()

    def registrar_prestamo(self):
        id_socio = self.entry_id_socio.get()
        id_libro = self.entry_id_libro.get()
        fecha_prestamo = self.entry_fecha_prestamo.get()
        fecha_devolucion = self.entry_fecha_devolucion.get()

        if not id_socio or not id_libro or not fecha_prestamo or not fecha_devolucion:
            messagebox.showerror("Error", "Por favor, complete todos los campos.")
            return
        self.db.registrar_prestamo(id_socio, id_libro, fecha_prestamo, fecha_devolucion)
        

    def volver_a_admin_prestamos(self):
        self.root.destroy()  # Cierra la ventana actual
        self.ventana_principal.root.deiconify()


