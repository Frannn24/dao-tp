class EstadoLibro:
    def __init__(self, libro):
        self.libro = libro

    def prestamo(self):
        pass

    def devolucion_en_fecha(self):
        pass

    def devolucion_con_demora(self):
        pass
    
    def esDisponible(self):
        return False
    
    def esPrestado(self):
        return False
    
    def esExtraviado(self):
        return False

class EstadoDisponible(EstadoLibro):
    def esDisponible(self):
        return True
    
    def prestamo(self):
        self.libro.cambiar_estado(EstadoPrestado(self.libro))

class EstadoPrestado(EstadoLibro):
    def esPrestado(self):
        return True
    
    def devolucion_en_fecha(self):
        self.libro.cambiar_estado(EstadoDisponible(self.libro))

    def devolucion_con_demora(self):
        self.libro.cambiar_estado(EstadoExtraviado(self.libro))

class EstadoExtraviado(EstadoLibro):
    def esExtraviado(self):
        return True
