import sqlite3
from datetime import datetime, timedelta

class DataInserter:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def insert_books(self):
        for i in range(1, 201):
            estado_libro = 'Disponible' if i % 2 == 0 else 'Prestado'
            self.cursor.execute("INSERT INTO libros (codigo, titulo, precio_reposicion, estado) VALUES (?, ?, ?, ?)",
                                (i, f"Libro-{i}", 10.99 * i, estado_libro))
            self.conn.commit()

    def insert_socios(self):
        for i in range(1, 101):
            self.cursor.execute("INSERT INTO socios (id_socio, nombre) VALUES (?, ?)",
                                (i, f"Socio-{i}"))
            self.conn.commit()

    def insert_prestamos(self):
        # Efectuar 50 préstamos con la fecha actual < fecha devolución
        for i in range(1, 51):
            id_socio = i
            id_libro = i

            fecha_prestamo = (datetime.now() - timedelta(days=i)).strftime('%Y-%m-%d %H:%M:%S')
            fecha_devolucion = (datetime.now() + timedelta(days=i)).strftime('%Y-%m-%d %H:%M:%S')

            self.cursor.execute('''
                INSERT INTO prestamo (id_socio, id_libro, estado, fecha_prestamo, fecha_devolucion)
                VALUES (?, ?, 1, ?, ?)
            ''', (id_socio, id_libro, fecha_prestamo, fecha_devolucion))
            self.conn.commit()

            self.cursor.execute("UPDATE libros SET estado = 'Prestado' WHERE codigo = ?", (id_libro,))
            self.conn.commit()

        # Efectuar 50 préstamos con la fecha actual > fecha devolución + 30 días
        for i in range(51, 101):
            id_socio = i
            id_libro = i

            fecha_prestamo = (datetime.now() - timedelta(days=i)).strftime('%Y-%m-%d %H:%M:%S')
            fecha_devolucion = (datetime.now() + timedelta(days=i + 30)).strftime('%Y-%m-%d %H:%M:%S')

            self.cursor.execute('''
                INSERT INTO prestamo (id_socio, id_libro, estado, fecha_prestamo, fecha_devolucion)
                VALUES (?, ?, 1, ?, ?)
            ''', (id_socio, id_libro, fecha_prestamo, fecha_devolucion))
            self.conn.commit()

            self.cursor.execute("UPDATE libros SET estado = 'Prestado' WHERE codigo = ?", (id_libro,))
            self.conn.commit()

    def close_connection(self):
        self.conn.close()

if __name__ == "__main__":
    db_name = "biblioteca.db"
    data_inserter = DataInserter(db_name)
    data_inserter.insert_books()
    data_inserter.insert_socios()
    data_inserter.insert_prestamos()
    data_inserter.close_connection()
