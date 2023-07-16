def binary_search(arr: list, x: int) -> bool:
    l, r = 0, len(arr) - 1

    while l <= r:
        m: int = (l + r) // 2
        if arr[m] == x:
            return True

        if arr[m] < x:
            l = m + 1
        else:
            l = m - 1

    return False


def negative_search(arr: list) -> int:
    """Number of negative numbers."""
    l, r = 0, len(arr) - 1

    while l <= r:
        m: int = (l + r) // 2

        if arr[m] < 0:
            r = m - 1
        else:
            l = m + 1

    return len(arr) - l


if __name__ == '__main__':
    assert True is binary_search([1, 2, 3, 4], 3)
    assert False is binary_search([1, 2, 3, 4], 31)

    assert 5 == negative_search([4, 3, 2, 1, -1, -2, -3, -4, -5])
    assert 3 == negative_search([4, 2, -1, -2, -3])
    assert 2 == negative_search([4, 2, -1, -3])
    assert 0 == negative_search([4, 3, 2, 1])
