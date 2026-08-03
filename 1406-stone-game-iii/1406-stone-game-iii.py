class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)

        dp1 = dp2 = dp3 = 0

        for i in range(n - 1, -1, -1):
            best = float('-inf')
            take = 0

            for k in range(3):
                if i + k < n:
                    take += stoneValue[i + k]

                    if k == 0:
                        nxt = dp1
                    elif k == 1:
                        nxt = dp2
                    else:
                        nxt = dp3

                    best = max(best, take - nxt)

            dp3 = dp2
            dp2 = dp1
            dp1 = best

        if dp1 > 0:
            return "Alice"
        elif dp1 < 0:
            return "Bob"
        else:
            return "Tie"