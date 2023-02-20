# 6. Zigzag Conversion

# Runtime: 103 ms, faster than 20.89% of Python3 online submissions for Zigzag Conversion.

# Memory Usage: 14.7 MB, less than 13.84% of Python3 online submissions for Zigzag Conversion.


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        rows = [[] for _ in range(numRows)]
        # In the first and last rows, the interval between two adjacent elements is the larget.
        largest_interval = (numRows * 2) - 2
        for r in range(numRows):
            i = r

            # In other rows, The sum of the intervals of every three elements is equal to the larget interval.
            curr_interval = largest_interval - 2 * r
            if curr_interval == 0:
                curr_interval = largest_interval

            while i < len(s):
                rows[r].append(s[i])
                i += curr_interval
                if curr_interval != largest_interval:
                    curr_interval = largest_interval - curr_interval

        ans = []
        for row in rows:
            ans.extend(row)
        return "".join(ans)