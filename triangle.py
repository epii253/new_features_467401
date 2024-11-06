import unittest

def area(a, h): 
    '''
    Принимает значения длинны стороны треугольника и высоты, опущенной на эту сторону, и возвращает площадь этого треугольника.
        Параметры:
            a (float): длинна стороны треугольник
            h (float): длинна высоты опущенной из вершины противолежащей стороне a треугольника.

        Возвращаемое значение:
            area (float): площадь треугольника со стороной a и высотой h, с основанием на стороне a.
        
        Примеры вызова:
            area(3.0, 7.5)
            > 11.25

            area(6.7, 1.85)
            > 6.1975

            area(3.25, 2.75)
            > 4.4
    '''
    return a * h / 2 

def perimeter(a, b, c): 
    '''
    Принимает значения длин сторон треугольника и возвращает его периметр.
        Параметры:
            a (float): первая сторона треугольник
            b (float): вторая сторона треугольник
            c (float): тертья сторона треугольник

        Возвращаемое значение:
            perimeter (float): периметр треугольника со сторонами a, b и c
        
        Примеры вызова:
            perimeter(9.4, 4.11, 48)
            > 61.51

            perimeter(4.45, 0.49, 26.2)
            > 31.14

            perimeter(44.0, 1.11, 79)
            > 124.11
    '''
    return a + b + c 

class TriangleTestCase(unittest.TestCase):
    def test_area(self):
        res = area(3.0, 7.5)
        self.assertAlmostEqual(res, 11.25, places=5)

        res = area(3.25, 2.75)
        self.assertAlmostEqual(res, 4.46875, places=5)

    def test_incorrect_area_input(self):
        res = area(-1.41, -2)
        self.assertAlmostEqual(res, 1.41, places=5)
        
    def test_perimetr(self):
        res = perimeter(4.45, 0.49, 26.2)
        self.assertAlmostEqual(res, 31.14, places=5)

        res = perimeter(44.0, 1.11, 79)
        self.assertAlmostEqual(res, 124.11, places=5)

    def test_incorrect_perimeter_input(self):
        res = perimeter(-0.99, -2, 2.99)
        self.assertAlmostEqual(res, 0, places=5)