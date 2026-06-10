"""Course module represents courses"""

class Course():
    """Represents courses"""

    def __init__(self, name, id, credit = 1,):
        
        self.name = name
        self.id = id
        self.credit = credit

        self.students = dict() #dict id of students in the class -> marks

    def add_student(self, student_id, mark = None):
        
        self.students[student_id] = mark

    def get_average_mark(self):

        nums = 0
        sum = 0
        for k, v in self.students.items():# id -> mark
            if v :
                sum += v
                nums += 1

        if nums:
            return sum / nums
        
        return None


    def __str__(self):
        s = "=================================\n"
        s += f"name: {self.name}, id:{self.id}\n"
        s += f"average mark: {self.get_average_mark()}\n"
        s += f"Students: {str(self.students)}\n"
        s += "================================="

        return s

def main():

    course1 = Course("Python", "B100", 5 )
    
    course1.add_student(1001, 80)
    course1.add_student(1002, 50)

    print(course1)


if __name__ == "__main__":
    main()