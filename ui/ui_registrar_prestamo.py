#ui_registrar_prestamo.py

import tkinter as tk
from tkinter import messagebox
from datetime import datetime, timedelta
from tkcalendar import DateEntry  # Importar el nuevo módulo
from database.database import BibliotecaDB


class RegistrarPrestamosWindow:
    def __init__(self, root, ventana_principal, db):
        self.db = db
        self.root = root
        self.root.title("Registrar Nuevo Prestamo")
        self.ventana_principal = ventana_principal

        self.id_socio_label = tk.Label(root, text="ID Socio:")
        self.id_socio_label.pack()
        self.entry_id_socio = tk.Entry(root)
        self.entry_id_socio.pack()

        self.id_libro_label = tk.Label(root, text="ID Libro:")
        self.id_libro_label.pack()
        self.entry_id_libro = tk.Entry(root)
        self.entry_id_libro.pack()


        # Configurar fecha de préstamo como la fecha actual
        self.fecha_prestamo = tk.StringVar()
        self.fecha_prestamo.set(tk.StringVar().set("Fecha Préstamo"))
        self.entry_fecha_prestamo = DateEntry(root, textvariable=self.fecha_prestamo, date_pattern='dd/mm/yyyy')
        self.entry_fecha_prestamo.pack()

        # Configurar fecha de devolución predeterminada a 7 días después de la fecha actual
        fecha_actual = tk.StringVar().set(datetime.now().strftime("%d/%m/%Y"))
        fecha_devolucion_predeterminada = (datetime.now() + timedelta(days=7)).strftime("%d/%m/%Y")

        self.fecha_devolucion_label = tk.Label(root, text="Fecha Devolución:")
        self.fecha_devolucion_label.pack()
        self.entry_fecha_devolucion = DateEntry(root, date_pattern='dd/mm/yyyy', selectbackground='gray80', selectforeground='black')
        self.entry_fecha_devolucion.set_date(fecha_devolucion_predeterminada)
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

        # Convertir las fechas al formato de la base de datos
        fecha_prestamo = datetime.strptime(fecha_prestamo, "%d/%m/%Y").strftime('%Y-%m-%d %H:%M:%S')  # Ajuste aquí
        fecha_devolucion = datetime.strptime(fecha_devolucion, "%d/%m/%Y").strftime('%Y-%m-%d %H:%M:%S')

        self.db.registrar_prestamo(id_socio, id_libro, fecha_prestamo, fecha_devolucion)

    def volver_a_admin_prestamos(self):
        self.root.destroy()  # Cierra la ventana actual
        self.ventana_principal.root.deiconify()


