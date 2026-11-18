def get_min_value_index(a_list):
    # Logic (pseudocode):
    # 1. If a_list is empty, return None.
    # 2. Assume the smallest value is at index 0 (min_index = 0).
    # 3. Loop over the indexes 1 to len(a_list) - 1:
    #    - If the value at the current index is STRICTLY smaller than
    #      the value at min_index, update min_index to the current index.
    #    - Using strictly smaller (<, not <=) keeps the FIRST index
    #      when the minimum value appears more than once.
    # 4. Return min_index (the index, not the value).
    # No min(), list.index(), or other banned functions.
    if len(a_list) == 0:
        return None

    min_index = 0
    for i in range(1, len(a_list)):
        if a_list[i] < a_list[min_index]:
            min_index = i

    return min_index


def fish_sort(a_list):
    # Logic (pseudocode):
    # 1. Make a copy of a_list with [:] and use it as the unsorted list,
    #    so the original list never changes (non-destructive).
    # 2. Start with an empty sorted list.
    # 3. While the unsorted list is not empty:
    #    - Use get_min_value_index to find the index of the smallest value.
    #    - Remove that value from the unsorted list with pop(index).
    #    - Append the removed value to the end of the sorted list.
    # 4. Return the sorted list (ascending order).
    # No min(), sorted(), list.sort(), list.index(), or list.remove().
    unsorted = a_list[:]
    sorted_list = []

    while len(unsorted) > 0:
        min_index = get_min_value_index(unsorted)
        smallest = unsorted.pop(min_index)
        sorted_list.append(smallest)

    return sorted_list


def main():
    # Logic (pseudocode):
    # 1. Print the result of the get_min_value_index example.
    # 2. Print the result of the fish_sort example.
    print(get_min_value_index([4, 6, 8, 2, 5, 2, 9]))
    print(fish_sort([4, 6, 8, 2, 5, 2, 9]))


if __name__ == "__main__":
    main()
