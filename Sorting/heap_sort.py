
"""max_heapify : Places the element at index 'i' at its position in the heap."""
def max_heapify(array: list[int], index: int, heap_size: int) -> None:
    largest = index             # parent
    left = 2 * index + 1        # left child
    right = 2 * index + 2       # right child

    # select index that hold largest value among parent and children
    if left < heap_size and array[left] > array[largest]:
        largest = left
    if right < heap_size and array[right] > array[largest]:
        largest = right
    # exchange parent with child if parent does not hold larger value
    if largest != index:
        array[index], array[largest] = array[largest], array[index]
        # repeat until heap property does not hold on the respective branch
        max_heapify(array, largest, heap_size)


"""build_max_heap : Builds a max heap with each element follow the property"""
def build_max_heap(array: list[int]) -> None:
    heap_size = len(array)
    # since half of elements in the array/heap are leaves, they are already in place
    # so we only have to run the loop on the first half elements.
    for i in range((heap_size // 2) - 1, -1, -1):
        max_heapify(array, i, heap_size)


"""heapsort : Exchange the max element aka first element of heap with the last
              and heapify the first element. Repeat it for all the elements until
              the array is sorted."""
def heapsort(array: list[int]) -> None:
    build_max_heap(array)
    heap_size = len(array)
    for i in range(len(array) - 1, 0, -1):
        array[0], array[i] = array[i], array[0]
        heap_size -= 1
        max_heapify(array, 0, heap_size)