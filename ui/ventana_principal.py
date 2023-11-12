#ventana_principal.py

import tkinter as tk
from ui.ui_admin_socios import AdministracionSociosWindow  # Agregamos la nueva ventana
from ui.ui_admin_libros import AdministracionLibrosWindow
from ui.ui_reg_prestamo import RegistrarPrestamoWindow 
from ui.ui_reg_devolucion import RegistrarDevolucionWindow



class VentanaPrincipal:
    def __init__(self, root, db):
        self.root = root
        self.root.title("Biblioteca")
        self.db = db
        
        self.admin_libros_button = tk.Button(root, text="Administración de Libros", command=self.abrir_ventana_admin_libros)
        self.admin_libros_button.pack()
        
        self.admin_socios_button = tk.Button(root, text="Administración de Socios", command=self.abrir_ventana_admin_socios)
        self.admin_socios_button.pack()
        
        self.reg_prestamo_button = tk.Button(root, text="Registrar Prestamo de libro", command=self.abrir_ventana_reg_prestamo)
        self.reg_prestamo_button.pack()
        
        self.reg_devolucion_button = tk.Button(root, text="Registrar Devoluvion de libro", command=self.abrir_ventana_reg_devolucion)
        self.reg_devolucion_button.pack()
        
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
        
    def abrir_ventana_reg_prestamo(self):
        self.root.withdraw()
        ventana_reg_prestamo = tk.Toplevel(self.root)
        app = RegistrarPrestamoWindow(ventana_reg_prestamo, self, self.db)
        
    def abrir_ventana_reg_devolucion(self):
        self.root.withdraw()
        ventana_reg_devolucion = tk.Toplevel(self.root)
        app = RegistrarDevolucionWindow(ventana_reg_devolucion, self, self.db)
   
    def volver_a_inicio(self):
        self.ventana_principal.root.deiconify()  # Vuelve a mostrar la ventana de inicio
