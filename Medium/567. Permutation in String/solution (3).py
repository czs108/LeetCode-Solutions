# 567. Permutation in String

# Runtime: 156 ms, faster than 30.40% of Python3 online submissions for Permutation in String.

# Memory Usage: 14.2 MB, less than 83.45% of Python3 online submissions for Permutation in String.


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
        while right < len(s2):
            c = s2[right]
            right += 1
            s2_count[c] += 1
            if s2_count[c] == s1_count[c]:
                formed += 1

            while right - left >= len(s1):
                if formed == len(s1_count):
                    return True
                else:
                    c = s2[left]
                    if s2_count[c] == s1_count[c]:
                        formed -= 1
                    s2_count[c] -= 1
                    left += 1

        return False