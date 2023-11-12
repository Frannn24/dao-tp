#ui_admin_socios.py

import tkinter as tk
from tkinter import ttk
from ui.ui_registrar_socio import RegistrarSocioWindow
import sqlite3
import tkinter.messagebox as messagebox

class AdministracionSociosWindow:
    def __init__(self, root, ventana_principal, db):
        self.root = root
        self.ventana_principal = ventana_principal
        self.root.title("Administración de Socios")
        self.db = db

        # División en dos frames
        self.frame_botones = tk.Frame(root)
        self.frame_botones.pack(side=tk.LEFT, padx=10, pady=10)

        self.frame_resultados = tk.Frame(root)
        self.frame_resultados.pack(side=tk.RIGHT, padx=10, pady=10)

        # Inicialmente ocultar el frame de resultados
        self.frame_resultados.pack_forget()

        self.registrar_socio_button = tk.Button(self.frame_botones, text="Registrar Socio", command=self.abrir_ventana_registrar_socio)
        self.registrar_socio_button.pack()

        self.ver_socios_button = tk.Button(self.frame_botones, text="Ver Socios", command=self.mostrar_socios)
        self.ver_socios_button.pack()

        self.volver_button = tk.Button(self.frame_botones, text="Volver a inicio", command=self.volver_a_inicio)
        self.volver_button.pack()

        # Área para mostrar los resultados
        self.treeview = ttk.Treeview(self.frame_resultados, columns=('ID Socio', 'Nombre'), show='headings')
        self.treeview.heading('ID Socio', text='ID Socio')
        self.treeview.heading('Nombre', text='Nombre')
        self.treeview.pack(fill=tk.BOTH, expand=True)

    def abrir_ventana_registrar_socio(self):
        self.root.withdraw()
        ventana_registrar_socio = tk.Toplevel(self.root)
        app = RegistrarSocioWindow(ventana_registrar_socio, self, self.db)

    def volver_a_inicio(self):
        self.root.destroy()  # Cierra la ventana actual
        self.ventana_principal.volver_a_inicio()

    def mostrar_socios(self):
        try:
            # Obtener todos los socios de la base de datos
            with self.db.conn:
                self.db.cursor.execute("SELECT id_socio, nombre FROM socios")
                socios = self.db.cursor.fetchall()

            # Limpiar la tabla
            for i in self.treeview.get_children():
                self.treeview.delete(i)

            # Agregar socios a la tabla
            for socio in socios:
                self.treeview.insert('', 'end', values=socio)

            # Cambiar las columnas del Treeview según el botón presionado
            self.treeview['columns'] = ('ID Socio', 'Nombre')
            self.treeview.heading('ID Socio', text='ID Socio')
            self.treeview.heading('Nombre', text='Nombre')

            # Mostrar el frame de resultados
            self.frame_resultados.pack()

        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Error al obtener la información: {str(e)}")
