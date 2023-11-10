# database.py
from models.estado import *
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
        
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS socios (
                id_socio INTEGER PRIMARY KEY,
                nombre TEXT NOT NULL,
                id_prestamo INTEGER
            )
        """)

    def guardar_libro(self, libro):
        try:
            self.cursor.execute("INSERT INTO libros (codigo, titulo, precio_reposicion, estado) VALUES (?, ?, ?, ?)",
                                (int(libro.codigo), str(libro.titulo), float(libro.precio_reposicion), "Disponible"))
            self.conn.commit()
        except sqlite3.IntegrityError:
            # Si se produce una excepción de integridad, significa que el código ya existe
            mensaje_error = "El código ya existe en la base de datos."
            messagebox.showerror("Error", mensaje_error)  # Muestra un cuadro de diálogo de error
            # No es necesario volver a lanzar la excepción aquí
            
    def guardar_socio(self, socio):
        try:
            # Verificar si el ID de socio ya existe
            self.cursor.execute("SELECT id_socio FROM socios WHERE id_socio = ?", (socio.id_socio,))
            existe_socio = self.cursor.fetchone()

            if existe_socio:
                mensaje_error = "El ID de socio ya existe en la base de datos. Por favor, ingrese un ID único."
                messagebox.showerror("Error", mensaje_error)
            else:
                # Insertar el nuevo socio
                self.cursor.execute("INSERT INTO socios (id_socio, nombre) VALUES (?, ?)",
                                    (int(socio.id_socio), str(socio.nombre)))
                self.conn.commit()
                messagebox.showinfo("Éxito", "Socio guardado con éxito")

        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Error al guardar el socio: {str(e)}")
    """     
    def prestar_libro(self, libro):
        prestado = Prestado()
        prestado.actualizar_estado(libro)

    def devolver_libro(self, libro, dias_de_retraso):
        if dias_de_retraso > 30:
            extraviado = Extraviado()
            extraviado.actualizar_estado(libro)
        else:
            disponible = Disponible()
            disponible.actualizar_estado(libro)
"""
    def cerrar(self):
        self.conn.close()
    
