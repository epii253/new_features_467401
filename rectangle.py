import unittest
import sys

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
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        sys.exit(-1)

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
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        sys.exit(-1)

    return 2*(a + b) 
