# 1244. Design a Leaderboard

# Runtime: 84 ms, faster than 54.73% of Python3 online submissions for Design a Leaderboard.

# Memory Usage: 14.7 MB, less than 60.65% of Python3 online submissions for Design a Leaderboard.


from collections import defaultdict
import heapq

class Leaderboard:
    # Heap
    def __init__(self) -> None:
        self._scores = defaultdict(int)

    def addScore(self, playerId: int, score: int) -> None:
        self._scores[playerId] += score

    def top(self, K: int) -> int:
        heap = []
        for x in self._scores.values():
            heapq.heappush(heap, x)
            if len(heap) > K:
                heapq.heappop(heap)
        return sum(heap)

    def reset(self, playerId: int) -> None:
        self._scores[playerId] = 0

# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)