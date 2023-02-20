# 1337. The K Weakest Rows in a Matrix


from collections import defaultdict

class Solution:
    # Linear Search and Map
    def kWeakestRows(self, mat: list[list[int]], k: int) -> list[int]:
        strengths = defaultdict(list)
        for i, row in enumerate(mat):
            strengths[sum(row)].append(i)

        sorted_strengths = sorted(list(strengths.keys()))

        idxes = []
        for strength in sorted_strengths:
            for idx in strengths[strength]:
                if len(idxes) == k:
                    break
                else:
                    idxes.append(idx)
        return idxes