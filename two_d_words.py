def two_d_words(word_list):
    # Logic (pseudocode):
    # 1. Go through every word in word_list.
    # 2. Keep the word only if its length is even (len(word) % 2 == 0).
    # 3. For each kept word, build a row: a list of its letters,
    #    one letter per column (inner list comprehension over the word).
    # 4. Collect all rows into one outer list -> the 2D list.
    # 5. An empty word_list (or no even-length words) gives [].
    return [[letter for letter in word] for word in word_list if len(word) % 2 == 0]


def main():
    # Logic (pseudocode):
    # 1. Check the example from the assignment with assert.
    # 2. Check my own cases: empty list, no qualifying words,
    #    and a mix including a single even word.
    # 3. Print a message if all asserts pass.

    # Example from the assignment
    assert two_d_words(["liberal", "normal", "framework", "file",
                        "encounter", "mature", "illustrate"]) == [
        ['n', 'o', 'r', 'm', 'a', 'l'],
        ['f', 'i', 'l', 'e'],
        ['m', 'a', 't', 'u', 'r', 'e'],
        ['i', 'l', 'l', 'u', 's', 't', 'r', 'a', 't', 'e']]

    # My own cases
    # Empty list returns []
    assert two_d_words([]) == []

    # No word qualifies (all odd lengths) returns []
    assert two_d_words(["cat", "apple", "a"]) == []

    # Mixed list: only the even-length words are kept, in order
    assert two_d_words(["hi", "dog", "code"]) == [['h', 'i'],
                                                   ['c', 'o', 'd', 'e']]

    print("All two_d_words tests passed!")


if __name__ == "__main__":
    main()
