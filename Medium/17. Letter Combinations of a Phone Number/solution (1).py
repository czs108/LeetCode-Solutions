# 17. Letter Combinations of a Phone Number

# Runtime: 32 ms, faster than 72.52% of Python3 online submissions for Letter Combinations of a Phone Number.

# Memory Usage: 14.2 MB, less than 62.44% of Python3 online submissions for Letter Combinations of a Phone Number.


class Solution:
    # Backtracking
    def letterCombinations(self, digits: str) -> list[str]:
        if len(digits) == 0:
            return []

        letters = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
                   "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        res = []

        def backtrack(start: int, comb: list[str]) -> None:
            if start == len(digits):
                res.append("".join(comb))
            else:
                for next in letters[digits[start]]:
                    comb.append(next)
                    backtrack(start + 1, comb)
                    comb.pop()

        backtrack(0, [])
        return res