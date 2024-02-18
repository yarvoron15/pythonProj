""""ТУТ НЕМНОГО МОДИФИЦИРОВАЛ И СОЕДЕНИЛ ФУНКЦИИ"""
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

unsorted_list = [64, 34, 25, 12, 22, 11, 90]
sorted_list = bubble_sort(unsorted_list)
print(sorted_list)


def binary_search(sorted_list, value):
    First = 0
    resultOk = False
    last = len(sorted_list) - 1
    pos = -1

    while First <= last:
        middle = (First + last) // 2
        if sorted_list[middle] == value:
            resultOk = True
            pos = middle
            break
        elif sorted_list[middle] < value:
            First = middle + 1
        else:
            last = middle - 1

    if resultOk:
        print("The number is found")
        print(pos)
    else:
        print("The number is not found")


# Using the sorted list from bubble_sort function
value = int(input("Enter the number: "))
binary_search(sorted_list, value)

"""" А ТУТ ИЩЕТ КАК В БЛОК СХЕМЕ И ФУНКЦИИ НЕ СОЕДЕНЕНЫ """
# def bubble_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         for j in range(0, n-i-1):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#     return arr
#
# unsorted_list = [64, 34, 25, 12, 22, 11, 90]
# sorted_list = bubble_sort(unsorted_list)
# print(sorted_list)
#
#
# def binary_search(N, value):
#     First = 0
#     resultOk = False
#     last = N - 1
#     pos = -1
#
#     while First < last:
#         middle = (First + last) // 2
#         if value == middle:
#             First = middle
#             last = First
#             resultOk = True
#             pos = middle
#         else:
#             if value > middle:
#                 First = middle + 1
#             else:
#                 last = middle - 1
#
#     if resultOk == True:
#         print("The number is found")
#         print(pos)
#     else:
#         print("The number is not found")
#
#
# N = 5000
# value =  int(input("Enter the number: "))
# binary_search(N, value)




