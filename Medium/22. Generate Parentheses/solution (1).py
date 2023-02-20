# 22. Generate Parentheses

# Runtime: 36 ms, faster than 70.81% of Python3 online submissions for Generate Parentheses.

# Memory Usage: 14.3 MB, less than 96.52% of Python3 online submissions for Generate Parentheses.


class Solution:
    # Backtracking
    def generateParenthesis(self, n: int) -> list[str]:
        ans = []

        def backtrack(left: int, right: int, prnth: list[str]) -> None:
            if len(prnth) == n * 2:
                ans.append("".join(prnth))
            else:
                if left < n:
                    prnth.append("(")
                    backtrack(left + 1, right, prnth)
                    prnth.pop()
                if right < left:
                    prnth.append(")")
                    backtrack(left, right + 1, prnth)
                    prnth.pop()

        backtrack(0, 0, [])
        return ans