def merge_sort(array: list[int]) -> None:
    if len(array) > 1:
        left_arr = array[:len(array) // 2]
        right_arr = array[len(array) // 2:]

        merge_sort(left_arr)
        merge_sort(right_arr)

        i = 0
        j = 0
        k = 0

        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                array[k] = left_arr[i]
                i += 1
            else:
                array[k] = right_arr[j]
                j += 1
            k += 1

        while i < len(left_arr):
            array[k] = left_arr[i]
            i += 1
            k += 1

        while j < len(right_arr):
            array[k] = right_arr[j]
            j += 1
            k += 1

