# 28. Implement strStr()

# Runtime: 1124 ms, faster than 5.18% of Python3 online submissions for Implement strStr().

# Memory Usage: 80.6 MB, less than 6.15% of Python3 online submissions for Implement strStr().


class Solution:
    # Knuth-Morris-Pratt - DFA
    _ASCII_NUM = 256

    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0

        def build_dfa(needle: str) -> list[list[int]]:
            dfa = [[0 for _ in range(len(needle))] for _ in range(self._ASCII_NUM)]
            dfa[ord(needle[0])][0] = 1
            X = 0
            for i in range(1, len(needle)):
                # Copy mismatch cases.
                for c in range(self._ASCII_NUM):
                    dfa[c][i] = dfa[c][X]
                # Set match case.
                dfa[ord(needle[i])][i] = i + 1
                # Update restart state.
                X = dfa[ord(needle[i])][X]
            return dfa

        dfa = build_dfa(needle)
        i, match_len = 0, 0
        # `match_len` is the number of characters in `needle` that have been matched.
        while i < len(haystack) and match_len < len(needle):
            match_len = dfa[ord(haystack[i])][match_len]
            i += 1
        if match_len == len(needle):
            return i - len(needle)
        else:
            return -1