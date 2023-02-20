# 520. Detect Capital

# Runtime: 28 ms, faster than 91.10% of Python3 online submissions for Detect Capital.

# Memory Usage: 14.3 MB, less than 13.27% of Python3 online submissions for Detect Capital.


class Solution:
    # Linear Scan
    def detectCapitalUse(self, word: str) -> bool:
        if len(word) == 1:
            return True

        # All capital letters.
        if word[0].isupper() and word[1].isupper():
            for c in word[2:]:
                if c.islower():
                    return False
            return True
        else:
            for c in word[1:]:
                if c.isupper():
                    return False
            return True