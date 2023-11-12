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
                estado TEXT,
                eliminado INTEGER DEFAULT 0
            )
        """)
        
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS socios (
                id_socio INTEGER PRIMARY KEY,
                nombre TEXT NOT NULL,
                eliminado INTEGER DEFAULT 0
            )
        """)
        
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS prestamo (
                id_prestamo INTEGER PRIMARY KEY,
                id_socio INTEGER,
                id_libro INTEGER,
                estado INTEGER, 
                fecha_prestamo TEXT,
                fecha_devolucion TEXT,
                FOREIGN KEY (id_socio) REFERENCES socios (id_socio),
                FOREIGN KEY (id_libro) REFERENCES libros (codigo)
            )
        ''')


    def registrar_libro(self, libro):
        try:
            # Verificar si el código de libro ya existe
            self.cursor.execute("SELECT codigo FROM libros WHERE codigo = ?", (libro.codigo,))
            existe_libro = self.cursor.fetchone()

            if existe_libro:
                mensaje_error = "El código de libro ya existe en la base de datos. Por favor, ingrese un código único."
                messagebox.showerror("Error", mensaje_error)
            else:
                # Insertar el nuevo libro
                self.cursor.execute("INSERT INTO libros (codigo, titulo, precio_reposicion, estado) VALUES (?, ?, ?, ?)",
                                    (int(libro.codigo), str(libro.titulo), float(libro.precio_reposicion), "Disponible"))
                self.conn.commit()
                mensaje_exito = f"Libro registrado con éxito: \nCodigo: {int(libro.codigo)} \nTitulo: {str(libro.titulo)} \nNombre: {float(libro.precio_reposicion)} \nEstado: Disponible"
                messagebox.showinfo("Éxito", mensaje_exito)

        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Error al guardar el libro: {str(e)}")
    
    def registrar_socio(self, socio):
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
                mensaje_exito = f"Socio registrado con éxito:\nID: {int(socio.id_socio)}\nNombre: {str(socio.nombre)}"
                messagebox.showinfo("Éxito", mensaje_exito)

        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Error al guardar el socio: {str(e)}")
   
   
    def registrar_prestamo(self, id_socio, id_libro, fecha_prestamo, fecha_devolucion):
        try:
            # Validar que id_socio existe en la tabla socios
            with self.conn:
                self.cursor.execute("SELECT id_socio FROM socios WHERE id_socio = ?", (id_socio,))
                existe_socio = self.cursor.fetchone()

            if not existe_socio:
                mensaje_error = "El ID de socio no existe en la base de datos. Por favor, ingrese un ID de socio válido."
                messagebox.showerror("Error", mensaje_error)
                return

            # Validar que id_socio no tenga más de tres préstamos activos
            with self.conn:
                self.cursor.execute("SELECT COUNT(*) FROM prestamo WHERE id_socio = ? AND estado = 1", (id_socio,))
                prestamos_activos = self.cursor.fetchone()[0]

            if prestamos_activos >= 3:
                mensaje_error = "Este socio ya tiene tres préstamos activos. No se pueden agregar más préstamos."
                messagebox.showerror("Error", mensaje_error)
                return

            # Validar que id_libro existe en la tabla libros
            with self.conn:
                self.cursor.execute("SELECT codigo FROM libros WHERE codigo = ? AND estado = 'Disponible'", (id_libro,))
                existe_libro = self.cursor.fetchone()

            if not existe_libro:
                mensaje_error = "El código de libro no existe en la base de datos. Por favor, ingrese un código de libro válido."
                messagebox.showerror("Error", mensaje_error)
                return

            # Si todos los criterios se cumplen, proceder con la inserción del préstamo
            # El estado es 1 para prestamo en curso, 2 terminado
            with self.conn:
                self.cursor.execute('''
                    INSERT INTO prestamo (id_socio, id_libro, estado, fecha_prestamo, fecha_devolucion)
                    VALUES (?, ?, 1, ?, ?)
                ''', (id_socio, id_libro, fecha_prestamo, fecha_devolucion))
                self.cursor.execute("UPDATE libros SET estado = 'Prestado' WHERE codigo = ?", (id_libro,))

            mensaje_exito = f"Prestamo registrado con éxito:\nID Socio: {int(id_socio)}\nCodigo libro: {str(id_libro)}\nFecha de prestamo: {str(fecha_prestamo)}\nFecha de devolucion: {str(fecha_devolucion)}"    
            messagebox.showinfo("Éxito", mensaje_exito)
        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Error al guardar el préstamo: {str(e)}")
        
        

    def terminar_prestamo(self, id_prestamo):

            try:
                # Validar que el préstamo existe
                with self.conn:
                    self.cursor.execute("SELECT id_prestamo, id_libro FROM prestamo WHERE id_prestamo = ?", (id_prestamo,))
                    prestamo_info = self.cursor.fetchone()

                if not prestamo_info:
                    mensaje_error = "El ID de préstamo no existe en la base de datos. Por favor, ingrese un ID de préstamo válido."
                    messagebox.showerror("Error", mensaje_error)
                    return

                # Cambiar el estado del préstamo a 2 (indicando que está terminado)
                with self.conn:
                    self.cursor.execute("UPDATE prestamo SET estado = 2 WHERE id_prestamo = ?", (id_prestamo,))

                    # Cambiar el estado del libro a "Disponible" en la tabla libros
                    self.cursor.execute("UPDATE libros SET estado = 'Disponible' WHERE codigo = ?", (prestamo_info[1],))

                messagebox.showinfo("Éxito", "Préstamo terminado con éxito. Libro marcado como 'Disponible'.")

            except sqlite3.Error as e:
                messagebox.showerror("Error", f"Error al terminar el préstamo: {str(e)}")
        
        
    def terminar_prestamo_extravio_danio(self, id_prestamo):
            try:
                # Validar que el préstamo existe
                with self.conn:
                    self.cursor.execute("SELECT id_prestamo, id_libro FROM prestamo WHERE id_prestamo = ?", (id_prestamo,))
                    prestamo_info = self.cursor.fetchone()

                if not prestamo_info:
                    mensaje_error = "El ID de préstamo no existe en la base de datos. Por favor, ingrese un ID de préstamo válido."
                    messagebox.showerror("Error", mensaje_error)
                    return

                # Obtener el precio_reposicion del libro
                with self.conn:
                    self.cursor.execute("SELECT precio_reposicion FROM libros WHERE codigo = ?", (prestamo_info[1],))
                    precio_reposicion = self.cursor.fetchone()[0]

                # Cambiar el estado del préstamo a 2 (indicando que está terminado)
                with self.conn:
                    self.cursor.execute("UPDATE prestamo SET estado = 2 WHERE id_prestamo = ?", (id_prestamo,))

                    # Cambiar el estado del libro a "Disponible" en la tabla libros
                    self.cursor.execute("UPDATE libros SET estado = 'Disponible' WHERE codigo = ?", (prestamo_info[1],))

                mensaje_exito = f"Préstamo ID: {(id_prestamo)} - terminado con éxito. \nLibro  marcado como 'Disponible'.\n"
                mensaje_exito += f"Precio Reposición del libro: {precio_reposicion}."

                messagebox.showinfo("Éxito", mensaje_exito)

            except sqlite3.Error as e:
                messagebox.showerror("Error", f"Error al terminar el préstamo: {str(e)}")

    
    def cerrar(self):
        self.conn.close()
    
