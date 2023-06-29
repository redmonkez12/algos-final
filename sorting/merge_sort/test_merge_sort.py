from merge_sort import merge_sort


def test_merge_sort():
    array = [55, -2, 33, 1, 202, 78, 4, 67, 15]
    merge_sort(array)

    assert array == [-2, 1, 4, 15, 33, 55, 67, 78, 202]
