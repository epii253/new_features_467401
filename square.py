import unittest

def area(a):
    '''
    Принимает значения сторооны квадрата и возвращает его площадь.

        Параметры:
            a (float): длинна стороны квадрата

        Возвращаемое значение:
            area (float): площадь квадрата со стороной a
        
        Примеры вызова:
            area(3.0)
            > 9.0

            area(7.3)
            > 53.29

            area(0.5)
            > 0.25
    '''
    return a * a


def perimeter(a):
    '''
    Принимает значения сторооны квадрата и возвращает его периметр.

        Параметры:
            a (float): длинна стороны квадрата

        Возвращаемое значение:
            perimeter (float): периметр квадрата со стороной a
        
        Примеры вызова:
            perimeter(14.4)
            > 57.6

            perimeter(7.77)
            > 31.08

            perimeter(9.55)
            > 38.2
    '''
    return 4 * a

class SquareTestCase(unittest.TestCase):
    def test_area(self):
        res = area(3.0)
        self.assertAlmostEqual(res, 9.0, places=5)

        res = area(7.3)
        self.assertAlmostEqual(res, 53.29, places=5)

    def test_incorrect_area_input(self):
        res = area(-1.41)
        self.assertAlmostEqual(res, 1.9881, 5)
        
    def test_perimetr(self):
        res = perimeter(14.4)
        self.assertAlmostEqual(res, 57.6, places=5)

        res = perimeter(9.55)
        self.assertAlmostEqual(res, 38.2, places=5)

    def test_incorrect_perimeter_input(self):
        res = perimeter(-0.99)
        self.assertAlmostEqual(res, -3.96, places=5)