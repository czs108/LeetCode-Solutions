# 20. Valid Parentheses

# Runtime: 28 ms, faster than 72.64% of Python3 online submissions for Valid Parentheses.

# Memory Usage: 13.9 MB, less than 5.22% of Python3 online submissions for Valid Parentheses.


class Solution:
    # Hash map for keeping track of mappings. This keeps the code very clean.
    # Also makes adding more types of parenthesis easier
    _PARENTHESES_MAP = {")": "(", "}": "{", "]": "["}

    def isValid(self, s: str) -> bool:
        # The stack to keep track of opening brackets.
        stack = []

        # For every bracket in the expression.
        for char in s:

            # If the character is an closing bracket
            if char in Solution._PARENTHESES_MAP:

                # Pop the topmost element from the stack, if it is non empty
                # Otherwise assign a dummy value of '#' to the top_element variable
                top_element = stack.pop() if stack else '#'

                # The mapping for the opening bracket in our hash and the top
                # element of the stack don't match, return False
                if Solution._PARENTHESES_MAP[char] != top_element:
                    return False
            else:
                # We have an opening bracket, simply push it onto the stack.
                stack.append(char)

        # In the end, if the stack is empty, then we have a valid expression.
        # The stack won't be empty for cases like ((()
        return not stack