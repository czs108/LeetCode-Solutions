# 1249. Minimum Remove to Make Valid Parentheses

# Runtime: 112 ms, faster than 78.49% of Python3 online submissions for Minimum Remove to Make Valid Parentheses.

# Memory Usage: 16 MB, less than 50.69% of Python3 online submissions for Minimum Remove to Make Valid


class Solution:
    # Using a Stack and String Builder
    def minRemoveToMakeValid(self, s: str) -> str:
        if len(s) == 0:
            return True

        ans, stack = set(), []
        for i, c in enumerate(s):
            if c == "(":
                stack.append((c, i))
            elif c == ")":
                if not stack:
                    ans.add(i)
                else:
                    stack.pop()

        for _, i in stack:
            ans.add(i)

        return "".join([s[i] for i in range(len(s)) if i not in ans])