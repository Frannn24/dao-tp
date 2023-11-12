from database.database import BibliotecaDB
from models.libro import *
from models.estado import *

# Conectar a la base de datos (asegúrate de que el nombre de la base de datos sea correcto)
db = BibliotecaDB("biblioteca.db")

def probar_cambio_estado(codigo_libro):
    # Obtener información del libro desde la base de datos
    db.cursor.execute("SELECT * FROM libros WHERE codigo = ?", (codigo_libro,))
    libro_info = db.cursor.fetchone()

    if libro_info:
        # Crear una instancia de Libro con la información de la base de datos
        libro = Libro(libro_info[0], libro_info[1], libro_info[2])
        estado_actual = libro.estado

        # Mostrar el estado actual del libro
        print(f"Estado actual del libro (código {codigo_libro}): {estado_actual.__class__.__name__}")

        # Realizar un cambio de estado (por ejemplo, de Disponible a Prestado)
        # Realizar un cambio de estado (por ejemplo, de Disponible a Prestado)
        if isinstance(estado_actual, Disponible):
            libro.realizar_prestamo()
        elif isinstance(estado_actual, Prestado):
            libro.realizar_devolucion(en_fecha=True)
        elif isinstance(estado_actual, Extraviado):
            print("El libro está extraviado. No se pueden realizar cambios de estado.")
        else:
            print("Estado no reconocido. No se pueden realizar cambios de estado.")

        # Mostrar el nuevo estado del libro
        nuevo_estado = libro.estado
        print(f"Nuevo estado del libro: {nuevo_estado.__class__.__name__}")

        # Actualizar el estado en la base de datos
        db.cursor.execute("UPDATE libros SET estado = ? WHERE codigo = ?", (nuevo_estado.__class__.__name__, codigo_libro))
        db.conn.commit()
        print("Estado actualizado en la base de datos.")

    else:
        print(f"No existe un libro con el código {codigo_libro} en la base de datos.")

# Código de prueba
if __name__ == "__main__":
    codigo_ingresado = input("Ingrese el código del libro: ")
    try:
        codigo_libro = int(codigo_ingresado)
        probar_cambio_estado(codigo_libro)
    except ValueError:
        print("El código ingresado no es válido. Por favor, ingrese un número entero.")
    
    # Cerrar la conexión con la base de datos al finalizar
    db.cerrar()
