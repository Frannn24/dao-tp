class Socio:
    def __init__(self, id_socio, nombre):
        # Constructor para crear un objeto Socio
        self.id_socio = id_socio
        self.nombre = nombre
        self.libros_prestados = []

    def agregar_libro_prestado(self, prestamos):
        # Método para agregar un libro prestado al socio
        if self.tiene_maximo_libros_prestados():
            self.libros_prestados.append(prestamos)
        else:
            print(f"El socio {self.nombre} ya tiene 3 prestamos hechos.")

    def tiene_demoras(self):
        # Método para verificar si el socio tiene libros con demora
        # Puedes implementar esta función según tus necesidades
        for libro in self.libros_prestados:
            if  libro.demoro():
                print(f"El socio {self.nombre} no devolvio el libro {libro}")
        


    def tiene_maximo_libros_prestados(self):
        # Método para verificar si el socio tiene más de tres libros prestados
        if len(self.libros_prestados) > 3:
            return True
        else:
            return False
