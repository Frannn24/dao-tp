import tkinter as tk
from ui import *
from database import BibliotecaDB

if __name__ == "__main__":
    root = tk.Tk()
    db = BibliotecaDB("biblioteca.db")
    app = VentanaPrincipal(root, db)
    root.mainloop()
