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

        # Configuración de estilo
        self.root.configure(bg='#EFEFEF')  # Color de fondo
        button_style = {'bg': '#4CAF50', 'fg': 'white', 'font': ('Arial', 12)}
        title_style = {'bg': '#EFEFEF', 'fg': '#333333', 'font': ('Arial', 20, 'bold')}

        # División en dos frames
        self.frame_botones = tk.Frame(root, bg='#EFEFEF')
        self.frame_botones.pack(side=tk.LEFT, padx=10, pady=10)

        self.frame_resultados = tk.Frame(root, bg='#EFEFEF')
        self.frame_resultados.pack(side=tk.RIGHT, padx=10, pady=10)

        # Inicialmente ocultar el frame de resultados
        self.frame_resultados.pack_forget()
        
        # Configurar tamaño de la ventana principal y centrar en la pantalla
        self.root.geometry("800x600")  # Ajusta según tus preferencias
        self.center_window()
        
        # Manejar eventos de cambio de tamaño de la ventana
        self.root.bind("<Configure>", self.on_resize)
        

        self.registrar_socio_button = tk.Button(self.frame_botones, text="Registrar Socio", command=self.abrir_ventana_registrar_socio, **button_style)
        self.registrar_socio_button.pack(pady=5, fill=tk.X)

        self.ver_socios_button = tk.Button(self.frame_botones, text="Ver Socios", command=self.mostrar_socios, **button_style)
        self.ver_socios_button.pack(pady=5, fill=tk.X)

        self.volver_button = tk.Button(self.frame_botones, text="Volver a inicio", command=self.volver_a_inicio, **button_style)
        self.volver_button.pack(pady=5, fill=tk.X)

        # Área para mostrar los resultados
        self.treeview = ttk.Treeview(self.frame_resultados, columns=('ID Socio', 'Nombre'), show='headings', style='Custom.Treeview')
        self.treeview.heading('ID Socio', text='ID Socio')
        self.treeview.heading('Nombre', text='Nombre')
        self.treeview.tag_configure('oddrow', background='#EFEFEF')
        self.treeview.tag_configure('evenrow', background='white')
        self.treeview.pack(fill=tk.BOTH, expand=True)

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
