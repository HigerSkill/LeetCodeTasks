from typing import List


class Solution:
    def _countNegativeInRow(self, arr: List) -> int:
        """Number of negative numbers."""
        l, r = 0, len(arr) - 1

        while l <= r:
            m: int = (l + r) // 2

            if arr[m] < 0:
                r = m - 1
            else:
                l = m + 1

        return len(arr) - l

    def countNegatives(self, grid: List[List[int]]) -> int:
        result: int = 0

        for row in grid:
            result += self._countNegativeInRow(row)

        return result


if __name__ == '__main__':
    s = Solution()

    grid1: List = [[4, 3, 2, -1], [3, 2, 1, -1], [1, 1, -1, -2], [-1, -1, -2, -3]]
    grid2: List = [[3,2],[1,0]]

    print(s.countNegatives(grid2))
    assert 8 == s.countNegatives(grid1)
    assert 0 == s.countNegatives(grid2)


