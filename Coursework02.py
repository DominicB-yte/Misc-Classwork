# Temperature = int(input ("What is the current temperature? (in Farenheit): "))
# if Temperature > 90:
#     print("I recommend you wear a swim suit.")
# elif Temperature > 70:
#         print("I recommend you wear shorts.")
# elif Temperature > 50:
#         print("I recommend you wear long pants.")
# elif Temperature <= 50:
#         print("I recommend you wear shorts.")

# StudentList1 = []
# print("**Student1\r\n")
# for x in range (1,5):
#     Grade1 = float(input ("Please input the result from Course" + str(x) + "\t: "))
#     StudentList1.append(Grade1)

# StudentList2 = []
# print("\r\n**Student2\r\n")
# for x in range (1,5):
#     Grade2 = float(input ("Please input the result from Course" + str(x) + "\t: "))
#     StudentList2.append(Grade2)

# StudentList3 = []
# print("\r\n**Student3\r\n")
# for x in range (1,5):
#     Grade3 = float(input ("Please input the result from Course" + str(x) + "\t: "))
#     StudentList3.append(Grade3)


# Avg1 = sum(StudentList1) / len(StudentList1)
# print("\r\nStudent1 Average Grade : " + str(round(Avg1, 3)))

# Avg2 = sum(StudentList2) / len(StudentList2)
# print("\r\nStudent2 Average Grade : " + str(round(Avg2, 3)))

# Avg3 = sum(StudentList3) / len(StudentList3)
# print("\r\nStudent3 Average Grade : " + str(round(Avg3, 3)))


# if Avg1 <= 4.00 and Avg1 >= 3.67:
#     print("\r\nStudent1 GPA : A")
# elif Avg1 <= 3.67 and Avg1 >= 3.00:
#     print("\r\nStudent1 GPA : B")
# elif Avg1 <= 3.00 and Avg1 >= 2.00:
#     print("\r\nStudent1 GPA : C")
# elif Avg1 <= 2.00:
#     print("\r\nStudent1 GPA : F")

# if Avg2 <= 4.00 and Avg2 >= 3.67:
#     print("\r\nStudent2 GPA : A")
# elif Avg2 <= 3.67 and Avg2 >= 3.00:
#     print("\r\nStudent2 GPA : B")
# elif Avg2 <= 3.00 and Avg2 >= 2.00:
#     print("\r\nStudent2 GPA : C")
# elif Avg2 <= 2.00:
#     print("\r\nStudent2 GPA : F")

# if Avg3 <= 4.00 and Avg3 >= 3.67:
#     print("\r\nStudent2 GPA : A")
# elif Avg3 <= 3.67 and Avg3 >= 3.00:
#     print("\r\nStudent2 GPA : B")
# elif Avg3 <= 3.00 and Avg3 >= 2.00:
#     print("\r\nStudent2 GPA : C")
# elif Avg3 <= 2.00:
#     print("\r\nStudent2 GPA : F")

# EmpName = input ("Please enter your Full Name :")
# WorkHours = int(input ("Please enter the amount of hours you've worked :"))

# Overtime = WorkHours - 40
# PayRate = 20
# OverPayRate = 25
# TotalPay = (WorkHours * PayRate) + (Overtime * OverPayRate)
# Tax = None

# print("Employee Name : ", EmpName)
# print("Total hours worked : ", WorkHours)
# if WorkHours < 40:
#     print("Regular hours worked : ", WorkHours)
# else:
#     print("Regular hours worked : 40")
# print("Regular pay rate : ", PayRate, " NZD")
# if WorkHours < 40:
#     print("Overtime hours worked : 0")
# else:
#     print("Overtime hours worked : ", Overtime)
# print("Overtime pay rate : ", OverPayRate, " NZD")
# print("Total Payment : ", TotalPay)
# if TotalPay > 700:
#     Tax = TotalPay * 0.30
# elif TotalPay <= 700 and TotalPay > 500:
#     Tax = TotalPay * 0.25
# elif TotalPay <= 500 and TotalPay > 350:
#     Tax = TotalPay * 0.15
# elif TotalPay < 350:
#     Tax = TotalPay * 0.05
# print("Amount taxed : ", Tax)
# NetTotal = TotalPay - Tax
# print("Net Payment : ", NetTotal)

# NumList = []
# Num1 = int(input ("First Number :"))
# NumList.append(Num1)
# while True:
#     Num2 = int(input ("Next Number :"))
#     if Num2 == 0:
#         i = len(NumList)
#         break
#     NumList.append(Num2)
#     print(NumList)
# print ("Total numbers typed :", i)

# for i in range(0,4):
#     for j in range(0, 4):
#         if i == j and j == i:
#             continue
#         print(i,",",j)

# Num1 = 1
# Num2 = 1
# NewNum = 0
# print(Num1)
# print(Num2)

# while True:
#     NewNum = Num1 + Num2
#     if NewNum > 1000:
#         break
#     print (NewNum)
#     Num1 = Num2
#     Num2 = NewNum

while True:
    LoopAmount = int(input ("Please enter a positive interger: "))
    Num1 = 1
    Num2 = 1
    NewNum = 0
    i = 2
    while i < LoopAmount:
        NewNum = Num1 + Num2
        if i > LoopAmount:
            break
        Num1 = Num2
        Num2 = NewNum
        i = i + 1
    print (NewNum)

