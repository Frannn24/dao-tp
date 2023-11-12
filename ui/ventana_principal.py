#ventana_principal.py

import tkinter as tk
from ui.ui_admin_socios import AdministracionSociosWindow  # Agregamos la nueva ventana
from ui.ui_admin_libros import AdministracionLibrosWindow
from ui.ui_admin_prestamos import AdministracionPrestamosWindow 
from ui.ui_admin_reportes import AdministracionReportesWindow



class VentanaPrincipal:
    def __init__(self, root, db):
        self.root = root
        self.root.title("Biblioteca")
        self.db = db
        
        self.admin_libros_button = tk.Button(root, text="Administración de Libros", command=self.abrir_ventana_admin_libros)
        self.admin_libros_button.pack()
        
        self.admin_socios_button = tk.Button(root, text="Administración de Socios", command=self.abrir_ventana_admin_socios)
        self.admin_socios_button.pack()
        
        self.reg_prestamo_button = tk.Button(root, text="Administracion de Prestamos de libro", command=self.abrir_ventana_admin_prestamo)
        self.reg_prestamo_button.pack()
        
        self.reg_prestamo_button = tk.Button(root, text="Administracion de Reportes", command=self.abrir_ventana_admin_reportes)
        self.reg_prestamo_button.pack()
        
        self.reg_devolucion_button = tk.Button(root, text="Registrar Devoluvion de libro", command=self.abrir_ventana_reg_devolucion)
        self.reg_devolucion_button.pack()
        
    def abrir_ventana_admin_libros(self):
        self.root.withdraw()
        ventana_admin_libros = tk.Toplevel(self.root)
        app = AdministracionLibrosWindow(ventana_admin_libros, self, self.db)
        #self.root.deiconify()
        
    def abrir_ventana_admin_socios(self):
        self.root.withdraw()
        ventana_admin_socios = tk.Toplevel(self.root)
        app = AdministracionSociosWindow(ventana_admin_socios, self, self.db)
        #self.root.deiconify()
        
    def abrir_ventana_admin_prestamo(self):
        self.root.withdraw()
        ventana_admin_prestamos = tk.Toplevel(self.root)
        app = AdministracionPrestamosWindow(ventana_admin_prestamos, self, self.db)
        
    def abrir_ventana_admin_reportes(self):
        self.root.withdraw()
        ventana_admin_reportes = tk.Toplevel(self.root)
        app = AdministracionReportesWindow(ventana_admin_reportes, self, self.db)
        
    def abrir_ventana_reg_devolucion(self):
        """
        self.root.withdraw()
        ventana_reg_devolucion = tk.Toplevel(self.root)
        app = RegistrarDevolucionWindow(ventana_reg_devolucion, self, self.db)
        """
    def volver_a_inicio(self):
        self.root.deiconify()  # Vuelve a mostrar la ventana de inicio
