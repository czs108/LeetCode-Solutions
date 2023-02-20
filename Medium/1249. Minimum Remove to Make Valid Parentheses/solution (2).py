# 1249. Minimum Remove to Make Valid Parentheses

# Runtime: 132 ms, faster than 57.45% of Python3 online submissions for Minimum Remove to Make Valid Parentheses.

# Memory Usage: 16.5 MB, less than 19.31% of Python3 online submissions for Minimum Remove to Make Valid


class Solution:
    # Two Pass String Builder
    def minRemoveToMakeValid(self, s: str) -> str:

        def delete_invalid_closing(s: str, open_sym: str, close_sym: str) -> str:
            sb = []
            balance = 0
            for c in s:
                if c == open_sym:
                    balance += 1
                elif c == close_sym:
                    if balance == 0:
                        continue
                    else:
                        balance -= 1
                sb.append(c)
            return "".join(sb)

        s = delete_invalid_closing(s, "(", ")")
        s = delete_invalid_closing(s[::-1], ")", "(")
        return s[::-1]