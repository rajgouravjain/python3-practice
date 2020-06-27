import os
from operator import itemgetter, attrgetter

s1 = "hello"
s2 = "olleh"
if (sorted(s1) == sorted(s2)):
    print("Same")
else :
    print("Different")

print(sorted("This is a gtest string that will be soreted".split(),key=str.lower))


students = [('ram',34),('shyam',88),('kiran',80),('meera',90)]

print(sorted(students,key=lambda student: student[1],reverse=True))

print(sorted(students,key=itemgetter(1),reverse=False))

class Student(object):
    def __init__(self, name="johndoe",marks=0):
        self.name = name
        self.marks = marks
    def __repr__(self):
        return repr((self.name,self.marks))

student_objs = [Student("ram",98),Student('shyam',55),Student('meera',88)]

print(sorted(student_objs,key=lambda student_obj: student_obj.name))
print(sorted(student_objs, key=attrgetter('marks'), reverse=False))
