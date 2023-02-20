# 392. Is Subsequence

# Runtime: 40 ms, faster than 35.28% of Python3 online submissions for Is Subsequence.

# Memory Usage: 25.1 MB, less than 5.03% of Python3 online submissions for Is Subsequence.


class Solution:
    # Divide and Conquer with Greedy
    def isSubsequence(self, s: str, t: str) -> bool:

        def is_subsequence(left, right):
            if left == len(s):
                return True
            elif right == len(t):
                return False

            if s[left] == t[right]:
                left += 1
            right += 1

            return is_subsequence(left, right)

        return is_subsequence(0, 0)