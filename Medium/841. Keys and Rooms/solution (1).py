# 841. Keys and Rooms

# Runtime: 64 ms, faster than 84.67% of Python3 online submissions for Keys and Rooms.

# Memory Usage: 15.1 MB, less than 11.68% of Python3 online submissions for Keys and Rooms.


class Solution:
    # Depth-First Search
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        visited = [False] * len(rooms)

        def dfs(id: int) -> None:
            visited[id] = True
            for next in rooms[id]:
                if not visited[next]:
                    dfs(next)

        dfs(0)
        return all(visited)