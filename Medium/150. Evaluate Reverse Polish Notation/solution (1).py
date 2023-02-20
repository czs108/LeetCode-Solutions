# 150. Evaluate Reverse Polish Notation

# Runtime: 68 ms, faster than 70.60% of Python3 online submissions for Evaluate Reverse Polish Notation.

# Memory Usage: 14.6 MB, less than 70.85% of Python3 online submissions for Evaluate Reverse Polish Notation.


class Solution:
    # Stack
    def evalRPN(self, tokens: list[str]) -> int:
        ops = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "/": lambda a, b: int(a / b),
            "*": lambda a, b: a * b
        }

        stack = []
        for token in tokens:
            if token in ops:
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(ops[token](num1, num2))
            else:
                stack.append(int(token))
        return stack.pop()