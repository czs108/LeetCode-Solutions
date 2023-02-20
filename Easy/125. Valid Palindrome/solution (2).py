# 125. Valid Palindrome

# Runtime: 56 ms, faster than 58.66% of Python3 online submissions for Valid Palindrome.

# Memory Usage: 14 MB, less than 25.38% of Python3 online submissions for Valid Palindrome.


class Solution:
    # Compare with Reverse
    def isPalindrome(self, s: str) -> bool:
        filtered_chars = filter(lambda c: c.isalnum(), s)
        lowercase_filtered_chars = map(lambda c: c.lower(), filtered_chars)

        filtered_chars_list = list(lowercase_filtered_chars)
        reversed_chars_list = filtered_chars_list[::-1]
        return filtered_chars_list == reversed_chars_list