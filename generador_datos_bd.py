#Antes de usar borrar la base de datos biblioteca.db, luego ejecutar main.py y luego ejecutar este archivo

import sqlite3
import random
from datetime import datetime, timedelta

class DataInserter:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def insert_books(self):
        # Insertar 100 libros
        for i in range(1, 201):
            if i % 4 == 0:  # Aproximadamente el 25% de los libros serán "Extraviados"
                estado_libro = 'Extraviado'
            elif i % 2 == 0:
                estado_libro = 'Disponible'
            else:
                estado_libro = 'Prestado'

            self.cursor.execute("INSERT INTO libros (codigo, titulo, precio_reposicion, estado) VALUES (?, ?, ?, ?)",
                        (i, f"Libro-{i}", 10.99 * i, estado_libro))
            self.conn.commit()

    def insert_socios(self):
        # Insertar 50 socios
        for i in range(1, 51):
            self.cursor.execute("INSERT INTO socios (id_socio, nombre) VALUES (?, ?)",
                                (i, f"Socio-{i}"))
            self.conn.commit()

    def insert_prestamos(self):
        # Insertar 50 préstamos
        for i in range(1, 51):
            id_socio = random.randint(1, 50)

            available_books_query = "SELECT codigo FROM libros WHERE estado = 'Disponible'"
            self.cursor.execute(available_books_query)
            available_books = self.cursor.fetchall()

            if not available_books:
                print("No hay libros disponibles para el préstamo.")
                break

            id_libro = random.choice(available_books)[0]

            active_loans_query = "SELECT COUNT(*) FROM prestamo WHERE id_socio = ? AND estado = 1"
            self.cursor.execute(active_loans_query, (id_socio,))
            active_loans = self.cursor.fetchone()[0]

            if active_loans >= 3:
                print(f"El socio {id_socio} ya tiene 3 libros prestados. No se puede agregar más préstamos.")
                continue

            fecha_prestamo = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            fecha_devolucion = (datetime.now() + timedelta(days=random.randint(7, 30))).strftime('%Y-%m-%d %H:%M:%S')

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
