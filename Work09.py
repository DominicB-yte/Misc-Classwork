# def Addition():
#     ListAdd = [1, 2, 3, 4, 5]
#     sumn = 0
#     for i in ListAdd:
#         sumn += i
#     return sumn

# print(Addition())

# def Multiplication():
#     ListMul = [1, 2, 3, 4, 5]
#     sumn = 1
#     for i in ListMul:
#         sumn = sumn * i
#     return sumn

# print(Multiplication())

# def Maximum():
#     ListMax = [1, 2, 3, 4, 5]
#     for i in ListMax:
#         if i > i + 1:
#             break
#         else:
#             continue
#     MaxValue = i
#     return MaxValue

# print(Maximum())


# def Duplicate():
#     ListDupe = [1, 2, 3, 3, 4, 5, 5]
#     ListDupe = list(dict.fromkeys(ListDupe))
#     return ListDupe

# print(Duplicate())

# def CopyList():
#     MainList = [1, 2, 3, 4, 5]
#     NewList = []
#     for i in MainList:
#         NewItem = i
#         NewList.append(NewItem)
#     return NewList

# print(CopyList())

# List1 = [1, 2, 3, 4, 5]
# List2 = [5, 1, 2, 3, 4]
# List3 = [4, 5, 1, 2, 3]
# def Similar():
#     if List1[-1] == List2[0]:
#         print("List 1 and List 2 are circularly identical")
#     elif List2[-1] == List3[0]:
#         print("List 2 and List 3 are circularly identical")
#     elif List3[-1] == List1[0]:
#         print("List 3 and List 1 are circularly identical")
#     else:
#         print("None of the lists are circulary identical")

# Similar()

# List1 = [1, 2, 3, 4, 5]
# def SecondMin():
#     List1.sort
#     print(List1[1])

# SecondMin()

def get_string():
    return "Selenium"

def get_list():
    return ["dog", "cat"]

def test_string_equal():
    assert get_string() == "Selenium"

def test_in_list():
    assert "elephant" in get_list()