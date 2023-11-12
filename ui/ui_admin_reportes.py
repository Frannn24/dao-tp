import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter.simpledialog import askstring
import sqlite3

class AdministracionReportesWindow:
    def __init__(self, root, ventana_principal, db):
        self.root = root
        self.ventana_principal = ventana_principal
        self.root.title("Administración de Reportes")
        self.db = db

        # División en dos frames
        self.frame_botones = tk.Frame(root)
        self.frame_botones.pack(side=tk.LEFT, padx=10, pady=10)

        self.frame_resultados = tk.Frame(root)
        self.frame_resultados.pack(side=tk.RIGHT, padx=10, pady=10)

        # Initially hide the frame
        self.frame_resultados.pack_forget()

        self.volver_button = tk.Button(self.frame_botones, text="Volver a inicio", command=self.volver_a_inicio)
        self.volver_button.pack()

        # Botones para cada reporte
        self.libros_estado_button = tk.Button(self.frame_botones, text="Libros por Estado", command=self.mostrar_libros_por_estado)
        self.libros_estado_button.pack()

        self.suma_precio_extraviados_button = tk.Button(self.frame_botones, text="Suma Precio Extraviados", command=self.mostrar_suma_precio_extraviados)
        self.suma_precio_extraviados_button.pack()

        self.solicitantes_libro_button = tk.Button(self.frame_botones, text="Solicitantes de Libro", command=self.mostrar_solicitantes_libro)
        self.solicitantes_libro_button.pack()

        self.prestamos_socio_button = tk.Button(self.frame_botones, text="Prestamos por Socio", command=self.mostrar_prestamos_socio)
        self.prestamos_socio_button.pack()

        # Botón para vaciar el frame de resultados
        self.vaciar_resultados_button = tk.Button(self.frame_botones, text="Vaciar Resultados", command=self.vaciar_resultados)
        self.vaciar_resultados_button.pack()

        # Área para mostrar los resultados
        self.treeview = ttk.Treeview(self.frame_resultados, columns=('', ''), show='headings')
        self.treeview.heading('', text='')  # Add empty heading initially
        self.treeview.pack(fill=tk.BOTH, expand=True)

    def volver_a_inicio(self):
        self.root.destroy()  # Cierra la ventana actual
        self.ventana_principal.volver_a_inicio()

    def mostrar_libros_por_estado(self):
        # Cambiar las columnas del Treeview según el botón presionado
        self.treeview['columns'] = ('Estado', 'Cantidad')
        self.treeview.heading('Estado', text='Estado')
        self.treeview.heading('Cantidad', text='Cantidad')
        try:
            # Obtener la cantidad de libros en cada estado
            with self.db.conn:
                self.db.cursor.execute("SELECT estado, COUNT(*) FROM libros GROUP BY estado")
                resultados = self.db.cursor.fetchall()

            # Limpiar la tabla
            for i in self.treeview.get_children():
                self.treeview.delete(i)

            # Agregar resultados a la tabla
            for resultado in resultados:
                self.treeview.insert('', 'end', values=resultado)

            # Mostrar el frame de resultados
            self.frame_resultados.pack()

        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Error al obtener la información: {str(e)}")

    def mostrar_suma_precio_extraviados(self):
        # Cambiar las columnas del Treeview según el botón presionado
        self.treeview['columns'] = ('Suma Precio Extraviados','')
        self.treeview.heading('Suma Precio Extraviados', text='Suma Precio Extraviados')
        try:
        # Obtener la suma del precio de reposición de todos los libros extraviados
            with self.db.conn:
                self.db.cursor.execute("SELECT SUM(precio_reposicion) FROM libros WHERE estado = 'Extraviado'")
                suma_precio_extraviados = self.db.cursor.fetchone()[0]

            # Limpiar la tabla
            for i in self.treeview.get_children():
                self.treeview.delete(i)

            # Agregar la suma a la tabla
            self.treeview.insert('', 'end', values=('Suma Precio Extraviados', round(suma_precio_extraviados, 2)))

            # Mostrar el frame de resultados
            self.frame_resultados.pack()

        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Error al obtener la información: {str(e)}")

    def mostrar_solicitantes_libro(self):
        self.treeview['columns'] = ('Solicitante','')
        self.treeview.heading('Solicitante', text='Solicitante')
        try:
            # Prompt the user for the book title
            libro_titulo = askstring("Solicitantes de Libro", "Ingrese el título del libro:")

            if libro_titulo is None:
                return  # Return if the user cancels the input

            print(f"Buscando solicitantes para el libro: {libro_titulo}")  # Add this line for debugging

            # Obtener los solicitantes del libro específico
            with self.db.conn:
                self.db.cursor.execute("""
                    SELECT s.nombre
                    FROM socios s
                    JOIN prestamo p ON s.id_socio = p.id_socio
                    JOIN libros l ON l.codigo = p.id_libro
                    WHERE l.titulo = ?
                """, (libro_titulo,))
                solicitantes = self.db.cursor.fetchall()

            print("Solicitantes encontrados:", solicitantes)  # Add this line for debugging

            # Limpiar la tabla
            for i in self.treeview.get_children():
                self.treeview.delete(i)

            # Agregar solicitantes a la tabla
            for solicitante in solicitantes:
                self.treeview.insert('', 'end', values=(solicitante[0],))

            #Mostrar el frame de resultados
            self.frame_resultados.pack()

        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Error al obtener la información: {str(e)}")


    def mostrar_prestamos_socio(self):
        self.treeview['columns'] = ('ID Préstamo', 'ID Libro', 'Estado', 'Fecha Préstamo', 'Fecha Devolución')
        self.treeview.heading('ID Préstamo', text='ID Préstamo')
        self.treeview.heading('ID Libro', text='ID Libro')
        self.treeview.heading('Estado', text='Estado')
        self.treeview.heading('Fecha Préstamo', text='Fecha Préstamo')
        self.treeview.heading('Fecha Devolución', text='Fecha Devolución')

        try:
            # Prompt the user for the member ID
            id_socio = askstring("Prestamos por Socio", "Ingrese el número de socio:")

            if id_socio is None:
                return  # Return if the user cancels the input

            print(f"Buscando préstamos para el socio: {id_socio}")  # Add this line for debugging

            # Obtener los préstamos del socio específico
            with self.db.conn:
                self.db.cursor.execute("""
                    SELECT id_prestamo, id_libro, estado, fecha_prestamo, fecha_devolucion
                    FROM prestamo
                    WHERE id_socio = ?
                """, (id_socio,))
                prestamos = self.db.cursor.fetchall()

            print("Préstamos encontrados:", prestamos)  # Add this line for debugging

            # Limpiar la tabla
            for i in self.treeview.get_children():
                self.treeview.delete(i)

            # Agregar préstamos a la tabla
            for prestamo in prestamos:
                self.treeview.insert('', 'end', values=prestamo)

            # Mostrar el frame de resultados
            self.frame_resultados.pack()

        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Error al obtener la información: {str(e)}")


    def vaciar_resultados(self):
        # Limpiar la tabla
        for i in self.treeview.get_children():
            self.treeview.delete(i)
        
        # Ocultar el frame de resultados
        self.frame_resultados.pack_forget()

