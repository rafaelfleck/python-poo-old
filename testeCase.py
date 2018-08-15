
import unittest

class ConverteNumeroRomano:

    def __init__(self):
        self.digito_map = {"M":1000, "D":500, "C":100, "L":50, "X":10, "V":5, "I":1}
        

    def converte_para_decimal(self, numero_romano):
        val = 0
        for char in numero_romano:
            val += self.digito_map[char]
        return val


class TestConverteNumeroRomano(unittest.TestCase):

    def setUp(self):
        print("Contruir o objetos da clas ConvertNumerosRomanos")
        self.cnr = ConverteNumeroRomano()

    def tearDown(self):
        print("Destroi o objetos da clas ConvertNumerosRomanos")
        self.cnr = None

    def test_mil(self):
        self.assertEqual(1000, self.cnr.converte_para_decimal('M'))

    def test_cem(self):
        self.assertEqual(100, self.cnr.converte_para_decimal('C'))

    def test_ciquenta(self):
        self.assertEqual(50, self.cnr.converte_para_decimal('L'))

    def test_vazio(self):
        self.assertTrue(self.cnr.converte_para_decimal('') == 0)
        self.assertFalse(self.cnr.converte_para_decimal('') > 0)


if __name__ == '__main__':
    unittest.main()