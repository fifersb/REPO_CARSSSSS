from django.test import TestCase
import unittest
from .models import MisionVision,SliderIndex,FormInsumo
# Create your tests here.
class TestEjemplos(unittest.TestCase):

    def test_de_iguales(self):
        self.assertEqual('ii','ii')

    def test_no_esta_el_texto(self):
        self.assertFalse('hola' in 'este es un mundo')
    
    def grabar_insumo(self):
        valor = 0
        try:
            ins = FormInsumo(
                nombre='JaJa',
                precio=2500,
                descripcion='lubricante',
                stock=7
            )
            ins.save()
            valor = 1
        except:
            valor = 0
        self.assertEqual(valor, 1)
        
if __name__ == "__main__":
    unittest.main()
