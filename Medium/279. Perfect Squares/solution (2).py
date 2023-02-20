# 279. Perfect Squares

# Runtime: 60 ms, faster than 96.81% of Python3 online submissions for Perfect Squares.

# Memory Usage: 14.7 MB, less than 42.95% of Python3 online submissions for Perfect Squares.


class Solution:
    # Greedy Enumeration
    def numSquares(self, n: int) -> int:
        square_nums = set([i * i for i in range(1, int(n**0.5) + 1)])

        def is_divided_by(n: int, count: int) -> bool:
            '''
            Return `true` if `n` can be decomposed into `count` number of perfect square numbers.
            '''
            if count == 1:
                return n in square_nums

            for k in square_nums:
                if is_divided_by(n - k, count - 1):
                    return True
            return False

        for count in range(1, n + 1):
            if is_divided_by(n, count):
                return count

        assert False