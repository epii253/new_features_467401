import math
import sys
import unittest

def area(r):
    '''
    Принимает радиус окружности и возвращает её площадь.

        Параметры:
            r (float): радиус окружности

        Возвращаемое значение:
            square (float): площадь окружности радиуса r
        
        Примеры вызова:
            area(3.0)
            > 28.274333882308

            area(0.0)
            > 0.000000000000

            area(3.5)
            > 38.484510006474
    '''
    if not isinstance(r, (int, float)):
        sys.exit(-1)

    return math.pi * r * r


def perimeter(r):
    '''
    Принимает радиус окружности и возвращает её периметр.

        Параметры:
            r (float): радиус окружности

        Возвращаемое значение:
            perimeter (float): периметр окружности с радиусом r
        
        Примеры вызова:
            perimeter(7.0)
            > 43.982297150257

            perimeter(2.5)
            > 7.8539816339744

            perimeter(0.5)
            > 3.1415926535897
    '''
    if not isinstance(r, (int, float)):
        sys.exit(-1)
        
    return 2 * math.pi * r