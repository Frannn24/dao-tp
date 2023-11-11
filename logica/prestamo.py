from datetime import *
from models.estado import *

class Prestamo:
    def __init__(self, libro, socio, fecha_prestamo, fecha_devolucion):
        # Constructor para crear un objeto Prestamo
        self.libro = libro
        self.socio = socio
        self.estado = 1
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = fecha_devolucion

    def demoro(self):
        # Método para calcular si el libro fue devuelto con demora
        fecha_actual = datetime.now()
        if fecha_actual >  self.fecha_devolucion:
            return True
        else:
            return False

    def fue_devuelto_en_fecha(self):
        # Método para verificar si el libro fue devuelto en fecha
        # Devuelve True si es devuelto en fecha, devuelve false si no.
        fecha_actual = datetime.now()
        if fecha_actual < self.fecha_devolucion:
            return True
        else:
            return False
    def estraviado(self):
        fecha_devoluvion_mes = self.fecha_devolucion + timedelta(days=30)
        if datetime.now() > fecha_devoluvion_mes:
            self.libro.estado = Extraviado
        else:
            print(f"El libro aun no paso 30 dias de la fecha de devolución.")
