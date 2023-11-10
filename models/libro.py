# libro.py

#from models.estado import EstadoDisponible, EstadoPrestado, EstadoExtraviado
from models.estado import *


class Libro:
    def __init__(self, codigo, titulo, precio_reposicion):
        self.codigo = codigo
        self.titulo = titulo
        self.precio_reposicion = precio_reposicion
        #self.estado = EstadoDisponible(self)
        self.estado = Disponible()

    def cambiar_estado(self, nuevo_estado):
        self.estado = nuevo_estado
        
    def realizar_prestamo(self):
        if isinstance(self.estado, Disponible):
            self.cambiar_estado(Prestado())
            # Actualizar la base de datos con el nuevo estado
        else:
            print("No se puede realizar un préstamo. El libro no está disponible.")
    """
    def realizar_prestamo(self):
        self.estado.prestamo()

    def realizar_devolucion(self, en_fecha=True):
        if en_fecha:
            self.estado.devolucion_en_fecha()
        else:
            self.estado.devolucion_con_demora()

    def esta_extraviado(self):
        #return isinstance(self.estado, EstadoExtraviado)
        return isinstance(self.estado, Extraviado)
    """