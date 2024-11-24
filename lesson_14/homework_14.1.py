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
#     GROUP_SIZE = 10
#
#     def __init__(self, number):
#         self.number = number
#         self.group = {}
#
#     def __str__(self):
#         return "\n".join(str(el) for el in self.group)
#
#     def add_student(self, student: Student):
#         if not isinstance(student, Student):
#             print("This is not a student")
#             return
#
#         if len(self.group) <= self.GROUP_SIZE:
#             self.group.update({student.last_name: student})
#         else:
#             raise GroupIsCrowdedError("Error! Group has already had 10 students!")
#
#     def find_student(self, last_name):
#         return self.group[last_name]
#
#     def delete_student(self, last_name):
#         if last_name in self.group:
#             self.group.pop(last_name)
#         print(f"Student {last_name} removed.")
#
#
# class GroupIsCrowdedError(Exception):
#     """Error will be called if you try to add 11-th student to group."""
#
#
# if __name__ == "__main__":
#     students_data = [
#         ("Vitaliy", "Apache", "man", 18, "math"),
#         ("Kate", "Lothbrok", "girl", 19, "math"),
#         ("Alex", "Goodzie", "man", 17, "math"),
#         ("Vika", "Belka", "girl", 19, "math"),
#         ("Sasha", "Shillk", "man", 18, "math"),
#         ("Margo", "Alamab", "girl", 17, "math"),
#         ("Mason", "Devete", "man", 18, "math"),
#         ("Ulya", "Arish", "girl", 19, "math"),
#         ("Rita", "Villers", "girl", 18, "math"),
#         ("Dasha", "Nottrust", "girl", 18, "math"),
#     ]
#
#     group_1 = Group(1)
#     for data in students_data:
#         student = Student(*data)
#         group_1.add_student(student)