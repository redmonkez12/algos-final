from insertion_sort import insertion_sort


def test_insertion_sort():
    array = [55, -2, 33, 1, 202, 78, 4, 67, 15]
    insertion_sort(array)

    assert array == [-2, 1, 4, 15, 33, 55, 67, 78, 202]
