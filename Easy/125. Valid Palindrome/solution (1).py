# 125. Valid Palindrome

# Runtime: 56 ms, faster than 34.66% of Python3 online submissions for Valid Palindrome.

# Memory Usage: 14 MB, less than 52.38% of Python3 online submissions for Valid Palindrome.


class Solution:
    # Two Pointers
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        left, right = 0, len(s) - 1
        while left < right:
            if not s[left].isalnum():
                left += 1
                continue
            elif not s[right].isalnum():
                right -= 1
                continue
            elif s[left] != s[right]:
                return False
            else:
                left += 1
                right -= 1
        return True