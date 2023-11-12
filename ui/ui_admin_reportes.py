import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
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
        self.treeview = ttk.Treeview(self.frame_resultados, columns=('Estado', 'Cantidad'), show='headings')
        self.treeview.heading('Estado', text='Estado')
        self.treeview.heading('Cantidad', text='Cantidad')
        self.treeview.pack(fill=tk.BOTH, expand=True)

    def volver_a_inicio(self):
        self.root.destroy()  # Cierra la ventana actual
        self.ventana_principal.volver_a_inicio()

    def mostrar_libros_por_estado(self):
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

        # Agregar el frame de resultados
            self.frame_resultados.pack()

        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Error al obtener la información: {str(e)}")


    def mostrar_suma_precio_extraviados(self):
        # Implement your logic for 'Suma Precio Extraviados' here
        pass

    def mostrar_solicitantes_libro(self):
        # Implement your logic for 'Solicitantes de Libro' here
        pass

    def mostrar_prestamos_socio(self):
        # Implement your logic for 'Prestamos por Socio' here
        pass

    def vaciar_resultados(self):
        # Limpiar la tabla
        for i in self.treeview.get_children():
            self.treeview.delete(i)
            # Ocultar el frame de resultados
            self.frame_resultados.pack_forget()

