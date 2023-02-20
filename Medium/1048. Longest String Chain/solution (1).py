# 1048. Longest String Chain

# Runtime: 132 ms, faster than 87.64% of Python3 online submissions for Longest String Chain.

# Memory Usage: 14.8 MB, less than 62.22% of Python3 online submissions for Longest String Chain.


class Solution:
    # Top-Down Dynamic Programming
    def longestStrChain(self, words: list[str]) -> int:
        words.sort(key=lambda s: len(s))

        lens = {}
        max_len = 1
        for s in words:
            curr_len = 1
            for i in range(len(s)):
                prdcssr = s[:i] + s[i + 1:]
                if prdcssr and prdcssr in lens:
                    curr_len = max(curr_len, lens[prdcssr] + 1)
            lens[s] = curr_len
            max_len = max(max_len, curr_len)
        return max_len