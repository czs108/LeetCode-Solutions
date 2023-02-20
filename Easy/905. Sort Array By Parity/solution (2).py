# 905. Sort Array By Parity


class Solution:
    # Two Pass
    # Write all the even elements first, then write all the odd elements.
    def sortArrayByParity(self, A: list[int]) -> list[int]:
        return ([x for x in A if x % 2 == 0] +
                [x for x in A if x % 2 == 1])