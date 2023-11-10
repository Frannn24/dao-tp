class Biblioteca:
    def __init__(self):
        self.libros = []
        self.socios = []
        self.prestamos = []

    def agregar_libro(self, libro):
        # Método para agregar un libro a la biblioteca
        self.libros.append(libro)

    def realizar_prestamo(self, libro, socio, fecha_devolucion):
        # Método para registrar un préstamo
        # Verificar condiciones antes de prestar el libro al socio
        pass

    def registrar_devolucion(self, prestamo):
        # Método para registrar la devolución de un libro y calcular si hubo demora
        pass

    def listar_libros_extraviados(self):
        # Método para listar los libros extraviados
        extraviados = [libro for libro in self.libros if libro.esta_extraviado()]
        return extraviados
