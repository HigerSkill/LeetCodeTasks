class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product: int = 1
        sums: int = 0

        for _ in range(len(str(n))):
            product *= n % 10
            sums += n % 10

            n //= 10

        return product - sums


if __name__ == '__main__':
    s = Solution()

    assert 15 == s.subtractProductAndSum(234)
    assert 21 == s.subtractProductAndSum(4421)