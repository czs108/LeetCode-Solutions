# 1048. Longest String Chain

# Runtime: 296 ms, faster than 31.71% of Python3 online submissions for Longest String Chain.

# Memory Usage: 16.6 MB, less than 16.13% of Python3 online submissions for Longest String Chain.


class Solution:
    # Top-Down Dynamic Programming
    def longestStrChain(self, words: list[str]) -> int:
        lens = {}
        words = set(words)

        def dfs(s: str) -> int:
            if s in lens:
                return lens[s]

            curr_max_len = 1
            for i in range(len(s)):
                prdcssr = s[:i] + s[i + 1:]
                if prdcssr and prdcssr in words:
                    curr_max_len = max(curr_max_len, dfs(prdcssr) + 1)
            lens[s] = curr_max_len
            return curr_max_len

        max_len = 1
        for s in words:
            max_len = max(max_len, dfs(s))
        return max_len