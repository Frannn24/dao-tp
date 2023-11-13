#ui_registrar_devolucion.py

import tkinter as tk
from tkinter import messagebox


class RegistrarDevolucionWindow:
    def __init__(self, root, ventana_principal, db) -> None:
        self.db = db
        self.root = root
        self.root.title("Devolucion")
        self.ventana_principal = ventana_principal
        
        
        # Configuración de estilo
        self.root.configure(bg='#EFEFEF')  # Color de fondo
        label_style = {'bg': '#EFEFEF', 'fg': '#333333', 'font': ('Arial', 12)}
        entry_style = {'bg': '#FFFFFF', 'fg': '#333333', 'font': ('Arial', 12)}
        button_style = {'bg': '#4CAF50', 'fg': 'white', 'font': ('Arial', 12)}

        self.id_prestamo_label = tk.Label(root, text="ID Prestamo:", **label_style)
        self.id_prestamo_label.pack(pady=5)
        self.entry_id_prestamo = tk.Entry(root, **entry_style)
        self.entry_id_prestamo.pack(pady=5)

        self.guardar_devolucion_button = tk.Button(root, text="Registrar Devolucion", command=self.registrar_devolucion, **button_style)
        self.guardar_devolucion_button.pack(pady=10)
        self.guardar_devolucion_ex_button = tk.Button(root, text="Registrar Devolucion extravio o daño", command=self.registrar_devolucion_extravio_danio, **button_style)
        self.guardar_devolucion_ex_button.pack(pady=10)

        self.volver_button = tk.Button(root, text="Volver a Administracion Devoluciones", command=self.volver_a_admin_devoluciones, **button_style)
        self.volver_button.pack(pady=10)

        # Configurar tamaño de la ventana y centrar en la pantalla
        self.root.geometry("400x300")  # Puedes ajustar este tamaño según tus preferencias
        self.center_window()

        # Manejar eventos de cambio de tamaño de la ventana
        self.root.bind("<Configure>", self.on_resize)

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
        
    def registrar_devolucion(self):
        id_prestamo = self.entry_id_prestamo.get()
        if not id_prestamo:
            messagebox.showerror("Error", "Por favor, complete todos los campos.")
            return
        self.db.terminar_prestamo(id_prestamo)
        
    def registrar_devolucion_extravio_danio(self):
        id_prestamo = self.entry_id_prestamo.get()
        if not id_prestamo:
            messagebox.showerror("Error", "Por favor, complete todos los campos.")
            return
        self.db.terminar_prestamo_extravio_danio(id_prestamo)
        
    def volver_a_admin_devoluciones(self):
        self.root.destroy()  # Cierra la ventana actual
        self.ventana_principal.root.deiconify()