def partition(array, low, high):
    pivot = array[high]

    i = low - 1  # -1
    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            (array[i], array[j]) = (array[j], array[i])

    (array[i + 1], array[high]) = (array[high], array[i + 1])

    return i + 1


def quick_sort(array, low, high):
    if low < high:
        part = partition(array, low, high)

        quick_sort(array, low, part - 1)  # beru levy list a aplikuji stejny algoritmus

        quick_sort(array, part + 1, high)  # beru pravy list a aplikuji stejny algoritmus


array = [-2, 45, 0, 11, -9, 88, -97, -202, 747]
# [-202, -97, -9, -2, 0, 11, 45, 88, 747]
quick_sort(array, 0, len(array) - 1)
print(array)
