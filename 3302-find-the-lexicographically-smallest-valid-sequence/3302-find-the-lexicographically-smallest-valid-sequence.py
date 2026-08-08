from typing import List

class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        n = len(word1)
        m = len(word2)

        # exact[i] = earliest position j in word2 such that
        # word2[j:] can be matched exactly in word1[i:]
        exact = [m] * (n + 1)

        # one[i] = earliest position j in word2 such that
        # word2[j:] can be matched with at most 1 mismatch
        one = [m] * (n + 1)

        # Pointers for suffix matching
        e = m
        o = m

        # Build suffix information from right to left
        for i in range(n - 1, -1, -1):

            old_e = e
            old_o = o

            # -------------------------
            # 0 mismatches
            # -------------------------
            if old_e > 0 and word1[i] == word2[old_e - 1]:
                e = old_e - 1

            exact[i] = e

            # -------------------------
            # At most 1 mismatch
            # -------------------------

            best = old_o

            # Option 1: match current character exactly
            if old_o > 0 and word1[i] == word2[old_o - 1]:
                best = min(best, old_o - 1)

            # Option 2: use the one allowed mismatch here
            if old_e > 0:
                best = min(best, old_e - 1)

            o = best
            one[i] = o

        # --------------------------------
        # Greedily build lexicographically
        # smallest index sequence
        # --------------------------------
        ans = []

        prev = -1
        mismatch_used = False

        for j in range(m):

            found = False

            for i in range(prev + 1, n):

                # Case 1:
                # Current character matches.
                # We can still use our mismatch later.
                if word1[i] == word2[j]:

                    if j == m - 1 or one[i + 1] <= j + 1:
                        ans.append(i)
                        prev = i
                        found = True
                        break

                # Case 2:
                # Current character doesn't match.
                # We must use our one mismatch here.
                elif not mismatch_used:

                    if j == m - 1 or exact[i + 1] <= j + 1:
                        ans.append(i)
                        prev = i
                        mismatch_used = True
                        found = True
                        break

            if not found:
                return []

        return ans