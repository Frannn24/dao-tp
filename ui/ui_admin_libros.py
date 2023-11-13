import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from ui.ui_registrar_libro import RegistrarLibroWindow
import sqlite3

class AdministracionLibrosWindow:
    def __init__(self, root, ventana_principal, db):
        self.root = root
        self.ventana_principal = ventana_principal
        self.root.title("Administración de Libros")
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
        
        # Initially hide the frame
        self.frame_resultados.pack_forget()

        # Configurar tamaño de la ventana principal y centrar en la pantalla
        self.root.geometry("800x600")  # Puedes ajustar este tamaño según tus preferencias
        self.center_window()

        # Manejar eventos de cambio de tamaño de la ventana
        self.root.bind("<Configure>", self.on_resize)


        self.registrar_libro_button = tk.Button(self.frame_botones, text="Registrar Libro", command=self.abrir_ventana_registrar_libro, **button_style)
        self.registrar_libro_button.pack(pady=5, fill=tk.X)

        self.ver_libros_button = tk.Button(self.frame_botones, text="Ver Libros", command=self.mostrar_libros, **button_style)
        self.ver_libros_button.pack(pady=5, fill=tk.X)

        self.volver_button = tk.Button(self.frame_botones, text="Volver a inicio", command=self.volver_a_inicio, **button_style)
        self.volver_button.pack(pady=5, fill=tk.X)

        # Área para mostrar los resultados
        self.treeview = ttk.Treeview(self.frame_resultados, columns=('Código', 'Título', 'Precio Reposición', 'Estado'), show='headings', style="My.Treeview")
        self.treeview.heading('Código', text='Código')
        self.treeview.heading('Título', text='Título')
        self.treeview.heading('Precio Reposición', text='Precio Reposición')
        self.treeview.heading('Estado', text='Estado')
        self.treeview.pack(fill=tk.BOTH, expand=True)  # Agregado este comando para mostrar el Treeview

        # Configurar estilo para la tabla
        style = ttk.Style()
        style.configure("My.Treeview.Heading", font=('Arial', 12, 'bold'))
        style.configure("My.Treeview", highlightthickness=0, bd=0, font=('Arial', 11))
        style.layout("My.Treeview", [('My.Treeview.treearea', {'sticky': 'nswe'})])

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

    def abrir_ventana_registrar_libro(self):
        self.root.withdraw()
        ventana_registrar_libro = tk.Toplevel(self.root)
        app = RegistrarLibroWindow(ventana_registrar_libro, self, self.db)

    def volver_a_inicio(self):
        self.root.destroy()  # Cierra la ventana actual
        self.ventana_principal.volver_a_inicio()

    def mostrar_libros(self):
        try:
            # Obtener todos los libros de la base de datos
            with self.db.conn:
                self.db.cursor.execute("SELECT codigo, titulo, precio_reposicion, estado FROM libros")
                libros = self.db.cursor.fetchall()

            # Limpiar la tabla
            for i in self.treeview.get_children():
                self.treeview.delete(i)

            # Agregar libros a la tabla
            for libro in libros:
                self.treeview.insert('', 'end', values=libro)

            # Mostrar el frame de resultados
            self.frame_resultados.pack()

        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Error al obtener la información: {str(e)}")
