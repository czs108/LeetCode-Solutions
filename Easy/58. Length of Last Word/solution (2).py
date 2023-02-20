# 58. Length of Last Word

# Runtime: 32 ms, faster than 21.74% of Python3 online submissions for Length of Last Word.

# Memory Usage: 13.7 MB, less than 5.26% of Python3 online submissions for Length of Last Word.


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(next(reversed(s.split()), ""))