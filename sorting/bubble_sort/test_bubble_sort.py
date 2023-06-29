from bubble_sort import bubble_sort


def test_bubble_sort():
    array = [55, -2, 33, 1, 202, 78, 4, 67, 15]
    bubble_sort(array)

    assert array == [-2, 1, 4, 15, 33, 55, 67, 78, 202]
