# 76. Minimum Window Substring

# Runtime: 128 ms, faster than 38.98% of Python3 online submissions for Minimum Window Substring.

# Memory Usage: 14.9 MB, less than 63.43% of Python3 online submissions for Minimum Window Substring.


from collections import Counter
import math

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        # Dictionary which keeps a count of all the unique characters in t.
        counts = Counter(t)

        # Number of unique characters in t, which need to be present in the desired window.
        required = len(counts)

        # Left and right pointer.
        left, right = 0, 0

        # Keep track of how many unique characters in t are present in the current window in its desired frequency.
        formed = 0

        # Dictionary which keeps a count of all the unique characters in the current window.
        window_counts = Counter()

        win_len, start, end = math.inf, None, None
        while right < len(s):
            # Add one character from the right to the window.
            char = s[right]
            window_counts[char] += 1

            # If the frequency of the current character added equals to the desired count in t then increment the formed count by 1.
            if char in counts and window_counts[char] == counts[char]:
                formed += 1

            # Try and contract the window till the point where it ceases to be 'desirable'.
            while left <= right and formed == required:
                char = s[left]

                # Save the smallest window until now.
                if right - left + 1 < win_len:
                    win_len, start, end = right - left + 1, left, right

                # The character at the position pointed by the `left` pointer is no longer a part of the window.
                window_counts[char] -= 1
                if char in counts and window_counts[char] < counts[char]:
                    formed -= 1

                # Move the left pointer ahead, this would help to look for a new window.
                left += 1

            # Keep expanding the window once we are done contracting.
            right += 1

        return "" if win_len == math.inf else s[start : end + 1]