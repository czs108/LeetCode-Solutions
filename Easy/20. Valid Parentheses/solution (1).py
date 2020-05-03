# 20. Valid Parentheses

# Runtime: 24 ms, faster than 90.39% of Python3 online submissions for Valid Parentheses.

# Memory Usage: 13.7 MB, less than 6.09% of Python3 online submissions for Valid Parentheses.


class Solution:
    def isValid(self, s: str) -> bool:
        left = [ '{', '[', '(' ]
        dict = { '}': '{', ']': '[', ')': '(', }
        stack = []
        for c in s:
            if c in left:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                else:
                    t = stack.pop()
                    if dict[c] != t:
                        return False
        return len(stack) == 0