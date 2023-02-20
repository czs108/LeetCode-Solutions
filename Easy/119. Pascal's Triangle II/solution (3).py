# 119. Pascal's Triangle II

# Runtime: 32 ms, faster than 65.22% of Python3 online submissions for Pascal's Triangle II.

# Memory Usage: 14.2 MB, less than 77.90% of Python3 online submissions for Pascal's Triangle II.


class Solution:
    # Recursion
    def getRow(self, rowIndex: int) -> list[int]:
        if rowIndex == 0:
            return [1]
        else:
            prev = [0] + self.getRow(rowIndex - 1) + [0]
            curr = []
            for i in range(rowIndex + 1):
                curr.append(prev[i] + prev[i + 1])
            return curr