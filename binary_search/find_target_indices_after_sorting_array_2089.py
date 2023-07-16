from typing import List


class Solution:
    def sort(self, nums: List[int]) -> List[int]:
        d: int = len(str(max(nums)))

        buckets: List[List[int]] = [[] for _ in range(10)]

        p_ten = 1
        for p in range(d):
            for el in nums:
                buckets[el // p_ten % 10].append(el)

            nums = [x for b in buckets for x in b]
            buckets = [[] for _ in range(10)]

            p_ten *= 10

        return nums

    def binary_search(self, nums: List[int], x: int) -> List[int]:
        l, r = 0, len(nums)-1
        ind: int = -1
        result: List[int] = []

        while l <= r:
            m: int = (l + r) // 2

            if nums[m] == x:
                ind = m
                break

            if nums[m] < x:
                l = m + 1
            else:
                r = m - 1

        i = ind
        while i >= 0 and nums[i] == x:
            result.append(i)
            i -= 1

        i = ind + 1
        while i < len(nums) and nums[i] == x:
            result.append(i)
            i += 1

        return result

    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        # Just for fun
        # It can work with O(n), without binary search and sort
        result: List[int] = self.binary_search(self.sort(nums), target)
        result = self.sort(result) if result else result
        return result


if __name__ == '__main__':
    s = Solution()

    arr: List[int] = [100, 1, 100]
    assert [1, 2] == s.targetIndices(arr, 100)
    arr: List[int] = [1]
    assert [] == s.targetIndices(arr, 2)
    arr: List[int] = [1]
    assert [0] == s.targetIndices(arr, 1)
    arr: List[int] = [1, 2, 5, 2, 3]
    assert [1, 2] == s.targetIndices(arr, 2)
