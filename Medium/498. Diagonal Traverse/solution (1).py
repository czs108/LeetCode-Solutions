# 498. Diagonal Traverse

# Runtime: 197 ms, faster than 54.97% of Python3 online submissions for Diagonal Traverse.

# Memory Usage: 16.6 MB, less than 95.61% of Python3 online submissions for Diagonal Traverse.


class Solution:
    def findDiagonalOrder(self, mat: list[list[int]]) -> list[int]:
        if not mat:
            return []

        row, col = len(mat), len(mat[0])

        ans = []
        curr = []
        reverse = False

        # From top-left to bottom-left.
        for i in range(row):
            r, c = i, 0
            # Get diagonal elements.
            while r >= 0 and c < col:
                curr.append(mat[r][c])
                r -= 1
                c += 1
            if reverse:
                ans.extend(reversed(curr))
            else:
                ans.extend(curr)
            reverse = not reverse
            curr = []

        # From bottom-left to bottom-right.
        for i in range(1, col):
            r, c = row - 1, i
            # Get diagonal elements.
            while r >= 0 and c < col:
                curr.append(mat[r][c])
                r -= 1
                c += 1
            if reverse:
                ans.extend(reversed(curr))
            else:
                ans.extend(curr)
            reverse = not reverse
            curr = []

        return ans