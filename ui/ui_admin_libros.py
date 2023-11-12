#ui_admin_libros.py

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from ui.ui_registrar_libro import RegistrarLibroWindow
import sqlite3

class AdministracionLibrosWindow:
    def __init__(self, root, ventana_principal, db):
        self.root = root
        self.ventana_principal = ventana_principal
        self.root.title("Administración de Libros")
        self.db = db

        # División en dos frames
        self.frame_botones = tk.Frame(root)
        self.frame_botones.pack(side=tk.LEFT, padx=10, pady=10)

        self.frame_resultados = tk.Frame(root)
        self.frame_resultados.pack(side=tk.RIGHT, padx=10, pady=10)

        # Initially hide the frame
        self.frame_resultados.pack_forget()

        self.registrar_libro_button = tk.Button(self.frame_botones, text="Registrar Libro", command=self.abrir_ventana_registrar_libro)
        self.registrar_libro_button.pack()

        self.ver_libros_button = tk.Button(self.frame_botones, text="Ver Libros", command=self.mostrar_libros)
        self.ver_libros_button.pack()

        self.volver_button = tk.Button(self.frame_botones, text="Volver a inicio", command=self.volver_a_inicio)
        self.volver_button.pack()

        # Área para mostrar los resultados
        self.treeview = ttk.Treeview(self.frame_resultados, columns=('Código', 'Título', 'Precio Reposición', 'Estado'), show='headings')
        self.treeview.heading('Código', text='Código')
        self.treeview.heading('Título', text='Título')
        self.treeview.heading('Precio Reposición', text='Precio Reposición')
        self.treeview.heading('Estado', text='Estado')
        self.treeview.pack(fill=tk.BOTH, expand=True)  # Agregado este comando para mostrar el Treeview

    def abrir_ventana_registrar_libro(self):
        self.root.withdraw()
        ventana_registrar_libro = tk.Toplevel(self.root)
        app = RegistrarLibroWindow(ventana_registrar_libro, self, self.db)

    def volver_a_inicio(self):
        self.root.destroy()  # Cierra la ventana actual
        self.ventana_principal.volver_a_inicio()

    def mostrar_libros(self):
        try:
            # Obtener todos los libros de la base de datos
            with self.db.conn:
                self.db.cursor.execute("SELECT codigo, titulo, precio_reposicion, estado FROM libros")
                libros = self.db.cursor.fetchall()

            # Limpiar la tabla
            for i in self.treeview.get_children():
                self.treeview.delete(i)

            # Agregar libros a la tabla
            for libro in libros:
                self.treeview.insert('', 'end', values=libro)

            # Mostrar el frame de resultados
            self.frame_resultados.pack()

        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Error al obtener la información: {str(e)}")
