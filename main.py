from university.student import Student


def main():

    students=[]
    
    students.append(Student("Jalal",1001))
    students.append(Student("Kamal",1002))
    
    for s in students:
        print(s)

if __name__ == "__main__":
    main()