# 279. Perfect Squares

# Runtime: 168 ms, faster than 91.50% of Python3 online submissions for Perfect Squares.

# Memory Usage: 15.1 MB, less than 33.64% of Python3 online submissions for Perfect Squares.


class Solution:
    # Greedy Tree | Breadth-First Search
    def numSquares(self, n: int) -> int:
        square_nums = [i * i for i in range(1, int(n**0.5) + 1)]
        lvl = 0

        # Use `set` to eliminate the redundancy of remainders within the same level.
        que = {n}
        while que:
            next_que = set()
            lvl += 1
            for remain in que:
                for sq in square_nums:
                    if remain == sq:
                        return lvl
                    elif remain >= sq:
                        next_que.add(remain - sq)
                    else:
                        break
            que = next_que
        assert False