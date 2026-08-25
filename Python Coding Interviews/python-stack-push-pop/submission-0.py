from typing import List


def reverse_list(arr: List[int]) -> List[int]:
    arr2 = []

    while len(arr) > 0:
        top_element = arr.pop()
        arr2.append(top_element)

    return arr2

    #return a new list of integers in reverese order. 



# do not modify below this line
print(reverse_list([1, 2, 3]))
print(reverse_list([3, 2, 1, 4, 6, 2]))
print(reverse_list([1, 9, 7, 3, 2, 1, 4, 6, 2]))
