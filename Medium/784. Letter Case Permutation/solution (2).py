# 784. Letter Case Permutation

# Runtime: 91 ms, faster than 19.56% of Python3 online submissions for Letter Case Permutation.

# Memory Usage: 15.6 MB, less than 16.05% of Python3 online submissions for Letter Case Permutation.


class Solution:
    # Iteration
    def letterCasePermutation(self, s: str) -> list[str]:
        ans = [[]]

        for c in s:
            size = len(ans)
            if c.isalpha():
                for i in range(size):
                    ans.append(ans[i][:])
                    ans[i].append(c.lower())
                    ans[i + size].append(c.upper())
            else:
                for i in range(size):
                    ans[i].append(c)
        return ["".join(i) for i in ans]