# 58. Length of Last Word

# Runtime: 32 ms, faster than 21.74% of Python3 online submissions for Length of Last Word.

# Memory Usage: 13.9 MB, less than 5.26% of Python3 online submissions for Length of Last Word.


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if not s:
            return 0

        last_word_len = 0
        blank = False
        for c in s:
            if c != ' ':
                if blank:
                    # Get a new word
                    last_word_len = 0
                    blank = False
                last_word_len += 1
            else:
                blank = True
        return last_word_len