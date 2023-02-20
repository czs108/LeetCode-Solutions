# 394. Decode String

# Runtime: 24 ms, faster than 95.62% of Python3 online submissions for Decode String.

# Memory Usage: 14.4 MB, less than 19.69% of Python3 online submissions for Decode String.


class Solution:
    # Stack
    def decodeString(self, s: str) -> str:
        nums, bufs = [], [[]]
        num = 0
        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c == "[":
                nums.append(num)
                num = 0
                bufs.append([])
            elif c.isalpha():
                bufs[-1].append(c)
            elif c == "]":
                bufs[-1].extend(bufs.pop(-1) * nums.pop(-1))
        return "".join(bufs[-1])