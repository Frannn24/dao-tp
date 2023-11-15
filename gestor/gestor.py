"""
Posible gestor:

from models.libro import Libro  # Importa la clase Libro desde models.libro
from models.socio import Socio  # Importa la clase Socio desde models.socio
from database.database import BibliotecaDB  # Importa la clase BibliotecaDB desde database

class GestorBiblioteca:
    def __init__(self, db_name):
        self.biblioteca_db = BibliotecaDB(db_name)
    
    def registrar_libro(self, libro):
        self.biblioteca_db.registrar_libro(libro)
    
    def registrar_socio(self, socio):
        self.biblioteca_db.registrar_socio(socio)
    
    def registrar_prestamo(self, id_socio, id_libro, fecha_prestamo, fecha_devolucion):
        self.biblioteca_db.registrar_prestamo(id_socio, id_libro, fecha_prestamo, fecha_devolucion)
    
    def terminar_prestamo(self, id_prestamo):
        self.biblioteca_db.terminar_prestamo(id_prestamo)
    
    def terminar_prestamo_extravio_danio(self, id_prestamo):
        self.biblioteca_db.terminar_prestamo_extravio_danio(id_prestamo)
    
    def registrar_extraviados(self, prestamo_id):
        self.biblioteca_db.registrar_extraviados(prestamo_id)
    
    def verificar_libros_extraviados(self):
        self.biblioteca_db.verificar_libros_extraviados()
    
    def cerrar_conexion(self):
        self.biblioteca_db.cerrar()


"""