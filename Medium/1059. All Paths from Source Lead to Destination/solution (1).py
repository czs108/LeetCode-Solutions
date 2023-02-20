# 1059. All Paths from Source Lead to Destination


from enum import Enum, auto

class State(Enum):
    # Vertex is not processed yet.
    NOT_PROCESSED = auto()
    # Vertex is being processed.
    PROCESSING = auto()
    # Vertex and all its descendants are processed.
    PROCESSED = auto()


class Solution:
    # Depth-First Search
    def leadsToDestination(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        graph = [[] for _ in range(n)]
        for edge in edges:
            src, dest = edge
            graph[src].append(dest)

        def dfs(node: int, states: list[State]) -> bool:
            if states[node] != State.NOT_PROCESSED:
                return states[node] == State.PROCESSED
            # If this is a leaf node, it should be equal to the destination.
            elif len(graph[node]) == 0:
                return node == destination

            states[node] = State.PROCESSING
            for next in graph[node]:
                if not dfs(next, states):
                    return False
            states[node] = State.PROCESSED
            return True

        return dfs(source, [State.NOT_PROCESSED] * n)