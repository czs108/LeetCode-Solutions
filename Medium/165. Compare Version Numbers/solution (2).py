# 165. Compare Version Numbers

# Runtime: 32 ms, faster than 63.01% of Python3 online submissions for Compare Version Numbers.

# Memory Usage: 14.3 MB, less than 61.51% of Python3 online submissions for Compare Version Numbers.


class Solution:
    # Two Pointers | One Pass
    def compareVersion(self, version1: str, version2: str) -> int:

        def get_next_chunk(version: str, start: int) -> tuple[int, int]:
            if start >= len(version):
                return 0, start
            else:
                end = start
                while end < len(version) and version[end] != ".":
                    end += 1
                return int(version[start:end]), end + 1

        p1, p2 = 0, 0
        while p1 < len(version1) or p2 < len(version2):
            num1, p1 = get_next_chunk(version1, p1)
            num2, p2 = get_next_chunk(version2, p2)
            if num1 != num2:
                return 1 if num1 > num2 else -1
        return 0