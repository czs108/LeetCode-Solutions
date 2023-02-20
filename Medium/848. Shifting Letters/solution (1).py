# 848. Shifting Letters

# Runtime: 1499 ms, faster than 9.37% of Python3 online submissions for Shifting Letters.

# Memory Usage: 27.3 MB, less than 55.56% of Python3 online submissions for Shifting Letters.


class Solution:
    def shiftingLetters(self, s: str, shifts: list[int]) -> str:
        for i in range(len(shifts) - 2, -1, -1):
            shifts[i] += shifts[i + 1]

        ans = []
        for i in range(len(shifts)):
            index = ord(s[i]) - ord('a')
            ans.append(chr(ord('a') + (index + shifts[i]) % 26))
        return "".join(ans)