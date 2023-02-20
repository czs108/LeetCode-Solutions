# 646. Maximum Length of Pair Chain

# Runtime: 3618 ms, faster than 7.25% of Python3 online submissions for Maximum Length of Pair Chain.

# Memory Usage: 15.1 MB, less than 9.68% of Python3 online submissions for Maximum Length of Pair Chain.


class Solution:
    # Dynamic Programming
    def findLongestChain(self, pairs: list[list[int]]) -> int:
        pairs.sort(key=lambda p: p[0])
        counts = [1] * len(pairs)
        for i in range(1, len(pairs)):
            for j in range(i):
                if pairs[j][1] < pairs[i][0]:
                    counts[i] = max(counts[i], counts[j] + 1)
        return max(counts)