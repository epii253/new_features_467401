import unittest

def area(a, b): 
    '''
    Принимает значения стороон прямоугольника и возвращает его площадь.

        Параметры:
            a (float): первая сторона прямоугольника
            b (float): вторая сторона прямоугольника

        Возвращаемое значение:
            area (float): площадь прямоугольника со сторонами a и b
        
        Примеры вызова:
            area(3.0, 7.9)
            > 23.7

            area(9.7, 8.8)
            > 85.36

            area(43.9, 9.1)
            > 399.49
    '''
    return a * b 

def perimeter(a, b): 
    '''
    Принимает значения стороон прямоугольника и возвращает его периметр.

        Параметры:
            a (float): первая сторона прямоугольника
            b (float): вторая сторона прямоугольника

        Возвращаемое значение:
            perimeter (float): периметр прямоугольника со сторонами a и b
        
        Примеры вызова:
            perimeter(3.0, 7.9)
            > 21.8

            perimeter(9.7, 8.8)
            > 37.0

            perimeter(43.9, 9.1)
            > 106.0
    '''
    return 2*(a + b) 


class RectangleTestCase(unittest.TestCase):
    def test_area(self):
        res = area(3.0, 7.9)
        self.assertAlmostEqual(res, 23.7, places=5)

        res = area(9.7, 8.8)
        self.assertAlmostEqual(res, 85.36, places=5)

    def test_incorrect_area_input(self):
        res = area(-1.0, 0.1)
        self.assertAlmostEqual(res, -0.1, places=5)
        
    def test_perimetr(self):
        res = perimeter(3.0, 7.9)
        self.assertAlmostEqual(res, 21.8, places=5)

        res = perimeter(43.9, 9.1)
        self.assertAlmostEqual(res, 106.0, places=5)

    def test_incorrect_perimeter_input(self):
        res = perimeter(-2.3, 7.1)
        self.assertAlmostEqual(res, 9.6, places=5)