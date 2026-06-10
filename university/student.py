"""Student module for simple university example"""

class Student():
    """Represents a student with basic details."""


    def __init__(self, name, id, ):
        self.name = name
        self.id = id

        self.courses = {}

    def add_course(self, course_id, mark = None):
        self.courses[course_id] = mark 

    def get_gpa(self): 

        nums = 0
        sum = 0
        for k, v in self.courses.items():# id -> mark
            if v :
                sum += v
                nums += 1

        if nums:
            return sum / nums
        
        return None  

    def __str__(self):
        s = "=================================\n"
        s += f"name: {self.name}, id:{self.id}\n"
        s += f"GPA: {self.get_gpa()}\n"
        s += f"Courses: {str(self.courses)}\n"
        s += "================================="

        return s


def main():
    """This is a test fdunction for Student class"""
    
    print("test1: ")
    s1 = Student("John Doh",1001)
    s1.add_course("B100S032026", 100)
    s1.add_course("B103S032026", 50)

    print(s1)

if __name__ == "__main__":
    main()