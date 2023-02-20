# 557. Reverse Words in a String III

# Runtime: 132 ms, faster than 5.15% of Python3 online submissions for Reverse Words in a String III.

# Memory Usage: 15 MB, less than 45.18% of Python3 online submissions for Reverse Words in a String III.


class Solution:
    def reverseWords(self, s: str) -> str:

        def reverse(start: int, end: int) -> list[str]:
            res = []
            while end >= start:
                 res.append(s[end])
                 end -= 1
            return res

        res = []
        head = None
        for i in range(len(s)):
            if head is None:
                head = i
            if i == len(s) - 1:
                res.extend(reverse(head, i))
            elif s[i] == " ":
                res.extend(reverse(head, i - 1) + [" "])
                head = None
        return "".join(res)