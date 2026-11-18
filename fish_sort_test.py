from fish_sort import get_min_value_index, fish_sort


def test_get_min_value_index_example():
    # Example list: smallest value 2 is first at index 3
    assert get_min_value_index([4, 6, 8, 2, 5, 2, 9]) == 3


def test_get_min_value_index_duplicate_min():
    # Smallest value 1 appears at indexes 1 and 3; the first (1) is returned
    assert get_min_value_index([5, 1, 7, 1, 3]) == 1


def test_get_min_value_index_empty():
    # Empty list returns None
    assert get_min_value_index([]) is None


def test_fish_sort_example():
    # Example list sorted in ascending order
    assert fish_sort([4, 6, 8, 2, 5, 2, 9]) == [2, 2, 4, 5, 6, 8, 9]


def test_fish_sort_non_destructive():
    # The original list must be unchanged after calling fish_sort
    original = [4, 6, 8, 2, 5, 2, 9]
    fish_sort(original)
    assert original == [4, 6, 8, 2, 5, 2, 9]
