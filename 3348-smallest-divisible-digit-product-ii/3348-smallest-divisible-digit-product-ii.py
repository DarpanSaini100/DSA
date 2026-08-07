from collections import Counter

class Solution:
    def smallestNumber(self, num: str, t: int) -> str:

        FACTOR_COUNTS = {
            0: Counter(),
            1: Counter(),
            2: Counter([2]),
            3: Counter([3]),
            4: Counter([2, 2]),
            5: Counter([5]),
            6: Counter([2, 3]),
            7: Counter([7]),
            8: Counter([2, 2, 2]),
            9: Counter([3, 3]),
        }

        def getPrimeCount(x):
            cnt = Counter({2: 0, 3: 0, 5: 0, 7: 0})
            for p in (2, 3, 5, 7):
                while x % p == 0:
                    cnt[p] += 1
                    x //= p
            return cnt, x == 1

        def getFactorCount(cnt):
            c8 = cnt[2] // 3
            rem2 = cnt[2] % 3

            c9 = cnt[3] // 2
            c3 = cnt[3] % 2

            c4 = rem2 // 2
            c2 = rem2 % 2

            c6 = 0

            if c2 and c3:
                c2 = 0
                c3 = 0
                c6 = 1

            if c3 and c4:
                c2 = 1
                c3 = 0
                c4 = 0
                c6 = 1

            return {
                "2": c2,
                "3": c3,
                "4": c4,
                "5": cnt[5],
                "6": c6,
                "7": cnt[7],
                "8": c8,
                "9": c9,
            }

        primeCount, ok = getPrimeCount(t)
        if not ok:
            return "-1"

        factorCount = getFactorCount(primeCount)

        if sum(factorCount.values()) > len(num):
            ans = ""
            for d in "23456789":
                ans += d * factorCount[d]
            return ans

        primePrefix = Counter()
        for ch in num:
            primePrefix += FACTOR_COUNTS[int(ch)]

        firstZero = len(num)
        for i, ch in enumerate(num):
            if ch == "0":
                firstZero = i
                break

        if firstZero == len(num) and primeCount <= primePrefix:
            return num

        n = len(num)

        for i in range(n - 1, -1, -1):
            d = int(num[i])
            primePrefix -= FACTOR_COUNTS[d]

            remain = n - i - 1

            if i > firstZero:
                continue

            for nd in range(d + 1, 10):
                need = getFactorCount(
                    primeCount - primePrefix - FACTOR_COUNTS[nd]
                )

                needDigits = sum(need.values())

                if needDigits <= remain:
                    ones = remain - needDigits

                    ans = num[:i] + str(nd)
                    ans += "1" * ones

                    for x in "23456789":
                        ans += x * need[x]

                    return ans

        factorCount = getFactorCount(primeCount)

        ans = "1" * (len(num) + 1 - sum(factorCount.values()))
        for x in "23456789":
            ans += x * factorCount[x]

        return ans