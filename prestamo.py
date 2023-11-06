from datetime import datetime

class Prestamo:
    def __init__(self, libro, socio, fecha_prestamo, fecha_devolucion):
        # Constructor para crear un objeto Prestamo
        self.libro = libro
        self.socio = socio
        self.fecha_prestamo = fecha_prestamo
        self.fecha_devolucion = fecha_devolucion

    def calcular_demora(self):
        # Método para calcular si el libro fue devuelto con demora
        fecha_actual = datetime.now()
        return (fecha_actual - self.fecha_devolucion).days

    def fue_devuelto_en_fecha(self):
        # Método para verificar si el libro fue devuelto en fecha
        return self.calcular_demora() <= 0
