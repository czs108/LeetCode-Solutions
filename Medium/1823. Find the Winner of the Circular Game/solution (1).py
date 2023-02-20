# 1823. Find the Winner of the Circular Game

# Runtime: 28 ms, faster than 95.81% of Python3 online submissions for Find the Winner of the Circular Game.

# Memory Usage: 14.4 MB, less than 47.35% of Python3 online submissions for Find the Winner of the Circular Game.


class Solution:
    # Simulation
    def findTheWinner(self, n: int, k: int) -> int:
        players = [i for i in range(1, n + 1)]
        start = 0
        while len(players) > 1:
            start = (start + k - 1) % len(players)
            players.pop(start)
        return players[0]