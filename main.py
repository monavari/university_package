from student import Student

def main():

    print("main function of main.py is called")
    print("name of the script:",__name__)
    # print("This sis the main function where i will implement the logic of the program")

    # example student
    students=[]
    
    students.append(Student("Jalal",1001))
    students.append(Student("Kamal",1002))
    
    for s in students:
        print(s)

if __name__ == "__main__":
    main()