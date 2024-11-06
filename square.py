import unittest
import sys

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
    if not isinstance(a, (int, float)):
        sys.exit(-1)

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
    if not isinstance(a, (int, float)):
        sys.exit(-1)

    return 4 * a