#ventana_principal.py

import tkinter as tk
from ui.ui_admin_socios import AdministracionSociosWindow  # Agregamos la nueva ventana
from ui.ui_admin_libros import AdministracionLibrosWindow 



class VentanaPrincipal:
    def __init__(self, root, db):
        self.root = root
        self.root.title("Biblioteca")
        self.db = db
        
        self.admin_libros_button = tk.Button(root, text="Administración de Libros", command=self.abrir_ventana_admin_libros)
        self.admin_libros_button.pack()
        
        self.admin_socios_button = tk.Button(root, text="Administración de Socios", command=self.abrir_ventana_admin_socios)
        self.admin_socios_button.pack()
        
    def abrir_ventana_admin_libros(self):
        self.root.withdraw()
        ventana_admin_libros = tk.Toplevel(self.root)
        app = AdministracionLibrosWindow(ventana_admin_libros, self, self.db)
        self.root.deiconify()
        
    def abrir_ventana_admin_socios(self):
        self.root.withdraw()
        ventana_admin_socios = tk.Toplevel(self.root)
        app = AdministracionSociosWindow(ventana_admin_socios, self, self.db)
        self.root.deiconify()
   
    def volver_a_inicio(self):
        self.ventana_principal.root.deiconify()  # Vuelve a mostrar la ventana de inicio
