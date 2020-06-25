import math


def square_area(side):
    """Returns the area of a square"""
    return side * side


def rectangle_area(base, height):
    """Returns the area of a rectangle"""
    return base * height


def triangle_area(base, height):
    """Returns the area of a triangle"""
    return (base * height)/2


def rhombus_area(diagonal_1, diagonal_2):
    """Returns the area of a rhombus"""
    return (diagonal_1 * diagonal_2) / 2


def trapezoid_area(base_minor, base_major, height):
    """Returns the area of a trapezoid"""
    return  height * (base_minor + base_major) / 2


def regular_polygon_area(perimeter, apothem):
    """Returns the area of a regular polygon"""
    return (perimeter * apothem) / 2


def circumference_area(radius):
    """Returns the area of a circumference"""
    return 3.14159*radius*radius


if __name__ == '__main__':
    import unittest

    class GeometrySuite(unittest.TestCase):

        def setUp(self):
            self.dict_squares_area = {
                1 : 1,
                4 : 2,
                9 : 3,
            }

            self.dict_rectangle_area = {
                2 : (1,2),
                6 : (2,3),
                12 : (3,4),
            }

            self.dict_triangle_area ={
                1 : (1,2),
                3 : (2,3),
                6 : (3,4),
            }
            
            self.dict_rhombus_area ={
                1 : (1,2),
                3 : (2,3),
                6 : (3,4),
            }

            self.dict_trapezoid_area ={
                4.5 : (1,2,3),
                10 : (2,3,4),
                17.5 : (3,4,5),
            }

            self.dict_polygon_area ={
                1 : (1,2),
                3 : (2,3),
                6 : (3,4),
            }

            self.dict_circumference_area ={
                3.14159 : 1,
                12.56636 : 2,
                50.26544 : 4,
            }


        def test_square_area(self):
            for key, value in self.dict_squares_area.items():
                self.assertEqual(key, square_area(value))


        def test_rectangle_area(self):
            for key, value in self.dict_rectangle_area.items():
                self.assertEqual(key, rectangle_area(value[0], value[1]))


        def test_triangle_area(self):
            for key, value in self.dict_triangle_area.items():
                self.assertEqual(key, triangle_area(value[0], value[1]))


        def test_rhombus_area(self):
            for key, value in self.dict_rhombus_area.items():
                self.assertEqual(key, rhombus_area(value[0], value[1]))


        def test_trapezoid_area(self):
            for key, value in self.dict_trapezoid_area.items():
                self.assertEqual(key, trapezoid_area(value[0], value[1], value[2]))

        def test_regular_polygon_area(self):
            for key, value in self.dict_polygon_area.items():
                self.assertEqual(key, regular_polygon_area(value[0], value[1]))

        def test_circumference_area(self):
            for key, value in self.dict_circumference_area.items():
                self.assertEqual(key, circumference_area(value))

        def tearDown(self):
            del(self.dict_squares_area)
            del(self.dict_rectangle_area)
            del(self.dict_triangle_area)
            del(self.dict_rhombus_area)
            del(self.dict_trapezoid_area)
            del(self.dict_polygon_area)
            del(self.dict_circumference_area)

    unittest.main()
