import random

"""partition: Function that sorts the pivot inplace."""
def partition(array: list[int], low: int, high: int) -> int:
    pivot : int = array[high]
    i : int = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i+1], array[high] = array[high], array[i+1]
    return i + 1


"""Quicksort: Sorts the array recursively by placing middle element of
              array in its correct place. The time complexity can be square
              of n (number of elements), but on an average case, it is nlogn.
              Randomization can be used to probabilistically avoid  running
              into the worst case."""

def quicksort(array: list[int], randomized = False) -> list[int]:
    if len(array) <= 1:
        return array
    if randomized:
        mid = random.randint(0, len(array) - 1)
    else:
        mid : int = len(array) // 2
    left = []
    right = []
    for i in range(len(array)):
        if i != mid:
            if array[i] <= array[mid]:
                left.append(array[i])
            else:
                right.append(array[i])
    if randomized:
        return quicksort(left, randomized=True) + [array[mid]] + quicksort(right, randomized=True)
    return  quicksort(left) + [array[mid]] + quicksort(right)

"""quicksort_inplace : Version of quicksort algorithm that does not required extra space."""
def quicksort_inplace(array: list[int], low: int, high: int) -> None:
    if low < high:
        part : int = partition(array, low, high)
        quicksort_inplace(array, low, part - 1)
        quicksort_inplace(array, part + 1, high)