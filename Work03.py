# print("The first 10 natural numbers are :")
# NatNums = []
# for i in range(0, 11):
#     print(i)
#     NatNums.append(i)
#     i = i + 1

# print("\nThe sum of all the numbers is :", sum(NatNums))

# ManualNums = int(input ("Please input a number :"))
# print("The first set natural numbers are :")
# NatNums = []
# for i in range(0, ManualNums + 1):
#     print(i)
#     NatNums.append(i)
#     i = i + 1

# print("\nThe sum of all the numbers is :", sum(NatNums))

# NumToCube = int(input ("Expected number :"))
# for i in range(1, NumToCube + 1):
#     CubedNum = i ** i
#     print("Number is :", i, "and ", i, "cubed is", CubedNum)
#     i = i + 1

# TimesBy = int(input ("Please insert a number to be used for it's times tables :"))
# for a in range(TimesBy + 1):
#         print(a, 'x', TimesBy, '=', a*TimesBy)

# NumAmount = int(input ("Please insert the amount fo numbers to count up to :"))
# i = 0
# Num1 = 1
# Num2 = 0
# MyNums = []

# while i < NumAmount:
#     print(Num1)
#     MyNums.append(Num1)
#     Num2 = Num1 + 2
#     Num1 = Num2
#     i += 1

# print("The sum of all theses numbers is :", sum(MyNums))

# for i in range(1, 51):
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#         continue
#     elif i % 3 == 0:
#         print("Fizz")
#         continue
#     elif i % 5 == 0:
#         print("Buzz")
#         continue
#     print(i)

# for i in range(1, 6):
#     print(str(i) * i)

# Balance = float(input ("Please input your current bank balance :"))
# Interest = float(input ("Please input your annual interest as a decimal :"))
# Goal = float(input ("Please input your desired bank balance :"))

# for i in range(int(Balance), int(Goal)):
#     if Balance > Goal:
#         break
#     Balance = Balance * (1 + Interest)
#     print(round(Balance, 2))

# Name = input ("Please enter your name :")
# AmountOfA = 0
# AmountOfE = 0
# AmountOfI = 0
# AmountOfO = 0
# AmountOfU = 0
# VowelList = []

# if 'a' or 'e' or 'i' or 'o' or 'u' in Name.lower():
#     AmountOfA = Name.lower().count("a")
#     AmountOfE = Name.lower().count("e")
#     AmountOfI = Name.lower().count("i")
#     AmountOfO = Name.lower().count("o")
#     AmountOfU = Name.lower().count("u")
# VowelList = AmountOfA, AmountOfE, AmountOfI, AmountOfO, AmountOfU

# print("A = ", AmountOfA)
# print("E = ", AmountOfE)
# print("I = ", AmountOfI)
# print("O = ", AmountOfO)
# print("U = ", AmountOfU)
# print("The sum of all vowels is :", sum(VowelList))

# import random
# print("Guess the random number between 1-100, you only have 5 guesses!")
# RanNumber = random.randint(1, 101)

# for i in range(5):
#     Guess = int(input (":"))
#     if Guess > RanNumber:
#         print("Too High!")
#     elif Guess < RanNumber:
#         print("Too Low!")
#     elif Guess == RanNumber:
#         print("Correct!")
#         break
# print("Game over! The number was :", RanNumber)

numbers = [53, 345, 2, 2, 99, -12, 0, 1899, -123, 76 , 55, -4, 2]

length = len(numbers)
for i in range(length):
    for j in range(0, length-1):
        if numbers[j] > numbers[j+1]:
            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
print(numbers)