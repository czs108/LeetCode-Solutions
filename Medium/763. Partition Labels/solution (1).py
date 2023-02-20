# 763. Partition Labels

# Runtime: 40 ms, faster than 75.24% of Python3 online submissions for Partition Labels.

# Memory Usage: 14.4 MB, less than 24.03% of Python3 online submissions for Partition Labels.


class Solution:
    # Greedy
    def partitionLabels(self, s: str) -> list[int]:
        last = {c: i for i, c in enumerate(s)}
        j = anchor = 0
        ans = []
        for i, c in enumerate(s):
            j = max(j, last[c])
            if i == j:
                ans.append(i - anchor + 1)
                anchor = i + 1
        return ans