# 567. Permutation in String

# Runtime: 108 ms, faster than 33.88% of Python3 online submissions for Permutation in String.

# Memory Usage: 14.6 MB, less than 7.74% of Python3 online submissions for Permutation in String.


class Solution:
    _SYM_NUM: int = 26

    # Sliding Window
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        def char_idx(c: str) -> int:
            return ord(c) - ord('a')

        s1_count = [0 for _ in range(self._SYM_NUM)]
        s2_count = [0 for _ in range(self._SYM_NUM)]
        for i in range(len(s1)):
            s1_count[char_idx(s1[i])] += 1
            s2_count[char_idx(s2[i])] += 1

        for i in range(len(s2) - len(s1)):
            if s1_count == s2_count:
                return True
            else:
                s2_count[char_idx(s2[i + len(s1)])] += 1
                s2_count[char_idx(s2[i])] -= 1

        return s1_count == s2_count