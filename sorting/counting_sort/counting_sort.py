# def counting_sort(array):
#     size = len(array)
#     output = [0] * size
#
#     # Initialize count array
#     count = [0] * 10
#
#     # Store the count of each elements in count array
#     for i in range(0, size):
#         count[array[i]] += 1
#
#     # Store the cummulative count
#     for i in range(1, 10):
#         count[i] += count[i - 1]
#
#     # Find the index of each element of the original array in count array
#     # place the elements in output array
#     i = size - 1
#     while i >= 0:
#         output[count[array[i]] - 1] = array[i]
#         count[array[i]] -= 1
#         i -= 1
#
#     # Copy the sorted elements into original array
#     for i in range(0, size):
#         array[i] = output[i]

def counting_sort(array: list[int]) -> None:
    max_value = max(array)
    count = [0] * (max_value + 1)

    for num in array:
        count[num] += 1



    size = len(count)
    output = [0] * len(array)  # Initialize the output array

    for i in range(1, size):
        count[i] += count[i - 1]

    print(count)
    print(array, "array")

    i = len(array) - 1
    while i >= 0:
        current = count[array[i]] - 1
        print(current, array[i])
        output[current] = array[i]
        count[array[i]] -= 1
        i -= 1
        print(count)

    # i = 0  # Start from the beginning of the array
    # while i < len(array):
    #     current = count[array[i]] - 1
    #     output[current] = array[i]
    #     count[array[i]] -= 1
    #     i += 1

    # Update the original array
    for i in range(0, len(array)):
        array[i] = output[i]


array = [4, 2, 2, 8, 3, 3, 1]

counting_sort(array)
# [1, 2, 2, 3, 3, 4, 8]
print(array)