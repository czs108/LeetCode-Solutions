# 28. Implement strStr()

# Runtime: 1124 ms, faster than 5.18% of Python3 online submissions for Implement strStr().

# Memory Usage: 80.6 MB, less than 6.15% of Python3 online submissions for Implement strStr().


class Solution:
    # Knuth-Morris-Pratt - DFA
    _ASCII_NUM = 256

    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0

        dfa = Solution._buildDFA(needle)
        i, j = 0, 0
        # `j` is the number of characters in `needle` that have been matched.
        while i < len(haystack) and j < len(needle):
            j = dfa[ord(haystack[i])][j]
            i += 1
        if j == len(needle):
            return i - len(needle)
        else:
            return -1

    @classmethod
    def _buildDFA(needle: str) -> List[List[int]]:
        dfa = [[0 for _ in range(len(needle))] for _ in range(cls._ASCII_NUM)]
        dfa[ord(needle[0])][0] = 1
        X = 0
        for j in range(1, len(needle)):
            # Copy mismatch cases.
            for c in range(cls._ASCII_NUM):
                dfa[c][j] = dfa[c][X]
            # Set match case.
            dfa[ord(needle[j])][j] = j + 1
            # Update restart state.
            X = dfa[ord(needle[j])][X]
        return dfa