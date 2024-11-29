# from man import Student
# from group import Group
#
#
# if __name__ == "__main__":
#     student_1 = Student("Vitaliy", "Apache", "man", 18, "math")
#     student_2 = Student("Kate", "Lothbrok", "girl", 19, "math")
#     student_3 = Student("Alex", "Goodzie", "man", 17, "math")
#     student_4 = Student("Vika", "Belka", "girl", 19, "math")
#     student_5 = Student("Sasha", "Shillk", "man", 18, "math")
#     student_6 = Student("Margo", "Alamab", "girl", 17, "math")
#     student_7 = Student("Mason", "Devete", "man", 18, "math")
#     student_8 = Student("Ulya", "Arish", "girl", 19, "math")
#     student_9 = Student("Rita", "Villers", "girl", 18, "math")
#     student_10 = Student("Dasha", "Nottrust", "girl", 18, "math")
#
#     group_1 = Group(1)
#
#     group_1.add_student(student_1)
#     group_1.add_student(student_2)
#     group_1.add_student(student_3)
#     group_1.add_student(student_4)
#     group_1.add_student(student_5)
#     group_1.add_student(student_6)
#     group_1.add_student(student_7)
#     group_1.add_student(student_8)
#     group_1.add_student(student_9)
#     group_1.add_student(student_10)
#
#     print(group_1.find_student("Nottrust"))
#     group_1.delete_student("Apache")
#
#     assert group_1.find_student("Villers") == student_9