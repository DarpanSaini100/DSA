from functools import lru_cache
from typing import List

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)

        # suffix[i] = total stones from i to the end
        suffix = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + piles[i]

        @lru_cache(None)
        def dp(i, M):
            # If we can take all remaining piles
            if i >= n:
                return 0

            if i + 2 * M >= n:
                return suffix[i]

            best = 0

            # Try taking x piles
            for x in range(1, 2 * M + 1):
                # Stones current player can ultimately get
                current = suffix[i] - dp(i + x, max(M, x))

                best = max(best, current)

            return best

        return dp(0, 1)