# 14. Longest Common Prefix

# Runtime: 36 ms, faster than 34.93% of Python3 online submissions for Longest Common Prefix.

# Memory Usage: 14.1 MB, less than 6.67% of Python3 online submissions for Longest Common Prefix.


class Solution:
    # Vertical scanning
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if len(strs) == 0:
            return ""

        first = strs[0]
        for i in range(len(first)):
            c = first[i]
            for j in range(1, len(strs)):
                if i == len(strs[j]) or strs[j][i] != c:
                    return first[:i]
        return first