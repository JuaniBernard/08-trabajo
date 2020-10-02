class Producto:
    def __init__(self, descripcion="", precio=0, tipo="", estado="disponible"):
        self.descripcion = descripcion
        self.precio = precio
        self.tipo = tipo
        self.estado = estado

    @property
    def descripcion(self):
        return self._descripcion

    @descripcion.setter
    def descripcion(self, value):
        self._descripcion = value

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, value):
        if value < 0:
            raise ValueError("El precio no puede ser un valor negativo.")
        else:
            self._precio = value

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self, value):
        self._tipo = value

    @property
    def estado(self):
        return self._estado

    @estado.setter
    def estado(self, value):
        self._estado = value
