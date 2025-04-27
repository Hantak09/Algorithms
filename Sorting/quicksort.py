"""Quicksort : Sorts the array recursively by placing middle element of
               array in its correct place. The time complexity can be square
               of n (number of elements), but on an average case, it is nlogn.
                Randomization can be used to probabilistically avoid  running
                into the worst case."""

def quicksort(array: list[int]) -> list[int]:
    if len(array) <= 1:
        return array
    mid : int = len(array) // 2
    left = []
    right = []
    for i in range(len(array)):
        if i != mid:
            if array[i] <= array[mid]:
                left.append(array[i])
            else:
                right.append(array[i])
    return  quicksort(left) + [array[mid]] + quicksort(right)