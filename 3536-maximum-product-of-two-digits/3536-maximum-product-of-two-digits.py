class Solution:
    def maxProduct(self, n: int) -> int:
        digits = [0] * 10

        while n:
            digits[n % 10] += 1
            n //= 10

        for i in range(9, -1, -1):
            if digits[i] >= 2:
                return i * i
            if digits[i]:
                for j in range(i - 1, -1, -1):
                    if digits[j]:
                        return i * j

        return 0