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
