#Getting attributes
#operator.attrgetter

class Student:
    def __init__(self, name, major, gpa):
        self.name = name
        self.major = major
        self.gpa = gpa

    def __repr__(self):
        return "{}: {}".format(self.name, self.gpa)

student_objs = [
    Student("Joe Smith", "physics", 3.7),
    Student("Jane Jones", "chemistry", 3.8),
    Student("Zoe Grimwald", "literature", 3.4)
    ]
from operator import attrgetter
print(sorted(student_objs, key=attrgetter("gpa")))
