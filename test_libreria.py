import unittest
import math
import libreria as cl

class TestComplexLib(unittest.TestCase):

    def test_suma(self):
        self.assertEqual(cl.suma((2, 3), (1, -1)), (3, 2))
        self.assertEqual(cl.suma((0, 0), (5, 7)), (5, 7))

    def test_resta(self):
        self.assertEqual(cl.resta((2, 3), (1, -1)), (1, 4))
        self.assertEqual(cl.resta((0, 0), (5, 7)), (-5, -7))

    def test_producto(self):
        self.assertEqual(cl.producto((1, 2), (3, 4)), (-5, 10))
        self.assertEqual(cl.producto((0, 1), (0, 1)), (-1, 0))

    def test_division(self):
        self.assertEqual(cl.division((1, 1), (1, -1)), (0.0, 1.0))
        self.assertAlmostEqual(cl.division((3, 2), (4, -1))[0], 0.588, places=3)
        self.assertAlmostEqual(cl.division((3, 2), (4, -1))[1], 0.647, places=3)

    def test_modulo(self):
        self.assertEqual(cl.modulo((3, 4)), 5)
        self.assertEqual(cl.modulo((0, 0)), 0)

    def test_conjugado(self):
        self.assertEqual(cl.conjugado((2, 3)), (2, -3))
        self.assertEqual(cl.conjugado((-1, -5)), (-1, 5))

    def test_cartesiano_a_polar(self):
        r, theta = cl.cartesiano_a_polar((1, 0))
        self.assertAlmostEqual(r, 1)
        self.assertAlmostEqual(theta, 0)

        r, theta = cl.cartesiano_a_polar((0, 1))
        self.assertAlmostEqual(r, 1)
        self.assertAlmostEqual(theta, math.pi/2)

    def test_polar_a_cartesiano(self):
        self.assertEqual(
            (round(cl.polar_a_cartesiano((1, 0))[0], 3),
             round(cl.polar_a_cartesiano((1, 0))[1], 3)),
            (1.0, 0.0)
        )
        self.assertEqual(
            (round(cl.polar_a_cartesiano((1, math.pi/2))[0], 3),
             round(cl.polar_a_cartesiano((1, math.pi/2))[1], 3)),
            (0.0, 1.0)
        )

    def test_fase(self):
        self.assertEqual(cl.fase((1, 0)), 0)
        self.assertAlmostEqual(cl.fase((0, 1)), math.pi/2)

if __name__ == '__main__':
    unittest.main()
