# 14. Longest Common Prefix

# Runtime: 28 ms, faster than 88.38% of Python3 online submissions for Longest Common Prefix.

# Memory Usage: 14 MB, less than 6.67% of Python3 online submissions for Longest Common Prefix.


class Solution:
    # Horizontal scanning
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if len(strs) == 0:
            return ""

        # LCP(LCP(LCP(S1, S2), S3), ... Sn)
        prefix = strs[0]
        for i in range(1, len(strs)):
            while strs[i].find(prefix) != 0:
                prefix = prefix[:-1]
                if len(prefix) == 0:
                    return ""
        return prefix