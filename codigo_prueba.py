"""     
    def prestar_libro(self, libro):
        prestado = Prestado()
        prestado.actualizar_estado(libro)

    def devolver_libro(self, libro, dias_de_retraso):
        if dias_de_retraso > 30:
            extraviado = Extraviado()
            extraviado.actualizar_estado(libro)
        else:
            disponible = Disponible()
            disponible.actualizar_estado(libro)
"""

