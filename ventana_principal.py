"""
Aca tendria que poderse crear la ventana principal, hay que cambiar los self para que respondan a un import de lo que se necesite

from ui import *

class VentanaPrincipal:
    def __init__(self, root, db):
        self.root = root
        self.root.title("Biblioteca")
        self.db = db

        self.guardar_libro_button = tk.Button(root, text="Guardar Libro", command=self.abrir_ventana_guardar_libro)
        self.guardar_libro_button.pack()

    def abrir_ventana_guardar_libro(self):
        self.root.withdraw()
        ventana_guardar_libro = tk.Toplevel(self.root)
        app = CrearLibroWindow(ventana_guardar_libro, self, self.db)

    def volver_a_ventana_guardar_libro(self):
        self.root.deiconify()  # Muestra la ventana principal
"""