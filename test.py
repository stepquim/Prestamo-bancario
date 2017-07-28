import unittest
from Prestamo import *


class Test(unittest.TestCase):
    #Test1 valida si el sueldo es mayor a 1000 y si el egreso es menor al sueldo para aceptar y darle el prestamo
    def test1(self):
        pablo = Persona(1500,500)
        PrestamodePablo = Prestamo()
        msg = PrestamodePablo.validar_prestamo(pablo)
        self.assertEquals(msg,"Prestamo aceptado")
		
if __name__ == '__main__':
    unittest.main()
