# database.py

import sqlite3
from tkinter import messagebox

class BibliotecaDB:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS libros (
                codigo INTEGER PRIMARY KEY,
                titulo TEXT NOT NULL,
                precio_reposicion REAL,
                estado TEXT
            )
        """)

    def guardar_libro(self, libro):
        try:
            self.cursor.execute("INSERT INTO libros (codigo, titulo, precio_reposicion, estado) VALUES (?, ?, ?, ?)",
                                (libro.codigo, libro.titulo, libro.precio_reposicion, "Disponible"))
            self.conn.commit()
        except sqlite3.IntegrityError:
            # Si se produce una excepción de integridad, significa que el código ya existe
            mensaje_error = "El código ya existe en la base de datos."
            messagebox.showerror("Error", mensaje_error)  # Muestra un cuadro de diálogo de error
            # No es necesario volver a lanzar la excepción aquí

    def cerrar(self):
        self.conn.close()
