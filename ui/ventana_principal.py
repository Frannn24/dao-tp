#ventana_principal.py

import tkinter as tk
from ui.ui_admin_socios import AdministracionSociosWindow  # Agregamos la nueva ventana
from ui.ui_admin_libros import AdministracionLibrosWindow
from ui.ui_admin_prestamos import AdministracionPrestamosWindow 
from ui.ui_admin_reportes import AdministracionReportesWindow
from ui.ui_admin_devoluciones import AdministradorDevolucionesWindow
from ui.ui_admin_extravios import AdministracionExtraviosWindow
from datetime import *



class VentanaPrincipal:
    _instance = None  # Variable de clase para almacenar la instancia única

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self, root, db):
        if not hasattr(self, 'initialized'):  # Asegura que la inicialización solo se haga una vez
            self.initialized = True
            self.root = root
            self.root.title("Biblioteca")
            self.db = db
            
            # Configuración de estilo
            self.root.configure(bg='#EFEFEF')  # Color de fondo
            button_style = {'bg': '#4CAF50', 'fg': 'white', 'font': ('Arial', 12)}
            title_style = {'bg': '#EFEFEF', 'fg': '#333333', 'font': ('Arial', 20, 'bold')}
            datetime_style = {'bg': '#EFEFEF', 'fg': '#555555', 'font': ('Arial', 12)}

            # Frame principal
            main_frame = tk.Frame(root, bg='#EFEFEF')
            main_frame.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)

            # Título y Fecha/Hora Frame
            title_datetime_frame = tk.Frame(main_frame, bg='#EFEFEF')
            title_datetime_frame.pack(expand=True, fill=tk.BOTH)

            # Título
            self.title_label = tk.Label(title_datetime_frame, text="Biblioteca", **title_style)
            self.title_label.pack(pady=10, side=tk.LEFT)


            # Botones Frame
            buttons_frame = tk.Frame(main_frame, bg='#EFEFEF')
            buttons_frame.pack(expand=True, fill=tk.BOTH)

            # Configurar tamaño de la ventana principal y centrar en la pantalla
            self.root.geometry("800x600")  # Puedes ajustar este tamaño según tus preferencias
            self.center_window()

            # Manejar eventos de cambio de tamaño de la ventana
            self.root.bind("<Configure>", self.on_resize)

            # Botones
            self.admin_libros_button = tk.Button(buttons_frame, text="Administración de Libros", command=self.abrir_ventana_admin_libros, **button_style)
            self.admin_libros_button.pack(pady=5, expand=True, fill=tk.X, side=tk.TOP)

            self.admin_socios_button = tk.Button(buttons_frame, text="Administración de Socios", command=self.abrir_ventana_admin_socios, **button_style)
            self.admin_socios_button.pack(pady=5, expand=True, fill=tk.X, side=tk.TOP)

            self.reg_prestamo_button = tk.Button(buttons_frame, text="Administracion de Prestamos de libro", command=self.abrir_ventana_admin_prestamo, **button_style)
            self.reg_prestamo_button.pack(pady=5, expand=True, fill=tk.X, side=tk.TOP)

            self.reg_devolucion_button = tk.Button(buttons_frame, text="Registrar Devolucion de libro", command=self.abrir_ventana_reg_devolucion, **button_style)
            self.reg_devolucion_button.pack(pady=5, expand=True, fill=tk.X, side=tk.TOP)
            
            self.reg_extravio_button = tk.Button(buttons_frame, text="Registrar Extravio de libro", command=self.abrir_ventana_reg_extravio, **button_style)
            self.reg_extravio_button.pack(pady=5, expand=True, fill=tk.X, side=tk.TOP)

            self.reg_prestamo_button = tk.Button(buttons_frame, text="Administracion de Reportes", command=self.abrir_ventana_admin_reportes, **button_style)
            self.reg_prestamo_button.pack(pady=5, expand=True, fill=tk.X, side=tk.TOP)

           
            

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
        
        self.root.withdraw()
        ventana_reg_devolucion = tk.Toplevel(self.root)
        app = AdministradorDevolucionesWindow(ventana_reg_devolucion, self, self.db)
    
    def abrir_ventana_reg_extravio(self):
        self.root.withdraw()
        ventana_reg_extravio = tk.Toplevel(self.root)
        app = AdministracionExtraviosWindow(ventana_reg_extravio, self, self.db)
        
    def volver_a_inicio(self):
        self.root.deiconify()  # Vuelve a mostrar la ventana de inicio
