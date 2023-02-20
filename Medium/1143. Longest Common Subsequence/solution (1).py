# 1143. Longest Common Subsequence

# Time Limit Exceeded


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) == 0 or len(text2) == 0:
            return 0

        opt1 = self.longestCommonSubsequence(text1[1:], text2)

        opt2 = 0
        first_idx = text2.find(text1[0])
        if first_idx >= 0:
            opt2 = 1 + self.longestCommonSubsequence(text1[1:], text2[first_idx + 1:])

        return max(opt1, opt2)