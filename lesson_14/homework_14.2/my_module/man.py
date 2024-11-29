#
# class Man:
#     def __init__(self, first_name, last_name, sex, age):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.sex = sex
#         self.age = age
#
#     def __str__(self):
#         return f"Human: {self.first_name} {self.last_name} is {self.age} years old {self.sex}."
#
#
#
# class Student(Man):
#     def __init__(self, first_name, last_name, sex, age, subject):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.sex = sex
#         self.age = age
#         self.subject = subject
#
#     def __str__(self):
#         return f"Student: {self.first_name} {self.last_name} is {self.age} years old {self.sex}."
#
#     def __eq__(self, other):
#         if not isinstance(other, Student):
#             return NotImplemented
#         return self.last_name == other.last_name
#
