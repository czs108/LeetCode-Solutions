# 28. Implement strStr()

# Runtime: 1124 ms, faster than 5.18% of Python3 online submissions for Implement strStr().

# Memory Usage: 80.6 MB, less than 6.15% of Python3 online submissions for Implement strStr().


class Solution:
    # Knuth-Morris-Pratt - DFA
    def __init__(self):
        Solution.__ascii_num = 256

    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0

        dfa = self.__buildDFA(needle)
        i, j = 0, 0
        n = len(needle)
        # `j` is the number of characters in `needle` that have been matched.
        while i < len(haystack) and j < n:
            j = dfa[ord(haystack[i])][j]
            i += 1
        if j == n:
            return i - n
        else:
            return -1

    def __buildDFA(self, needle: str) -> List[List[int]]:
        assert len(needle) != 0

        n = len(needle)
        dfa = [[0 for i in range(n)] for j in range(Solution.__ascii_num)]
        dfa[ord(needle[0])][0] = 1
        X = 0
        for j in range(1, n):
            # Copy mismatch cases.
            for c in range(Solution.__ascii_num):
                dfa[c][j] = dfa[c][X]
            # Set match case.
            dfa[ord(needle[j])][j] = j + 1
            # Update restart state.
            X = dfa[ord(needle[j])][X]
        return dfa