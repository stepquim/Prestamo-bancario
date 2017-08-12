import unittest
from Prestamo import *


class Test(unittest.TestCase):
    #Test1 valida si el sueldo es mayor a 1000 y si el egreso es menor al sueldo para aceptar y darle el prestamo
    def test1(self):
        pablo = Persona(1500,500)
        PrestamodePablo = Prestamo()
        msg = PrestamodePablo.validar_prestamo(pablo)
        self.assertEquals(msg,"Prestamo aceptado")
		#Test2 
    def test2(self):
        juan = Persona(1500,1600)
        Prestamodejuan = Prestamo()
        msg = Prestamodejuan.validar_prestamo(juan)
        self.assertEquals(msg,"Prestamo negado")
	
    #Test3 
    def test3(self):
        ana = Persona(800,400)
        Prestamodeana = Prestamo()
        msg = Prestamodeana.validar_prestamo(ana)
        self.assertEquals(msg,"Prestamo aceptado")
	
    #Test4 
    def test4(self):
        mia = Persona(800,900)
        Prestamodemia = Prestamo()
        msg = Prestamodemia.validar_prestamo(mia)
        self.assertEquals(msg,"Prestamo negado")
        
if __name__ == '__main__':
    unittest.main()
