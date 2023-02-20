# 12. Integer to Roman

# Runtime: 56 ms, faster than 40.29% of Python3 online submissions for Integer to Roman.

# Memory Usage: 13.8 MB, less than 6.15% of Python3 online submissions for Integer to Roman.


class Solution:
    def intToRoman(self, num: int) -> str:
        map = {1000: "M",
                900: "CM",
                500: "D",
                400: "CD",
                100: "C",
                90: "XC",
                50: "L",
                40: "XL",
                10: "X",
                9: "IX",
                5: "V",
                4: "IV",
                1: "I"}

        ret = ""
        remainder = num
        for k, sym in map.items():
            quotient, remainder = divmod(remainder, k)
            ret += sym * quotient
        return ret