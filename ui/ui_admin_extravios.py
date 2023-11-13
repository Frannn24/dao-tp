#ui_admin_extravios.py

import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime, timedelta
import sqlite3

class AdministracionExtraviosWindow:
    def __init__(self, root, ventana_principal, db) -> None:
        self.root = root
        self.ventana_principal = ventana_principal
        self.root.title("Administrar Extravíos")
        self.db = db
        self.libros_prestados = []  # Lista para almacenar libros prestados

        # Configuración de estilo
        self.root.configure(bg='#EFEFEF')  # Color de fondo
        button_style = {'bg': '#4CAF50', 'fg': 'white', 'font': ('Arial', 12)}
        title_style = {'bg': '#EFEFEF', 'fg': '#333333', 'font': ('Arial', 20, 'bold')}

        # División en dos frames
        self.frame_botones = tk.Frame(root, bg='#EFEFEF')
        self.frame_botones.pack(side=tk.LEFT, padx=10, pady=10)

        self.frame_resultados = tk.Frame(root, bg='#EFEFEF')
        self.frame_resultados.pack(side=tk.RIGHT, padx=10, pady=10)

        # Configurar tamaño de la ventana principal y centrar en la pantalla
        self.root.geometry("800x600")  # Puedes ajustar este tamaño según tus preferencias
        self.center_window()

        # Manejar eventos de cambio de tamaño de la ventana
        self.root.bind("<Configure>", self.on_resize)

        self.mostrar_libros_button = tk.Button(self.frame_botones, text="Mostrar Libros", command=self.mostrar_libros, **button_style)
        self.mostrar_libros_button.pack(pady=5, fill=tk.X)

        self.guardar_extravio_button = tk.Button(self.frame_botones, text="Registrar Extravío", command=self.registrar_extravio, **button_style)
        self.guardar_extravio_button.pack(pady=5, fill=tk.X)

        self.volver_button = tk.Button(self.frame_botones, text="Volver a inicio", command=self.volver_a_inicio, **button_style)
        self.volver_button.pack(pady=5, fill=tk.X)

        # Área para mostrar los resultados
        self.treeview = ttk.Treeview(self.frame_resultados, columns=('ID Libro', 'Fecha Devolución', 'Días de Demora'), show='headings', style='Custom.Treeview')
        self.treeview.heading('ID Libro', text='ID Libro')
        self.treeview.heading('Fecha Devolución', text='Fecha Devolución')
        self.treeview.heading('Días de Demora', text='Días de Demora')
        self.treeview.pack(fill=tk.BOTH, expand=True)  # Agregado este comando para mostrar el Treeview

        # Configurar estilo para la tabla
        style = ttk.Style()
        style.configure("Custom.Treeview.Heading", font=('Arial', 12, 'bold'))
        style.configure("Custom.Treeview", highlightthickness=0, bd=0, font=('Arial', 11))
        style.layout("Custom.Treeview", [('Custom.Treeview.treearea', {'sticky': 'nswe'})])

    def center_window(self):
        # Centrar la ventana en la pantalla
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        window_width = self.root.winfo_reqwidth()
        window_height = self.root.winfo_reqheight()
        x = int((screen_width - window_width) / 2)
        y = int((screen_height - window_height) / 2)
        self.root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    def on_resize(self, event):
        # Manejar evento de cambio de tamaño de la ventana
        self.center_window()

    def mostrar_libros(self):
        try:
            # Obtener libros en estado 'Prestado' con fecha de devolución superada por 30 días
            with self.db.conn:
                query = (
                    "SELECT id_libro, fecha_devolucion FROM prestamo "
                    "WHERE estado = 1 AND fecha_devolucion < ? AND id_libro IN (SELECT codigo FROM libros WHERE estado = 'Prestado')"
                )
                print("Consulta SQL (Mostrar Libros):", query)
                self.db.cursor.execute(query, ((datetime.now() - timedelta(days=30)).strftime('%Y-%m-%d %H:%M:%S'),))
                libros_prestamo = self.db.cursor.fetchall()

            # Limpiar la tabla
            for i in self.treeview.get_children():
                self.treeview.delete(i)

            # Agregar libros prestados a la tabla
            for libro in libros_prestamo:
                fecha_devolucion = datetime.strptime(libro[1], '%Y-%m-%d %H:%M:%S')
                dias_demora = (datetime.now() - fecha_devolucion).days
                self.treeview.insert('', 'end', values=(libro[0], libro[1], dias_demora))

        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Error al mostrar los libros: {str(e)}")

    def registrar_extravio(self):
        try:
            # Obtener libros en estado 'Prestado' con fecha de devolución superada por 30 días
            with self.db.conn:
                query = (
                    "SELECT id_libro, fecha_devolucion FROM prestamo "
                    "WHERE estado = 1 AND fecha_devolucion < ? AND id_libro IN (SELECT codigo FROM libros WHERE estado = 'Prestado')"
                )
                print("Consulta SQL (Registrar Extravío):", query)
                self.db.cursor.execute(query, ((datetime.now() - timedelta(days=30)).strftime('%Y-%m-%d %H:%M:%S'),))
                libros_prestamo = self.db.cursor.fetchall()

            # Cambiar el estado de los libros a 'Extraviado'
            with self.db.conn:
                libros_actualizados = 0
                for libro in libros_prestamo:
                    if libro[0] not in self.libros_prestados:
                        self.db.cursor.execute("UPDATE libros SET estado = 'Extraviado' WHERE codigo = ?", (libro[0],))
                        libros_actualizados += 1
                        self.libros_prestados.append(libro[0])

            mensaje_exito = f"{libros_actualizados} libro(s) marcado(s) como 'Extraviado' con éxito."
            messagebox.showinfo("Éxito", mensaje_exito)

            # Limpiar la tabla después de realizar el cambio de estado
            for i in self.treeview.get_children():
                self.treeview.delete(i)

            # Vaciar la lista de libros prestados
            self.libros_prestados = []

        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Error al registrar el extravío de los libros: {str(e)}")

    def volver_a_inicio(self):
        self.root.destroy()  # Cierra la ventana actual
        self.ventana_principal.volver_a_inicio()
