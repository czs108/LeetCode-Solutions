# 1036. Escape a Large Maze

# Runtime: 916 ms, faster than 56.91% of Python3 online submissions for Escape a Large Maze.

# Memory Usage: 16.1 MB, less than 78.26% of Python3 online submissions for Escape a Large Maze.


import copy
from collections import defaultdict
from queue import Queue

class Solution:
    _NEIGHBORS = [(1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)]
    _ACCESSIBLE_NEIGHBORS = [(1, 0), (0, -1), (-1, 0), (0, 1)]
    _ROW_LEN = 10**6
    _COL_LEN = 10**6

    def __init__(self):
        self._blocked = None

    def isEscapePossible(self, blocked: list[list[int]], source: list[int], target: list[int]) -> bool:
        if len(blocked) <= 1:
            return True
        else:
            self._blocked = self._remove_isolated_blocks(self._convert_blocklist_to_set(blocked))
            return self._is_escape_possible(tuple(source), tuple(target))\
                    and self._is_escape_possible(tuple(target), tuple(source))

    # Breadth First Search
    def _is_escape_possible(self, source: tuple[int, int], target: tuple[int, int]) -> bool:
        max_surround_area = len(self._blocked) * (len(self._blocked) - 1) // 2
        step = 0
        marked = defaultdict(bool)
        que = Queue()
        que.put(source)
        marked[source] = True
        while not que.empty():
            v = que.get()
            step += 1
            if v == target or step > max_surround_area:
                return True
            neighbors = self._get_accessible_neighbors(v)
            for adj in neighbors:
                if (adj not in self._blocked) and (not marked[adj]):
                    que.put(adj)
                    marked[adj] = True
        return False

    def _convert_blocklist_to_set(self, blocked: list[list[int]]) -> set[tuple[int, int]]:
        hash_set = set()
        for v in blocked:
            hash_set.add(tuple(v))
        return hash_set

    def _remove_isolated_blocks(self, blocked: set[tuple[int, int]]) -> set[tuple[int, int]]:
        res = copy.deepcopy(blocked)
        for v in blocked:
            isolated = True
            neighbors = self._get_neighbors(v)
            for adj in neighbors:
                if adj in blocked:
                    isolated = False
                    break
            if isolated:
                res.remove(v)
        return res

    def _get_neighbors(self, loc: tuple[int, int]) -> list[tuple[int, int]]:
        neighbors = []
        for adj in self._NEIGHBORS:
            neighbor = (loc[0] + adj[0], loc[1] + adj[1])
            if self._is_location_valid(neighbor):
                neighbors.append(neighbor)
        return neighbors

    def _get_accessible_neighbors(self, loc: tuple[int, int]) -> list[tuple[int, int]]:
        neighbors = []
        for adj in self._ACCESSIBLE_NEIGHBORS:
            neighbor = (loc[0] + adj[0], loc[1] + adj[1])
            if self._is_location_valid(neighbor):
                neighbors.append(neighbor)
        return neighbors

    def _is_location_valid(self, loc: tuple[int, int]) -> bool:
        valid_row = (0 <= loc[0] and loc[0] < self._ROW_LEN)
        valid_col = (0 <= loc[1] and loc[1] < self._COL_LEN)
        return valid_row and valid_col