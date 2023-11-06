class EstadoLibro:
    def __init__(self, libro):
        self.libro = libro

    def prestamo(self):
        pass

    def devolucion_en_fecha(self):
        pass

    def devolucion_con_demora(self):
        pass

class EstadoDisponible(EstadoLibro):
    def prestamo(self):
        self.libro.cambiar_estado(EstadoPrestado(self.libro))

class EstadoPrestado(EstadoLibro):
    def devolucion_en_fecha(self):
        self.libro.cambiar_estado(EstadoDisponible(self.libro))

    def devolucion_con_demora(self):
        self.libro.cambiar_estado(EstadoExtraviado(self.libro))

class EstadoExtraviado(EstadoLibro):
    pass
