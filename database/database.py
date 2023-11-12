# database.py
from models.estado import *
import sqlite3
from tkinter import messagebox
from datetime import *

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
                fecha_prestamo DATE,
                fecha_devolucion DATE,
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
            fecha_prestamo = datetime.strptime(fecha_prestamo, "%Y-%m-%d %H:%M:%S")  # Ajuste aquí
            fecha_devolucion = datetime.strptime(fecha_devolucion, "%Y-%m-%d %H:%M:%S")  # Ajuste aquí

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
            # El estado es 1 para préstamo en curso, 2 terminado
            with self.conn:
                self.cursor.execute('''
                    INSERT INTO prestamo (id_socio, id_libro, estado, fecha_prestamo, fecha_devolucion)
                    VALUES (?, ?, 1, ?, ?)
                ''', (id_socio, id_libro, fecha_prestamo, fecha_devolucion))
                self.cursor.execute("UPDATE libros SET estado = 'Prestado' WHERE codigo = ?", (id_libro,))

            mensaje_exito = f"Prestamo registrado con éxito:\nID Socio: {int(id_socio)}\nCodigo libro: {str(id_libro)}\nFecha de prestamo: {fecha_prestamo.strftime('%d/%m/%Y')}\nFecha de devolucion: {fecha_devolucion.strftime('%d/%m/%Y')}"
            messagebox.showinfo("Éxito", mensaje_exito)
        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Error al guardar el préstamo: {str(e)}")

    def terminar_prestamo(self, id_prestamo):
        try:
            # Validar que el préstamo existe
            with self.conn:
                self.cursor.execute("SELECT id_prestamo, id_libro, fecha_prestamo, fecha_devolucion FROM prestamo WHERE id_prestamo = ?", (id_prestamo,))
                prestamo_info = self.cursor.fetchone()

            if not prestamo_info:
                mensaje_error = "El ID de préstamo no existe en la base de datos. Por favor, ingrese un ID de préstamo válido."
                messagebox.showerror("Error", mensaje_error)
                return

            # Convertir las cadenas de fecha a objetos datetime
            fecha_prestamo = datetime.strptime(prestamo_info[2], '%Y-%m-%d %H:%M:%S')
            fecha_devolucion = datetime.strptime(prestamo_info[3], '%Y-%m-%d %H:%M:%S')

            # Cambiar el estado del préstamo a 2 (indicando que está terminado)
            with self.conn:
                self.cursor.execute("UPDATE prestamo SET estado = 2 WHERE id_prestamo = ?", (id_prestamo,))

                # Cambiar el estado del libro a "Disponible" en la tabla libros
                self.cursor.execute("UPDATE libros SET estado = 'Disponible' WHERE codigo = ?", (prestamo_info[1],))

            mensaje_exito = f"Préstamo terminado con éxito. Libro marcado como 'Disponible'."
            messagebox.showinfo("Éxito", mensaje_exito)

        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Error al terminar el préstamo: {str(e)}")

    def terminar_prestamo_extravio_danio(self, id_prestamo):
        try:
            # Validar que el préstamo existe
            with self.conn:
                self.cursor.execute("SELECT id_prestamo, id_libro, estado FROM prestamo WHERE id_prestamo = ?", (id_prestamo,))
                prestamo_info = self.cursor.fetchone()

            if not prestamo_info:
                mensaje_error = "El ID de préstamo no existe en la base de datos. Por favor, ingrese un ID de préstamo válido."
                messagebox.showerror("Error", mensaje_error)
                return

            if prestamo_info[2] == 1:  # Verificar si el estado del préstamo es 'En curso'
                # Obtener el precio_reposicion del libro
                with self.conn:
                    self.cursor.execute("SELECT precio_reposicion FROM libros WHERE codigo = ?", (prestamo_info[1],))
                    precio_reposicion = self.cursor.fetchone()[0]

                # Cambiar el estado del préstamo a 2 (indicando que está terminado)
                with self.conn:
                    self.cursor.execute("UPDATE prestamo SET estado = 2 WHERE id_prestamo = ?", (id_prestamo,))

                    if prestamo_info[2] == 'Extraviado':
                        # Cambiar el estado del libro a "Disponible" solo si el estado del préstamo es 'Extraviado'
                        self.cursor.execute("UPDATE libros SET estado = 'Disponible' WHERE codigo = ?", (prestamo_info[1],))

                        mensaje_exito = f"Préstamo ID: {(id_prestamo)} - terminado con éxito. \nLibro  marcado como 'Disponible'.\n"
                        mensaje_exito += f"Precio Reposición del libro: {precio_reposicion}$."

                        messagebox.showinfo("Éxito", mensaje_exito)
                    else:
                        messagebox.showinfo("Éxito", "Préstamo terminado con éxito. Libro no marcado como 'Disponible' debido a que no está Extraviado.")
            else:
                messagebox.showinfo("Éxito", "Préstamo ya terminado o no está en curso.")

        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Error al terminar el préstamo: {str(e)}")

    def registrar_extraviados(self, prestamo_id):
        try:
            with self.conn:
                self.cursor.execute("SELECT id_prestamo, id_libro, fecha_devolucion FROM prestamo WHERE id_prestamo = ?", (prestamo_id,))
                prestamo_info = self.cursor.fetchone()

                if not prestamo_info:
                    mensaje_error = "El ID de préstamo no existe en la base de datos. Por favor, ingrese un ID de préstamo válido."
                    messagebox.showerror("Error", mensaje_error)
                    return

                fecha_devolucion = datetime.strptime(prestamo_info[2], '%Y-%m-%d %H:%M:%S').strftime('%d/%m/%Y')  # Ajuste aquí

                # Verificar si la fecha actual es mayor a 30 días después de la fecha de devolución
                if datetime.now() < (fecha_devolucion + timedelta(days=30)):
                    mensaje_error = "La fecha actual no es mayor a los 30 días pactados."
                    messagebox.showerror("Error", mensaje_error)
                    return

                with self.conn:
                    self.cursor.execute("UPDATE libros SET estado = 'Extraviado' WHERE codigo = ?", (prestamo_info[1],))

                mensaje_exito = f"Libro ID: {prestamo_info[1]} registrado como extraviado con éxito."
                messagebox.showinfo("Éxito", mensaje_exito)

        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Error al registrar el extravío del préstamo: {prestamo_id}")
               
   
    
    # En un método para verificar libros extraviados
    def verificar_libros_extraviados(self):
        try:
            # Obtener los préstamos con más de 30 días de demora
            with self.conn:
                self.cursor.execute("SELECT id_prestamo, id_libro FROM prestamo WHERE estado = 1 AND (julianday('now') - julianday(fecha_devolucion)) > 30")
                libros_extraviados = self.cursor.fetchall()

            # Cambiar el estado de los libros a 'Extraviado'
            for prestamo_info in libros_extraviados:
                with self.conn:
                    self.cursor.execute("UPDATE libros SET estado = 'Extraviado' WHERE codigo = ?", (prestamo_info[1],))

            mensaje_exito = f"{len(libros_extraviados)} libros marcados como 'Extraviados'."
            messagebox.showinfo("Éxito", mensaje_exito)

        except sqlite3.Error as e:
            messagebox.showerror("Error", f"Error al verificar libros extraviados: {str(e)}")
    
    def cerrar(self):
        self.conn.close()
    
