# from math import gcd
#
#
# class ProperFraction:
#     def __init__(self, numerator, denominator):
#         if denominator == 0:
#             raise ValueError("Denominator cannot be zero.")
#         if numerator >= denominator:
#             raise ValueError("The fraction is not proper (numerator >= denominator).")
#         self.numerator = numerator
#         self.denominator = denominator
#         self.simplify()
#
#     def simplify(self):
#         common_divisor = gcd(self.numerator, self.denominator)
#         self.numerator //= common_divisor
#         self.denominator //= common_divisor
#
#     def __repr__(self):
#         return f"{self.numerator}/{self.denominator}"
#
#     def __add__(self, other):
#         numerator = self.numerator * other.denominator + other.numerator * self.denominator
#         denominator = self.denominator * other.denominator
#         return ProperFraction(numerator, denominator)
#
#     def __sub__(self, other):
#         numerator = self.numerator * other.denominator - other.numerator * self.denominator
#         denominator = self.denominator * other.denominator
#         if numerator < 0:
#             raise ValueError("Resulting fraction is negative.")
#         return ProperFraction(numerator, denominator)
#
#     def __mul__(self, other):
#         numerator = self.numerator * other.numerator
#         denominator = self.denominator * other.denominator
#         return ProperFraction(numerator, denominator)
#
#     def __eq__(self, other):
#         return self.numerator == other.numerator and self.denominator == other.denominator
#
#     def __lt__(self, other):
#         return self.numerator * other.denominator < other.numerator * self.denominator
#
#     def __le__(self, other):
#         return self.numerator * other.denominator <= other.numerator * self.denominator
#
#     def __gt__(self, other):
#         return self.numerator * other.denominator > other.numerator * self.denominator
#
#     def __ge__(self, other):
#         return self.numerator * other.denominator >= other.numerator * self.denominator
#
#
# try:
#     f1 = ProperFraction(1, 3)
#     f2 = ProperFraction(2, 5)
#
#     print("Дробь 1:", f1)
#     print("Дробь 2:", f2)
#
#     print("Сума:", f1 + f2)
#     print("Разниця:", f1 - f2)
#     print("Произведение:", f1 * f2)
#
#     print("f1 < f2:", f1 < f2)
#     print("f1 == f2:", f1 == f2)
# except ValueError as e:
#     print("Ошибка:", e)
