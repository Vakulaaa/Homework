#
# class Man:
#     def __init__(self, first_name, last_name, sex, age):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.sex = sex
#         self.age = age
#
#     def __str__(self):
#         return f"Human: {self.first_name, self.last_name} is {self.age} years old {self.sex}."
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
#         return f"Student: {self.first_name, self.last_name} is {self.age} years old {self.sex}."
#
#
# class Group:
#     def __init__(self, number):
#         self.number = number
#         self.group = []
#
#     def __str__(self):
#         return "\n".join(str(el) for el in self.group)
#
#     def add_student(self, student):
#         if isinstance(student, Student):
#             self.group.append(student)
#
#     def find_student(self, last_name):
#         for student in self.group:
#             if student.last_name == last_name:
#                 return student
#             else: return None
#
#     def delete_student(self, last_name):
#         self.find_student(last_name).remove()
#
#
# student_1 = Student("Vitaliy", "Apache", "man", 18, "math")
# group_1 = Group(1)
# group_1.add_student(student_1)
# print(group_1.find_student("Apache"))
# print(group_1)
