# 72. Edit Distance

# 23 / 1146 test cases passed.
# Status: Time Limit Exceeded


class Solution:
    # Recursive
    def minDistance(self, word1: str, word2: str) -> int:
        if len(word1) == 0:
            return len(word2)
        elif len(word2) == 0:
            return len(word1)

        # Convert `word1` to `word2`.
        replace = self.minDistance(word1[:-1], word2[:-1]) + (1 if word1[-1] != word2[-1] else 0)
        remove = self.minDistance(word1[:-1], word2) + 1
        insert = self.minDistance(word1, word2[:-1]) + 1
        return min(replace, remove, insert)