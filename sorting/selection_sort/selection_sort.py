def selection_sort(array: list[int]) -> None:
    size = len(array)

    for i in range(size):
        min_index = i

        for j in range(i + 1, size):
            if array[j] < array[min_index]:
                min_index = j

        array[i], array[min_index] = array[min_index], array[i]
