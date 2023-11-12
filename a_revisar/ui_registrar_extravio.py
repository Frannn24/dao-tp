import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime, timedelta

class RegistrarExtravioWindow:
    def __init__(self, root, ventana_principal, db) -> None:
        self.db = db
        self.root = root
        self.root.title("Extravio")
        self.ventana_principal = ventana_principal

        # Primer frame con botones
        self.frame_botones = tk.Frame(root)
        self.frame_botones.pack(side=tk.LEFT, padx=10, pady=10)

        self.id_prestamo_label = tk.Label(self.frame_botones, text="ID Prestamo: ")
        self.id_prestamo_label.pack()
        self.entry_id_prestamo = tk.Entry(self.frame_botones)
        self.entry_id_prestamo.pack()

        self.guardar_extravio_button = tk.Button(self.frame_botones, text="Registrar Extravio", command=self.registrar_extravio)
        self.guardar_extravio_button.pack()

        self.volver_button = tk.Button(self.frame_botones, text="Volver a Administracion Extravios", command=self.volver_a_admin_extravios)
        self.volver_button.pack()

        # Segundo frame con lista de libros prestados y fecha de devolución superada
        self.frame_resultados = tk.Frame(root)
        self.frame_resultados.pack(side=tk.RIGHT, padx=10, pady=10)

        # Initially hide the frame
        self.frame_resultados.pack_forget()

        self.treeview = ttk.Treeview(self.frame_resultados, columns=('ID Libro', 'Fecha Devolución'), show='headings')
        self.treeview.heading('ID Libro', text='ID Libro')
        self.treeview.heading('Fecha Devolución', text='Fecha Devolución')
        self.treeview.pack(fill=tk.BOTH, expand=True)

    def registrar_extravio(self):
        id_prestamo = self.entry_id_prestamo.get()
        if not id_prestamo:
            messagebox.showerror("Error", "Por favor, complete el campo ID Prestamo.")
            return

        try:
            # Obtener libros prestados con fecha de devolución superada
            with self.db.conn:
                self.db.cursor.execute("SELECT id_libro, fecha_devolucion FROM prestamo WHERE estado = 1 AND fecha_devolucion < ?", (datetime.now(),))
                libros_prestamo = self.db.cursor.fetchall()

            # Limpiar la tabla
            for i in self.treeview.get_children():
                self.treeview.delete(i)

            # Agregar libros prestados a la tabla
            for libro in libros_prestamo:
                self.treeview.insert('', 'end', values=libro)

            # Mostrar el frame de resultados
            self.frame_resultados.pack()

            # Cambiar el estado de los libros a 'Extraviado'
            with self.db.conn:
                for libro in libros_prestamo:
                    self.db.cursor.execute("UPDATE libros SET estado = 'Extraviado' WHERE codigo = ?", (libro[0],))

            mensaje_exito = "Libros marcados como 'Extraviado' con éxito."
            messagebox.showinfo("Éxito", mensaje_exito)

        except Exception as e:
            messagebox.showerror("Error", f"Error al registrar el extravío de los libros: {str(e)}")

    def volver_a_admin_extravios(self):
        self.root.destroy()  # Cierra la ventana actual
        self.ventana_principal.root.deiconify()
