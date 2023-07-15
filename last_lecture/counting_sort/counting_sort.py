def counting_sort(array: list[int]) -> None:
    max_value = max(array)
    count = [0] * (max_value + 1)

    for num in array:
        count[num] += 1

    # size = len(count)
    size = max_value + 1
    output = [0] * len(array)

    print(count), 8,

    for i in range(1, size):
        count[i] += count[i - 1]

    i = 0
    while i < len(array):
        current = count[array[i]] - 1
        output[current] = array[i]
        count[array[i]] -= 1
        i += 1

    for i in range(0, len(array)):
        array[i] = output[i]


array = [4, 2, 2, 8, 3, 3, 1]

counting_sort(array)
print(array)  # [1, 2, 2, 3, 3, 4, 8]
