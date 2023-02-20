# 779. K-th Symbol in Grammar

# Memory Limit Exceeded


class Solution:
    def kthGrammar(self, n: int, k: int) -> int:

        def build_next(row: str) -> str:
            if len(row) == 0:
                return ""
            elif row[0] == "0":
                return "01" + build_next(row[1:])
            elif row[0] == "1":
                return "10" + build_next(row[1:])
            else:
                assert False

        s = "0"
        for _ in range(n):
            s = build_next(s)
        return s[k - 1]