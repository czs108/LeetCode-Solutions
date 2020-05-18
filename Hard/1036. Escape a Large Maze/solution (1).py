# 1036. Escape a Large Maze

# Runtime: 916 ms, faster than 56.91% of Python3 online submissions for Escape a Large Maze.

# Memory Usage: 16.1 MB, less than 78.26% of Python3 online submissions for Escape a Large Maze.


from typing import Set, Tuple
import copy
import collections
import queue

class Solution:
    _NEIGHBORS = [(1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)]
    _ACCESSIBLE_NEIGHBORS = [(1, 0), (0, -1), (-1, 0), (0, 1)]
    _ROW_LEN = 10**6
    _COL_LEN = 10**6

    def __init__(self):
        self._blocked = None

    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        if len(blocked) <= 1:
            return True
        else:
            self._blocked = Solution._removeIsolatedBlocks(Solution._convertBlockListToSet(blocked))
            return self._isEscapePossible(tuple(source), tuple(target))\
                    and self._isEscapePossible(tuple(target), tuple(source))

    # Breadth First Search
    def _isEscapePossible(self, source: Tuple[int, int], target: Tuple[int, int]) -> bool:
        max_surround_area = len(self._blocked) * (len(self._blocked) - 1) // 2
        step = 0
        marked = collections.defaultdict(bool)
        que = queue.Queue()
        que.put(source)
        marked[source] = True
        while not que.empty():
            v = que.get()
            step += 1
            if v == target or step > max_surround_area:
                return True
            neighbors = Solution._getAccessibleNeighbors(v)
            for adj in neighbors:
                if (adj not in self._blocked) and (not marked[adj]):
                    que.put(adj)
                    marked[adj] = True
        return False

    @staticmethod
    def _convertBlockListToSet(blocked: List[List[int]]) -> Set[Tuple[int, int]]:
        hash_set = set()
        for v in blocked:
            hash_set.add(tuple(v))
        return hash_set

    @classmethod
    def _removeIsolatedBlocks(cls, blocked: Set[Tuple[int, int]]) -> Set[Tuple[int, int]]:
        res = copy.deepcopy(blocked)
        for v in blocked:
            isolated = True
            neighbors = cls._getNeighbors(v)
            for adj in neighbors:
                if adj in blocked:
                    isolated = False
                    break
            if isolated:
                res.remove(v)
        return res

    @classmethod
    def _getNeighbors(cls, loca: Tuple[int, int]) -> List[Tuple[int, int]]:
        neighbors = []
        for adj in cls._NEIGHBORS:
            neighbor = (loca[0] + adj[0], loca[1] + adj[1])
            if cls._isLocatValid(neighbor):
                neighbors.append(neighbor)
        return neighbors

    @classmethod
    def _getAccessibleNeighbors(cls, loca: Tuple[int, int]) -> List[Tuple[int, int]]:
        neighbors = []
        for adj in cls._ACCESSIBLE_NEIGHBORS:
            neighbor = (loca[0] + adj[0], loca[1] + adj[1])
            if cls._isLocatValid(neighbor):
                neighbors.append(neighbor)
        return neighbors

    @classmethod
    def _isLocatValid(cls, locat: Tuple[int, int]) -> bool:
        valid_row = (0 <= locat[0] and locat[0] < cls._ROW_LEN)
        valid_col = (0 <= locat[1] and locat[1] < cls._COL_LEN)
        return valid_row and valid_col