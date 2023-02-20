# 779. K-th Symbol in Grammar

# Runtime: 28 ms, faster than 83.78% of Python3 online submissions for K-th Symbol in Grammar.

# Memory Usage: 14.2 MB, less than 78.55% of Python3 online submissions for K-th Symbol in Grammar.


class Solution:
    #               0
    #        /             \
    #       0               1
    #    /     \         /     \
    #   0       1       1       0
    #  / \     / \     / \     / \
    # 0   1   1   0   1   0   0   1
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        elif k % 2 == 0:
            return 0 if self.kthGrammar(n - 1, k // 2) == 1 else 1
        else:
            return self.kthGrammar(n - 1, (k + 1) // 2)