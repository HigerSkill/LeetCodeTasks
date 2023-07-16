class Solution:
    def theMaximumAchievableX(self, num: int, t: int) -> int:
        return num + t * 2


if __name__ == '__main__':
    s = Solution()

    assert 7 == s.theMaximumAchievableX(3, 2)
    assert 6 == s.theMaximumAchievableX(4, 1)
