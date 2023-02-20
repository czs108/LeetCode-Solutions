# 20. Valid Parentheses

# Runtime: 24 ms, faster than 90.39% of Python3 online submissions for Valid Parentheses.

# Memory Usage: 13.7 MB, less than 6.09% of Python3 online submissions for Valid Parentheses.


class Solution:
    _PARENTHESES_MAP = {")": "(", "}": "{", "]": "["}
    _LEFT_PARENTHESES = ['{', '[', '(']

    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in Solution._LEFT_PARENTHESES:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                else:
                    t = stack.pop()
                    if Solution._PARENTHESES_MAP[c] != t:
                        return False
        return len(stack) == 0