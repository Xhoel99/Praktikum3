def dc_power(base, exponent):
    # Logic (pseudocode):
    # 1. If exponent < 0, return None.
    # 2. If exponent == 0, return 1.
    # 3. If exponent == 1, return base.
    # 4. Otherwise, recursively compute half = P(base, exponent // 2).
    #    (Computed once and reused, since P(B, E // 2) appears twice
    #    in the formula and both calls give the same value.)
    # 5. If exponent is odd, return base * half * half.
    # 6. If exponent is even, return half * half.
    # No loops, no ** operator, no pow(), no math import.
    if exponent < 0:
        return None
    elif exponent == 0:
        return 1
    elif exponent == 1:
        return base

    half = dc_power(base, exponent // 2)

    if exponent % 2 == 1:
        return base * half * half
    else:
        return half * half


def main():
    # Logic (pseudocode):
    # 1. Assert every case from the assignment's table.
    # 2. Assert my own cases: base 2, base 0, negative base
    #    with odd and even exponents.
    # 3. Print a message if all asserts pass.

    # Cases from the assignment's table
    assert dc_power(999, -1) is None
    assert dc_power(10000, 0) == 1
    assert dc_power(42, 1) == 42
    assert dc_power(3, 10) == 59049
    assert dc_power(8, 7) == 2097152

    # My own cases
    assert dc_power(2, 10) == 1024
    assert dc_power(0, 5) == 0
    assert dc_power(-2, 3) == -8
    assert dc_power(-2, 4) == 16

    print("All dc_power tests passed!")


if __name__ == "__main__":
    main()
