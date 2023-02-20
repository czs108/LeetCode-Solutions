# 38. Count and Say

# Runtime: 32 ms, faster than 75.03% of Python3 online submissions for Count and Say.

# Memory Usage: 13.8 MB, less than 6.38% of Python3 online submissions for Count and Say.


class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"

        res = ""
        prev_res = self.countAndSay(n - 1)
        count = 0
        prev_num = prev_res[0]
        for i in prev_res:
            if i == prev_num:
                count += 1
            else:
                res += f"{count}{prev_num}"
                prev_num = i
                count = 1
        res += f"{count}{prev_num}"
        return res