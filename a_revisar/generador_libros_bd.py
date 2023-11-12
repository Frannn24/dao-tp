import sqlite3

class BookInserter:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def insert_books(self, start_code=201, num_books=100):
        # Insertar libros en la base de datos con estado "Disponible"
        for i in range(start_code, start_code + num_books):
            self.cursor.execute("INSERT INTO libros (codigo, titulo, precio_reposicion, estado) VALUES (?, ?, ?, ?)",
                                (i, f"Libro-{i}", 10.99 * i, 'Disponible'))
            self.conn.commit()

    def close_connection(self):
        self.conn.close()

if __name__ == "__main__":
    db_name = "biblioteca.db"
    book_inserter = BookInserter(db_name)
    book_inserter.insert_books(start_code=201, num_books=100)
    book_inserter.close_connection()
