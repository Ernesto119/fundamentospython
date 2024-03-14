import unittest
from unittest.mock import patch
from gestion_de_almacenes import crear_almacen, crear_objecto,pantalla
from io import StringIO
import sys

class TestAlmacen(unittest.TestCase):
    def test_creacion_almacen(self):
        lista_almacenes = []
        inventario = []
        crear_almacen("Almacen 1", 10, 10, 10, lista_almacenes, inventario)
        
        # Check if a warehouse is created
        self.assertEqual(len(lista_almacenes), 1)
        self.assertEqual(len(inventario), 1)

    def test_creacion_objeto(self):
        lista_almacenes = []
        inventario = []
        crear_almacen("Almacen 1", 10, 10, 10, lista_almacenes, inventario)
        crear_objecto("Objeto 1", inventario[0])

        # Check if an item is created
        self.assertEqual(len(inventario[0]), 1)
        self.assertEqual(inventario[0][0][1], "Objeto 1")

    @patch('sys.stdout', new_callable=StringIO)
    def test_pantalla(self, mock_stdout):
        lista_almacenes = []
        inventario = []
        crear_almacen("Almacen 1", 10, 10, 10, lista_almacenes, inventario)
        crear_objecto("Objeto 1", inventario[0])

        pantalla(lista_almacenes)

        # Check if the output matches the expected format
        expected_output = "IDNombre                   Capacidad\n---------------------------------------------\n0000Almacen 1                       1000\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)


if __name__ == '__main__':
    unittest.main()

