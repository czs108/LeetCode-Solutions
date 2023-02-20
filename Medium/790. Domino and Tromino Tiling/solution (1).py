# 790. Domino and Tromino Tiling

# Runtime: 32 ms, faster than 83.59% of Python3 online submissions for Domino and Tromino Tiling.

# Memory Usage: 14.2 MB, less than 70.51% of Python3 online submissions for Domino and Tromino Tiling.


class Solution:
    # Dynamic Programming
    def numTilings(self, n: int) -> int:
        MOD = 10**9 + 7

        if n <= 2:
            return n

        # Fully covered board: All tiles on board are covered by a domino or a tromino.
        # Partially covered board: Same as a fully covered board, except leave the tile in the upper-right corner uncovered.

        # f(k): The number of ways to fully cover a board of width k.
        f = [0] * (n + 1)

        # p(k): The number of ways to partially cover a board of width k.
        p = [0] * (n + 1)

        f[1], f[2] = 1, 2
        p[2] = 1

        for k in range(3, n + 1):
            # To get f(k):
            # From f(k-1), we can add 1 vertical domino for each tiling in a fully covered board with a width of k-1.
            # From f(k-2), we can add 2 horizontal dominos for each tiling in a fully covered board with a width of k-2.
            # From p(k-1), we can add an L-shaped tromino for each tiling in a partially covered board with a width of k-1.
            # We multiply by p(k-1) by 2 because for any partially covered tiling, there will be a horizontally symmetrical tiling of it.
            f[k] = (f[k - 1] + f[k - 2] + 2 * p[k - 1]) % MOD

            # To get p(k):
            # From f(k-2), we can add a tromino to a fully covered board of width k-2.
            # From p(k-1), we can add a horizontal domino to a partially covered board of width k-1.
            p[k] = (p[k - 1] + f[k - 2]) % MOD
        return f[n]