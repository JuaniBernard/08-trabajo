import unittest
from producto import Producto
from parameterized import parameterized
from productoServices import ProductoService
from repositorios import Repositorios


class TestProducto(unittest.TestCase):
    def test_uso_property(self):
        producto = Producto()
        producto.descripcion = 'acer A515'
        producto.precio = 500000
        producto.tipo = 'computadoras'
        producto.estado = 'disponible'
        self.assertDictEqual(producto.__dict__, {'_descripcion': 'acer A515',
                                                 '_precio': 500000,
                                                 '_tipo': 'computadoras',
                                                 '_estado': 'disponible'})

    def test_constructor_con_valores_iniciales(self):
        producto = Producto("Lenovo 450", 300000, 'computadoras')
        self.assertDictEqual(producto.__dict__, {'_descripcion': 'Lenovo 450',
                                                 '_precio': 300000,
                                                 '_tipo': 'computadoras',
                                                 '_estado': 'disponible'})

    def test_precio_negativo(self):
        with self.assertRaises(ValueError):
            Producto('Asus', -5000000, 'computadoras')

    @parameterized.expand([
            ("lenovo t490", 6000000, 'computadoras', 'vendido'),
            ("samsung s10", 200000, 'celular', 'vendido'),
            ("samsung s20", 400000, 'celular', 'disponible'),
            ("acer", 6000500, 'computadoras', 'disponible'),
            ("HP", 6000000, 'computadoras', 'disponible'),
        ])
    # Agregar un producto
    def test_add_producto(self, descripcion, precio, tipo, estado):
        producto = Producto(descripcion, precio, tipo, estado)
        productoKey = ProductoService().add_producto(producto)
        self.assertDictEqual(Repositorios.productosList[productoKey],
                             producto. __dict__)

    @parameterized.expand([
        (1, "lenovo t480", 5000000, 'computadoras', 'vendido'),
    ])
    # Modificar un producto
    def test_update_producto(self, key, descripcion, precio, tipo, estado):
        producto = Producto(descripcion, precio, tipo)
        ProductoService().update_producto(key, producto)
        self.assertDictEqual(Repositorios.productosList[key],
                             producto.__dict__)

    @parameterized.expand([
        (111, "samsung s10", 300000, 'celular'),
        (345, "HP", 4500000, 'computadoras'),
    ])
    # Verificar la exeption al modificar un producto con un legajo que no
    # existe
    def test_update_member_value_error(self, key, descripcion, precio, tipo):
        producto = Producto(descripcion, precio, tipo)
        with self.assertRaises(ValueError):
            ProductoService().update_producto(key, producto)

    @parameterized.expand([
        ("ascendente",
            {0: {'_descripcion': 'samsung s10', '_precio': 200000,
             '_tipo': 'celular', '_estado': 'vendido'},
             1: {'_descripcion': 'samsung s20', '_precio': 400000,
             '_tipo': 'celular', '_estado': 'disponible'},
             2: {'_descripcion': 'lenovo t490', '_precio': 6000000,
             '_tipo': 'computadoras', '_estado': 'vendido'},
             3: {'_descripcion': 'HP', '_precio': 6000000, '_tipo':
             'computadoras', '_estado': 'disponible'},
             4: {'_descripcion': 'acer', '_precio': 6000500,
             '_tipo': 'computadoras', '_estado': 'disponible'}}),
        ("descendente",
            {0: {'_descripcion': 'acer', '_precio': 6000500,
             '_tipo': 'computadoras', '_estado': 'disponible'},
             1: {'_descripcion': 'lenovo t490', '_precio': 6000000,
             '_tipo': 'computadoras', '_estado': 'vendido'},
             2: {'_descripcion': 'HP', '_precio': 6000000, '_tipo':
             'computadoras', '_estado': 'disponible'},
             3: {'_descripcion': 'samsung s20', '_precio': 400000,
             '_tipo': 'celular', '_estado': 'disponible'},
             4: {'_descripcion': 'samsung s10', '_precio': 200000,
             '_tipo': 'celular', '_estado': 'vendido'}}),
    ])
    def test_insertion_sort_precio(self, tipo_orden, list_ordenada):
        self.maxDiff = None
        lista_ordenada = ProductoService().\
            insertion_sort_precio(Repositorios.productosList, tipo_orden)
        self.assertDictEqual(lista_ordenada, list_ordenada)

    @parameterized.expand([
        (200000, {'_descripcion':
         'samsung s10', '_precio': 200000, '_tipo': 'celular',
                  '_estado': 'vendido'}),
        (400000, {'_descripcion':
         'samsung s20', '_precio': 400000, '_tipo': 'celular',
                  '_estado': 'disponible'}),
    ])
    # Busqueda binaria
    def test_busqueda_binaria(self, precio_buscado, producto):
        busqueda = ProductoService().\
            busqueda_binaria(Repositorios.productosList, precio_buscado)
        self.assertDictEqual(busqueda, producto)

    # Eliminar un producto
    # def test_delete_producto(self):
    #    ProductoService().delete_producto(0)
    #    self.assertEqual(Repositorios.productosList.get(0), None)
    #    print(ProductoService().get_productosList())

    # @parameterized.expand([
    #    ("lenovo t490", 6000000, 'computadoras')
    # ])
    # Verificar la exeption al modificar un producto con un legajo que no
    # existe
    # def test_delete_producto_value_error(self, descripcion, precio, tipo):
    #    long_list = len(Repositorios.productosList)
    #    with self.assertRaises(ValueError):
    #        ProductoService().delete_producto(long_list+1)

    @parameterized.expand([
        ("disponible",
            {2: {'_descripcion': 'samsung s20', '_precio': 400000,
             '_tipo': 'celular', '_estado': 'disponible'},
             3: {'_descripcion': 'acer', '_precio': 6000500,
             '_tipo': 'computadoras', '_estado': 'disponible'},
             4: {'_descripcion': 'HP', '_precio': 6000000,
             '_tipo': 'computadoras', '_estado': 'disponible'}}),
        ("vendido",
            {0: {'_descripcion': 'lenovo t490', '_precio': 6000000,
             '_tipo': 'computadoras', '_estado': 'vendido'},
             1: {'_descripcion': 'samsung s10', '_precio': 200000,
             '_tipo': 'celular', '_estado': 'vendido'}}),
    ])
    def test_get_lista_estado(self, estado, list_estado):
        lista_estado = ProductoService().\
            get_lista_estado(Repositorios.productosList, estado)
        self.assertDictEqual(lista_estado, list_estado)


if __name__ == '__main__':
    unittest.main()
