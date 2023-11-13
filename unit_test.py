from Examen2 import MiClase
import unittest

class TestDB(unittest.TestCase):
    def setUp(self):
        self.object = MiClase(5, 120, 12, ["Canción 1", "Canción 2", "Canción 3"], [0.8, 0.9, 0.7])

    def test_ObtieneValencia(self):
        self.assertEqual(self.object.ObtieneValencia(1234567), 4)
        self.assertEqual(self.object.ObtieneValencia(123456789), 5)

    def test_DivisibleTempo(self):
        self.assertEqual(self.object.DivisibleTempo(10), [1, 2, 5, 10])
        self.assertEqual(self.object.DivisibleTempo(11), [1, 11])

    def test_ObtieneMasBailable(self):
        self.assertEqual(self.object.ObtieneMasBailable([0.8, 0.9, 0.7]), 0.9)
        self.assertEqual(self.object.ObtieneMasBailable([0.75, 0.1, 0.99]), 0.99)

    def test_VerificaListaCanciones(self):
        self.assertEqual(self.object.VerificaListaCanciones(["Canción 1", "Canción 2", "Canción 3"]), True)
        self.assertEqual(self.object.VerificaListaCanciones(["Canción 1", "Canción 2", None]), False)

    def test_Encuentra(self):
        #Test of Encuentra method
        for i in range(51):
            self.assertEqual(self.object.Encuentra([0, 1, 2, 3, i], i), False)
    

if __name__ == "__main__":
    unittest.main()