import tkinter as tk
from ui.ventana_principal import *

from database.database import BibliotecaDB

if __name__ == "__main__":
    root = tk.Tk()
    db = BibliotecaDB("biblioteca.db")
    app = VentanaPrincipal(root, db)
    root.mainloop()
