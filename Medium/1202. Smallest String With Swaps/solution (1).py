# 1202. Smallest String With Swaps


from collections import defaultdict

class Solution:
    # Union Find
    def __init__(self) -> None:
        self._roots: list[int] = None
        self._ranks: list[int] = None

    def smallestStringWithSwaps(self, s: str, pairs: list[list[int]]) -> str:
        self._roots = [-1] * len(s)
        self._ranks = [1] * len(s)
        for i, j in pairs:
            self._union(i, j)

        # If two characters can be swapped, they belong to the same character set.
        # All characters in the same set can be arranged in any order.
        sets = defaultdict(list)
        for i in range(len(self._roots)):
            sets[self._find(i)].append(s[i])

        # Sort characters in each set.
        for root in sets:
            sets[root].sort()

        # For each set, we incrementally arrange the characters it contains.
        res = []
        for i in range(len(self._roots)):
            res.append(sets[self._find(i)].pop(0))
        return "".join(res)


    def _find(self, idx: int) -> int:
        if self._roots[idx] < 0:
            return idx
        else:
            self._roots[idx] = self._find(self._roots[idx])
            return self._roots[idx]

    def _union(self, idx1: int, idx2: int) -> None:
        root1, root2 = self._find(idx1), self._find(idx2)
        if root1 != root2:
            if self._ranks[root1] < self._ranks[root2]:
                self._roots[root1] = root2
            elif self._ranks[root1] > self._ranks[root2]:
                self._roots[root2] = root1
            else:
                self._roots[root1] = root2
                self._ranks[root1] += 1