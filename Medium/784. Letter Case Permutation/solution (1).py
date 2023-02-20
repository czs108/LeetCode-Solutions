# 784. Letter Case Permutation

# Runtime: 98 ms, faster than 16.21% of Python3 online submissions for Letter Case Permutation.

# Memory Usage: 15.5 MB, less than 27.62% of Python3 online submissions for Letter Case Permutation.


class Solution:
    # Recursion
    def letterCasePermutation(self, s: str) -> list[str]:
        ans = []

        def select(curr: str, i: int) -> None:
            if i == len(s):
                ans.append(curr)
            elif s[i].isalpha():
                select(curr + s[i].lower(), i + 1)
                select(curr + s[i].upper(), i + 1)
            else:
                select(curr + s[i], i + 1)

        select("", 0)
        return ans