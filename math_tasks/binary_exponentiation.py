def exp1(a: int, n: int) -> int:
    """Binary exponentiation v1.

    Time complexity O(logN)
    """
    if n == 0:
        return 1

    if n % 2 == 1:
        return exp1(a, n - 1) * a

    e: int = exp1(a, n // 2)

    return e * e


def exp2(a: int, n: int) -> int:
    """Binary exponentiation v2.

    Time complexity O(logN)
    """
    result: int = 1

    while n != 0:
        if n & 1:
            result *= a

        n >>= 1
        a *= a

    return result


if __name__ == '__main__':
    assert 2**10 == exp1(2, 10)
    assert 175**23 == exp1(175, 23)

    assert 2**10 == exp2(2, 10)
    assert 175**23 == exp2(175, 23)
