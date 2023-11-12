#ui_admin_prestamos.py

import tkinter as tk
from tkinter import ttk
from ui.ui_registrar_prestamo import RegistrarPrestamosWindow
import sqlite3
import tkinter.messagebox as messagebox


class AdministracionPrestamosWindow:
    def __init__(self, root, ventana_principal, db):
        self.root = root
        self.ventana_principal = ventana_principal
        self.root.title("Administración de Préstamos")
        self.db = db

        # División en dos frames
        self.frame_botones = tk.Frame(root)
        self.frame_botones.pack(side=tk.LEFT, padx=10, pady=10)

        self.frame_resultados = tk.Frame(root)
        self.frame_resultados.pack(side=tk.RIGHT, padx=10, pady=10)

        # Inicialmente ocultar el frame de resultados
        self.frame_resultados.pack_forget()

        self.registrar_prestamo_button = tk.Button(self.frame_botones, text="Registrar Préstamo", command=self.abrir_ventana_registrar_prestamo)
        self.registrar_prestamo_button.pack()

        self.ver_prestamos_button = tk.Button(self.frame_botones, text="Ver Préstamos", command=self.mostrar_prestamos)
        self.ver_prestamos_button.pack()

        self.volver_button = tk.Button(self.frame_botones, text="Volver a inicio", command=self.volver_a_inicio)
        self.volver_button.pack()

        # Área para mostrar los resultados
        self.treeview = ttk.Treeview(self.frame_resultados, columns=('ID Préstamo', 'ID Socio', 'ID Libro', 'Estado', 'Fecha Préstamo', 'Fecha Devolución'), show='headings')
        self.treeview.heading('ID Préstamo', text='ID Préstamo')
        self.treeview.heading('ID Socio', text='ID Socio')
        self.treeview.heading('ID Libro', text='ID Libro')
        self.treeview.heading('Estado', text='Estado')
        self.treeview.heading('Fecha Préstamo', text='Fecha Préstamo')
        self.treeview.heading('Fecha Devolución', text='Fecha Devolución')
        self.treeview.pack(fill=tk.BOTH, expand=True)

    def abrir_ventana_registrar_prestamo(self):
        self.root.withdraw()
        ventana_registrar_prestamo = tk.Toplevel(self.root)
        app = RegistrarPrestamosWindow(ventana_registrar_prestamo, self, self.db)

    def volver_a_inicio(self):
        self.root.destroy()  # Cierra la ventana actual
        self.ventana_principal.volver_a_inicio()

    def mostrar_prestamos(self):
        try:
            # Obtener todos los préstamos de la base de datos
            with self.db.conn:
                self.db.cursor.execute("SELECT id_prestamo, id_socio, id_libro, estado, fecha_prestamo, fecha_devolucion FROM prestamo")
                prestamos = self.db.cursor.fetchall()

            # Limpiar la tabla
            for i in self.treeview.get_children():
                self.treeview.delete(i)

            # Agregar préstamos a la tabla
            for prestamo in prestamos:
                self.treeview.insert('', 'end', values=prestamo)

            # Cambiar las columnas del Treeview según el botón presionado
            self.treeview['columns'] = ('ID Préstamo', 'ID Socio', 'ID Libro', 'Estado', 'Fecha Préstamo', 'Fecha Devolución')
            self.treeview.heading('ID Préstamo', text='ID Préstamo')
            self.treeview.heading('ID Socio', text='ID Socio')
            self.treeview.heading('ID Libro', text='ID Libro')
            self.treeview.heading('Estado', text='Estado')
            self.treeview.heading('Fecha Préstamo', text='Fecha Préstamo')
            self.treeview.heading('Fecha Devolución', text='Fecha Devolución')

            # Mostrar el frame de resultados
            self.frame_resultados.pack()

        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Error al obtener la información: {str(e)}")
