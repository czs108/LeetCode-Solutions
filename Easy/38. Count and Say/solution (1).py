# 38. Count and Say

# Runtime: 32 ms, faster than 75.03% of Python3 online submissions for Count and Say.

# Memory Usage: 13.8 MB, less than 6.38% of Python3 online submissions for Count and Say.


class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"

        result = ""
        prev = self.countAndSay(n - 1)
        count = 0
        c = prev[0]
        for i in prev:
            if i == c:
                count += 1
            else:
                result = result + str(count) + c
                c = i
                count = 1
        result = result + str(count) + c
        return result