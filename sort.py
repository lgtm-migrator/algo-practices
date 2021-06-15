from typing import List


def bubble_sort(list: List[int]) -> List[int]:
    change = True
    while change:
        change = False
        for i in range(len(list)-1):
            if list[i] > list[i+1]:
                list[i], list[i+1] = list[i+1], list[i]
                change = True
    return list


def select_sort(list: List[int]) -> List[int]:
    for index in range(len(list)-1):
        min = index
        for j in range(index+1, len(list)):
            if list[j] < list[min]:
                min = j
        list[index], list[min] = list[min], list[index]
    return list


def binary_search(list: List[int], low: int, high: int, element: int):
    # Reached to the last operation
    if low == high:
        if list[low] > element:
            return low
        else:
            return low + 1

    mid = (low + high)/2
    # check whether middle value is greater than the element. If so, we skip to the half of lower elements.
    if list[mid] < element:
        return binary_search(list, mid+1, high, element)
    # The case middle value is smaller than the element is same way as the above.
    else:
        return binary_search(list, low, mid-1, element)


def insert_sort(list: List[int()]) -> List[int]:
    for i in range(1, len(list)):
        element = list[i]
        # search index where to insert the element.
        index = binary_search(list, 0, i-1, element)
        # Update the list by merging [element] into list[0:index] .... list[index:i] + list[i+1:]←not yet sorted
        list[:] = list[0:index] + [element] + list[index+1:i] + list[i+1:]
    return list


def quick_sort(list: List[int]) -> List[int]:
    left = []
    right = []
    length = len(list)
    if (length <= 1):
        return list

    # In this case, the reference value is at the middle of list.
    ref = list[(0+length)/2]
    # Store same values as reference value in list.
    ref_list = []

    for num in list:
        if num < ref:
            left.append(num)
        elif num > ref:
            right.append(num)
        else:
            ref_list.append(num)
    left = quick_sort(left)
    right = quick_sort(right)

    return left + ref_list + right
