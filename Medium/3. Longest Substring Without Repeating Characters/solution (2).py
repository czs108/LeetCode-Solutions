# 3. Longest Substring Without Repeating Characters

# Runtime: 60 ms, faster than 74.37% of Python3 online submissions for Longest Substring Without Repeating Characters.

# Memory Usage: 14.4 MB, less than 53.07% of Python3 online submissions for Longest Substring Without Repeating Characters.


class Solution:
    # Two Pointers
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Define a mapping of the characters to its index.
        idx = {}
        max_len = 0
        left = 0
        for right in range(len(s)):
            char = s[right]
            if char in idx:
                # Skip the characters immediately when finding a repeated character.
                left = max(left, idx[char])

            max_len = max(max_len, right - left + 1)
            idx[char] = right + 1

        return max_len