# 567. Permutation in String

# Runtime: 124 ms, faster than 32.41% of Python3 online submissions for Permutation in String.

# Memory Usage: 14.1 MB, less than 95.54% of Python3 online submissions for Permutation in String.


from collections import Counter

class Solution:
    # Sliding Window
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_count = Counter(s1)

        right, left = 0, 0
        formed = 0
        s2_count = Counter()
        for right in range(len(s2)):
            c = s2[right]
            s2_count[c] += 1
            if s2_count[c] == s1_count[c]:
                formed += 1

            if right - left + 1 > len(s1):
                c = s2[left]
                if s2_count[c] == s1_count[c]:
                    formed -= 1
                s2_count[c] -= 1
                left += 1

            if formed == len(s1_count):
                return True

        return False