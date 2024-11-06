import unittest

import circle
import rectangle
import square
import triangle

class CircleTestCase(unittest.TestCase):
    def test_area(self):
        res = circle.area(3.0)
        self.assertAlmostEqual(res, 28.274333882308, places=5)

        res = circle.area(3.5)
        self.assertAlmostEqual(res, 38.484510006474, places=5)

    def test_incorrect_area_input(self):
        res = circle.area(-1.0)
        self.assertAlmostEqual(res, 0, places=5)
        
    def test_perimetr(self):
        res = circle.perimeter(2.5)
        self.assertAlmostEqual(res, 15.707963267948966, places=5)

        res = circle.perimeter(0.5)
        self.assertAlmostEqual(res, 3.1415926535897, places=5)

    def test_incorrect_perimeter_input(self):
        res = circle.perimeter(-2.5)
        self.assertAlmostEqual(res, 0, places=5)


class RectangleTestCase(unittest.TestCase):
    def test_area(self):
        res = rectangle.area(3.0, 7.9)
        self.assertAlmostEqual(res, 23.7, places=5)

        res = rectangle.area(9.7, 8.8)
        self.assertAlmostEqual(res, 85.36, places=5)

    def test_incorrect_area_input(self):
        res = rectangle.area(-1.0, 0.1)
        self.assertAlmostEqual(res, 0, places=5)
        
    def test_perimetr(self):
        res = rectangle.perimeter(3.0, 7.9)
        self.assertAlmostEqual(res, 21.8, places=5)

        res = rectangle.perimeter(43.9, 9.1)
        self.assertAlmostEqual(res, 106.0, places=5)

    def test_incorrect_perimeter_input(self):
        res = rectangle.perimeter(-2.3, 7.1)
        self.assertAlmostEqual(res, 0, places=5)

class SquareTestCase(unittest.TestCase):
    def test_area(self):
        res = square.area(3.0)
        self.assertAlmostEqual(res, 9.0, places=5)

        res = square.area(7.3)
        self.assertAlmostEqual(res, 53.29, places=5)

    def test_incorrect_area_input(self):
        res = square.area(-1.41)
        self.assertAlmostEqual(res, 0, 5)
        
    def test_perimetr(self):
        res = square.perimeter(14.4)
        self.assertAlmostEqual(res, 57.6, places=5)

        res = square.perimeter(9.55)
        self.assertAlmostEqual(res, 38.2, places=5)

    def test_incorrect_perimeter_input(self):
        res = square.perimeter(-0.99)
        self.assertAlmostEqual(res, 0, places=5)

class TriangleTestCase(unittest.TestCase):
    def test_area(self):
        res = triangle.area(3.0, 7.5)
        self.assertAlmostEqual(res, 11.25, places=5)

        res = triangle.area(3.25, 2.75)
        self.assertAlmostEqual(res, 4.46875, places=5)

    def test_incorrect_area_input(self):
        res = triangle.area(-1.41, -2)
        self.assertAlmostEqual(res, 0, places=5)
        
    def test_perimetr(self):
        res = triangle.perimeter(4.45, 0.49, 26.2)
        self.assertAlmostEqual(res, 31.14, places=5)

        res = triangle.perimeter(44.0, 1.11, 79)
        self.assertAlmostEqual(res, 124.11, places=5)

    def test_incorrect_perimeter_input(self):
        res = triangle.perimeter(-0.99, -2, 2.99)
        self.assertAlmostEqual(res, 0, places=5)