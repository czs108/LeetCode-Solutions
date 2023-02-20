# 567. Permutation in String

# Runtime: 8060 ms, faster than 5.00% of Python3 online submissions for Permutation in String.

# Memory Usage: 14.3 MB, less than 83.42% of Python3 online submissions for Permutation in String.


class Solution:
    _SYM_NUM: int = 26

    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        def char_idx(c: str) -> int:
            return ord(c) - ord('a')

        s1_count = [0 for _ in range(self._SYM_NUM)]
        for c in s1:
            s1_count[char_idx(c)] += 1

        for i in range(len(s2) - len(s1) + 1):
            s2_count = [0 for _ in range(self._SYM_NUM)]
            for j in range(len(s1)):
                s2_count[char_idx(s2[i + j])] += 1
            if s1_count == s2_count:
                return True

        return False