# NumberList = []
# Num1 = int(input("Enter the first number: "))
# NumberList.append(Num1)

# while True:
#     Num2 = int(input("Enter the next number, or Zero to exit: "))
#     if Num2 == 0:
#         break
#     NumberList.append(Num2)

# NumberList.reverse()
# print(NumberList)

# MessageList = []
# i = 1

# while i <= 5:
#     Message = input("Please enter message " + str(i) + ": ")
#     MessageList.append(Message)
#     i = i + 1

# SeeMessage = int(input("Which message would you like to see?: "))
# print(MessageList[SeeMessage - 1])

# NumList = []
# FirstNum = int(input("Please enter the first number: "))
# NumList.append(FirstNum)
# FinalTotal, i = 1, 0

# while i >= 0:
#     NextNum = int(input("Enter the next number, or 0 if finished: "))
#     if NextNum == 0:
#         break
#     elif i == 0:
#         FinalTotal = FinalTotal * FirstNum
#     NumList.append(NextNum)
#     FinalTotal = FinalTotal * NextNum

# print(NumList, "Multiplied together is: ", FinalTotal)

# FriendList = []
# FirstFriend = input("Please enter the name of a friend: ")
# FriendList.append(FirstFriend)

# while True:
#     NextFriend = input("Please enter another name, or press enter if finished: ")
#     if not NextFriend:
#         break 
#     FriendList.append(NextFriend)

# for friend in FriendList:
#     print(friend)

# def Courses():
#     while True:
#         NextCourse = input("Please enter another name, or press enter if finished: ")
#         if not NextCourse:
#             break 
#         CourseList.append(NextCourse)

# def Grading():
#     for course in CourseList:
#         CourseGrade = int(input("Enter your grade for " + course + ": "))
#         GradeList.append(CourseGrade)

# CourseList = []
# GradeList = []
# FirstCourse = input("Please enter the name of the first course: ")
# CourseList.append(FirstCourse)
# Courses()
# Grading()

# grades = 0
# for course in CourseList:
#     print(course, "Grade: ", GradeList[grades])
#     grades = grades + 1

# FinalGrade = sum(GradeList)/len(GradeList)
# print("Your final GPA is: ", round(FinalGrade, 1))

def InCommon():
    ListC = (set(ListA).intersection(ListB))
    if "" not in ListC:
        print("Common numbers are:", ListC)
    else:
        print("There are no items in common")

ListA = []
ListB = []

while True:
    ItemA = int(input("Enter a number for list A: "))
    if ItemA == 0:
        break
    else:
        ListA.append(ItemA)

while True:
    ItemB = int(input("Enter a number for list B: "))
    if ItemB == 0:
        break
    else:
        ListB.append(ItemB)

InCommon()