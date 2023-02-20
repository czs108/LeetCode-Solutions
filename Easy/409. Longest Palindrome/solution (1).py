# 409. Longest Palindrome

# Runtime: 48 ms, faster than 18.41% of Python3 online submissions for Longest Palindrome.

# Memory Usage: 14.2 MB, less than 80.60% of Python3 online submissions for Longest Palindrome.


from collections import Counter

class Solution:
    # Greedy
    def longestPalindrome(self, s: str) -> int:
        nums = Counter(s)
        ans = 0
        for n in nums.values():
            ans += n // 2 * 2
            if ans % 2 == 0 and n % 2 == 1:
                # Add a unique center.
                ans += 1
        return ans