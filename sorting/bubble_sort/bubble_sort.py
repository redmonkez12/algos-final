def bubble_sort(array: list[int]) -> None:
    size = len(array)
    for i in range(size):
        swapped = False

        for j in range(size - 1 - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True

        if not swapped:
            break
