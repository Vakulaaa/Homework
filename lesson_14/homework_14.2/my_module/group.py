from man import Student
from exceptions import GroupIsCrowdedError


class Group:
    GROUP_SIZE = 10
    def __init__(self, number):
        self.number = number
        self.group = []

    def __str__(self):
        return "\n".join(str(el) for el in self.group)

    def add_student(self, student):
        if isinstance(student, Student):
            if len(self.group) <= self.GROUP_SIZE:
                self.group.append(student)
            else: raise GroupIsCrowdedError("Error! Group has already had 10 students!")

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def delete_student(self, last_name):
        self.group.remove(self.find_student(last_name))
        print(f"Student {last_name} removed.")

