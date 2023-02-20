# 1046. Last Stone Weight


class Solution:
    # Array-Based Simulation
    def lastStoneWeight(self, stones: list[int]) -> int:

        def remove_largest() -> int:
            idx = stones.index(max(stones))
            stones[-1], stones[idx] = stones[idx], stones[-1]
            return stones.pop()

        while len(stones) > 1:
            stone1, stone2 = remove_largest(), remove_largest()
            if stone1 != stone2:
                stones.append(stone1 - stone2)
        return stones[0] if stones else 0