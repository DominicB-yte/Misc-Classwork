# Num = int(input("Please enter a number! : "))
# if 0 < Num:
#     print ("Cool! you're Positive")
# else:
#     print ("Not Cool! you're HIV Positive")

# Num = int(input("Please enter a number! : "))
# NumNew = Num % 2
# if NumNew == 0:
#     print ("This number is even!")

# Num1 = int(input("Please enter your first number! : "))
# Num2 = int(input("Please enter your second number! : "))
# if Num1 > Num2:
#     print (Num1, "is larger than", Num2)
# else:
#     print (Num2, "is larger than ", Num1)

# Employee = input ("Please enter your Firstname :")
# SalaryNum = int(input ("Please input the amount you earn on sales :"))

# if SalaryNum > 499999:
#     print ("Congratulations", Employee, ",", end='\0')
#     print ("you're entitled to a bonus!")

# if SalaryNum < 499999:
#     print ("Sorry", Employee, ",", end='\0')
#     print ("you're not entitled to a bonus.")

# Employee = input ("Please enter your Firstname :")
# SalaryNum = int(input ("Please input the amount you earn on sales :"))

# if SalaryNum > 499999:
#     print ("Congratulations", Employee, ",", end='\0')
#     print ("you're entitled to a bonus!")

# else:
#     print ("Sorry", Employee, ",", end='\0')
#     print ("you're not entitled to a bonus.")

# Num = int(input("Please enter a number! : "))
# NumNew = Num % 2
# if NumNew == 0:
#     print ("This number is even!")
# else:
#     print ("This number is odd!")

# Num1 = input ("Please enter the first number :")
# Num2 = input ("Please enter the second number :")
# Num3 = input ("Please enter the third number :")

# if Num1 > Num2 and Num1 > Num3:
#     print ("The First number was the largest, being ", Num1)
# elif Num2 > Num1 and Num2 > Num3:
#     print ("The Second number was the largest, being", Num2)
# elif Num3 > Num1 and Num3 > Num2:
#     print ("The Third number was the largest, being", Num3)

# Lugg = int(input ("Please enter the weight of your luggage in kilograms :"))

# if Lugg > 20:
#     print ("There is a $25 fee for overweight luggage")
# elif Lugg == 20:
#     print ("Your luggage in on the threshold for being overweight")
# elif Lugg < 20:
#     print ("Have a safe flight!")

# Age = int(input ("Please input your age :"))
# if Age > 18:
#     print ("Adult")
# elif Age <= 3:
#     print ("Infant")
# elif Age <= 7:
#     print ("Baby")
# elif Age <= 13:
#         print ("Child")
# elif Age <= 18:
#         print ("Teenager")

# import sys
# Grade = float(input ("Please enter the grade you received :"))
# if Grade >= 0 and Grade <= 39.99:
#     print ("Your final grade is an E")
# elif Grade >= 40 and Grade <= 44.99:
#     print ("Your final grade is an D")
# elif Grade >= 45 and Grade <= 59.99:
#     print ("Your final grade is an C")
# elif Grade >= 60 and Grade <= 74.99:
#     print ("Your final grade is an B")
# elif Grade >= 75 and Grade <= 100:
#     print ("Your final grade is an A")
# elif Grade > 100 or Grade < 0:
#     sys.exit()

# n = 1
# while n < 101:
#     print (n)
#     n += 1

# NumList = []
# Num1 = int(input ("First Number :"))
# while True:
#     Num2 = int(input ("Next Number :"))
#     if Num2 < 0:
#         i = Num1 + sum(NumList)
#         break
#     NumList.append(Num2)
#     print(NumList)
# print ("Total is :", i)

# for y in range(2, 302, 2):
#     print(y)
# print("Done")

# import random
# for x in range(0, 101):
#     y = random.randint(5, 500)
#     print(y)
# print("Done")

for a in range(1,11):
    for b in range(1, 11):
        print(a, 'x', b, '=', a*b)