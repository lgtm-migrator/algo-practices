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
