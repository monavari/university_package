"""Simple database IO for university"""
import os

from student import Student
from course import Course

STUDENT_DATABASE = "./data/student.csv"

#student: id, name, course1:mark, course2: mark

def write_student(student):

    with open(STUDENT_DATABASE, "a") as f:
        s = f"{student.id},{student.name}"

        for k,v in student.courses.items():
            s += f",{k}:{v}"

        s += "\n"
        f.write(s)


def read_students():

    students = []
    with open(STUDENT_DATABASE, "r") as f:

        while f:
            sl = f.readline()
            sl = sl.split(",")
            id, name = sl[0], sl[1]
            print(id,name)


def main():

    print("test1: ")
    s1 = Student("John Doh",1001)
    s1.add_course("B100S032026", 100)
    s1.add_course("B103S032026", 50)


    s2 = Student("Jahan",1002)
    s2.add_course("B100S032026", 90)
    s2.add_course("B103S032026", 80)

    write_student(s1)
    write_student(s2)

    read_students()


if __name__ == "__main__":

    main()