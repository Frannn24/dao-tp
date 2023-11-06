class Socio:
    def __init__(self, nombre):
        # Constructor para crear un objeto Socio
        self.nombre = nombre
        self.libros_prestados = []

    def agregar_libro_prestado(self, libro):
        # Método para agregar un libro prestado al socio
        self.libros_prestados.append(libro)

    def tiene_demoras(self):
        # Método para verificar si el socio tiene libros con demora
        # Puedes implementar esta función según tus necesidades
        pass

    def tiene_maximo_libros_prestados(self):
        # Método para verificar si el socio tiene más de tres libros prestados
        return len(self.libros_prestados) > 3
