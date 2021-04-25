def ReadStudentInfo():
    Name = input("Please enter your name: ")
    ID = input("Please enter your ID Number: ")
    return Name,ID

def ReadStudentGrades():
    StudentList1 = []
    print("**Student1\r\n")
    for x in range (1,5):
        Grade1 = float(input ("Please input the result from Course" + str(x) + "\t: "))
        StudentList1.append(Grade1)
    return StudentList1