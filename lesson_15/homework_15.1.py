# import math
#
#
# class Rectangle:
#
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def __str__(self):
#         return f'Rectangle has width {self.width} and height {self.height}.'
#
#     def get_square(self):
#         return self.width * self.height
#
#     def __eq__(self, other):
#         if not isinstance(other, Rectangle):
#             return NotImplemented
#         return self.get_square() == other.get_square
#
#     def __add__(self, other):
#         if not isinstance(other, Rectangle):
#             return NotImplemented
#         total_area = self.get_square() + other.get_square()
#         return Rectangle._create_from_area(total_area)
#
#     def __mul__(self, n):
#         if not isinstance(n, (int, float)) or n <= 0:
#             raise ValueError("Multiplier must be a positive number")
#         new_area = self.area * n
#         return Rectangle._create_from_area(new_area)
#
#     @staticmethod
#     def _create_from_area(area):
#         side = math.sqrt(area)
#         width = math.floor(side)
#         height = math.ceil(area / width)
#         return Rectangle(width, height)
#
#
# r1 = Rectangle(2, 4)
# r2 = Rectangle(3, 6)
# assert r1.get_square() == 8, 'Test1'
# assert r2.get_square() == 18, 'Test2'
#
# r3 = r1 + r2
# assert r3.get_square() == 26, 'Test3'
#
# r4 = r1 * 4
# assert r4.get_square() == 32, 'Test4'
#
# assert Rectangle(3, 6) == Rectangle(2, 9), 'Test5'
