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
        replaceCost = self.minDistance(word1[:-1], word2[:-1]) + (1 if word1[-1] != word2[-1] else 0)
        removeCost = self.minDistance(word1[:-1], word2) + 1
        insertCost = self.minDistance(word1, word2[:-1]) + 1
        return min(replaceCost, removeCost, insertCost)