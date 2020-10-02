from repositorios import Repositorios


class ProductoService:
    def add_producto(self, producto):
        key = len(Repositorios.productosList)
        while key in Repositorios.productosList:
            key = key + 1
        Repositorios.productosList[key] = producto.__dict__
        return key

    def update_producto(self, key, producto):
        if key in Repositorios.productosList:
            Repositorios.productosList[key]['_descripcion'] = producto.\
                _descripcion
            Repositorios.productosList[key]['_precio'] = producto._precio
            Repositorios.productosList[key]['_tipo'] = producto._tipo
            Repositorios.productosList[key]['_estado'] = producto._estado
        else:
            raise ValueError("ID de producto incorrecta.")

    def delete_producto(self, key):
        if key in Repositorios.productosList:
            del Repositorios.productosList[key]
        else:
            raise ValueError("ID de producto incorrecta.")

    def get_productosList(self):
        return Repositorios.productosList

    def insertion_sort_precio(self, lista, orden):
        lista1 = lista.copy()
        if orden == 'ascendente':
            for i in range(1, len(lista1)):
                valor = lista1[i]
                j = i-1
                while j >= 0 and valor['_precio'] < lista1[j]['_precio']:
                    lista1[j + 1] = lista1[j]
                    j -= 1
                lista1[j + 1] = valor
            return lista1
        if orden == 'descendente':
            for i in range(1, len(lista1)):
                valor = lista1[i]
                j = i-1
                while j >= 0 and valor['_precio'] > lista1[j]['_precio']:
                    lista1[j + 1] = lista1[j]
                    j -= 1
                lista1[j + 1] = valor
            return lista1

    def busqueda_binaria(self, lista, precio):
        lista_ordenada = self.insertion_sort_precio(lista, 'ascendente')
        low = 0
        high = len(lista_ordenada) - 1
        mid = 0
        while low <= high:
            mid = (high + low) // 2
            if lista_ordenada[mid]['_precio'] < precio:
                low = mid + 1
            elif lista_ordenada[mid]['_precio'] > precio:
                high = mid - 1
            else:
                return lista_ordenada[mid]
        return False

    def get_lista_estado(self, get_lista_productos, estado):
        st_dict = {}
        for i in get_lista_productos:
            if get_lista_productos[i]["_estado"] == estado:
                st_dict[i] = get_lista_productos[i]
        return st_dict
