# 3. Longest Substring Without Repeating Characters

# Runtime: 84 ms, faster than 34.28% of Python3 online submissions for Longest Substring Without Repeating Characters.

# Memory Usage: 14.4 MB, less than 24.10% of Python3 online submissions for Longest Substring Without Repeating Characters.


from collections import Counter

class Solution:
    # Two Pointers
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        max_len = 0
        counts = Counter()
        for right in range(len(s)):
            r = s[right]
            counts[r] += 1

            while counts[r] > 1:
                l = s[left]
                counts[l] -= 1
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len