# def Add(i, j): 
#     return (i + j) 

# Add(10, 9) 

# def Add(i, j):
#     return (i + j)

# print(Add(10, 9))

# def PrintX():
#     print("x")

# def MultipuleX():
#     Num = int(input ("Please enter an integer :"))
#     for _ in range(Num):
#         PrintX()

# MultipuleX()

# Num = int(input("Please enter an integer: "))
# def IsEven():
#     if Num % 2 == 0:
#         return True
#     elif Num % 2 != 0:
#         return False


# if IsEven():
#     print(Num, "is even")
# else:
#     print(Num, "is odd")

# TimesBy = int(input("Please insert a number to be used for it's times tables: "))

# def TimesMethod():
#     for a in range(1, 11):
#             print(a, 'x', TimesBy, '=', a*TimesBy)
# TimesMethod()

import Classwork05Module

def CalculateGPA():
    Avg1 = sum(GradeList) / len(GradeList)
    print("\r\n Average Grade for ", Name, "With student ID :", StudentID, ": " + str(round(Avg1, 3)))
    if Avg1 <= 4.00 and Avg1 >= 3.67:
        print("\r\nStudent1 GPA : A")
    elif Avg1 <= 3.67 and Avg1 >= 3.00:
        print("\r\nStudent1 GPA : B")
    elif Avg1 <= 3.00 and Avg1 >= 2.00:
        print("\r\nStudent1 GPA : C")
    elif Avg1 <= 2.00:
        print("\r\nStudent1 GPA : F")

Name, StudentID = Classwork05Module.ReadStudentInfo()
GradeList = Classwork05Module.ReadStudentGrades()
CalculateGPA()