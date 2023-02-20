# 752. Open the Lock

# Runtime: 672 ms, faster than 46.66% of Python3 online submissions for Open the Lock.

# Memory Usage: 15.9 MB, less than 20.64% of Python3 online submissions for Open the Lock.


class Solution:
    # Breadth-first Search
    def openLock(self, deadends: list[str], target: str) -> int:

        def neighbors(node: str) -> Iterable[str]:
            for i in range(len(node)):
                x = int(node[i])
                for d in (-1, 1):
                    y = (x + d) % 10
                    yield node[:i] + str(y) + node[i + 1:]

        dead = set(deadends)
        que = [("0000", 0)]
        seen = {"0000"}
        while len(que) > 0:
            node, depth = que.pop(0)
            if node == target:
                return depth
            if node in dead:
                continue
            for nei in neighbors(node):
                if nei not in seen:
                    seen.add(nei)
                    que.append((nei, depth + 1))
        return -1