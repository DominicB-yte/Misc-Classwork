# def PrintStrings():
#     for i in StringList:
#         print(i)

# String = input("Enter some text: ")
# StringList = list(String)
# PrintStrings()

# def IndexStrings():
#     VowelList = ["a", "e", "i", "o", "u"]
#     for i, char in enumerate(Stringlist):
#         if char in VowelList:
#             print(char, "is in index", i)

# String = input("Enter some text: ")
# Stringlist = list(String.lower())
# IndexStrings()

# def CommonStrings():
#     for i, j in enumerate(StringList):
#         if j in StringList2[i]:
#             print("Both string have" , j, "in index", i)

# String = input("Enter the first string:")
# String2 = input("Enter the second string:")
# StringList = list(String.lower())
# StringList2 = list(String2.lower())
# CommonStrings()

# def ConvertList():
#     StringList.reverse()
#     str1 = ''.join(StringList)
#     print(str1)

# String = input("Please enter some text: ")
# StringList = list(String)
# ConvertList()

# def OddList():
#     NewList = []
#     for i, j in enumerate(StringList):
#         if i % 2 == 0:
#             toAdd = StringList[i]
#             NewList.append(toAdd)
    
#     j = ''.join(NewList)
#     print(j)

# String = input("Please enter some text: ")
# StringList = list(String)
# OddList()

# def IndexList():
#     for i, j in enumerate(StringList):
#         if UserIndex > len(StringList):
#             print("Your number is out of range")
#             break
#         elif j == StringList[UserIndex]:
#             del StringList[UserIndex]
#             NewString = ''.join(StringList)
#             print(NewString)
#             break

# String = input("Please enter some text: ")
# UserIndex = int(input("Please enter a number: "))
# StringList = list(String)
# IndexList()

# def VowelCount():
#     print("There are", Text.count("a"), "\"A\" in the text")
#     print("There are", Text.count("e"), "\"E\" in the text")
#     print("There are", Text.count("i"), "\"I\" in the text")
#     print("There are", Text.count("o"), "\"O\" in the text")
#     print("There are", Text.count("u"), "\"U\" in the text")

# UserInput = input("Please enter some text: ")
# Text = list(UserInput.lower())
# VowelCount()

import re
def WoodCount():
    Counted = 1
    for i in WoodSplit:
        if re.search("woodchuck", i):
            Counted = Counted
        elif re.search("wood.", i):
            Counted = Counted + 1
    print("The word wood occurs", Counted, "times")

WoodString = """How much wood would a woodchuck chuck If a woodchuck could chuck wood? He would chuck, he would, as much as he could, And chuck as much as a woodchuck would If a woodchuck could chuck wood."""

print(WoodString)
WoodString.lower()
WoodSplit = list(WoodString.split())
WoodCount()