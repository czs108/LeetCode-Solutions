# 1168. Optimize Water Distribution in a Village


from collections import defaultdict
import heapq

class Solution:
    # Prim's Algorithm with Heap | Greedy
    #
    # Building the tree one vertex at a time, from an arbitrary starting vertex,
    # at each step adding the cheapest possible connection from any vertex in the tree to a vertex that is not in the tree.
    def minCostToSupplyWater(self, n: int, wells: list[int], pipes: list[list[int]]) -> int:
        # Bidirectional graph represented in adjacency list.
        graph = defaultdict(list)

        # Add a virtual vertex indexed with 0,
        # then add an edge to each of the house weighted by the cost.
        for idx, cost in enumerate(wells):
            graph[0].append((cost, idx + 1))

        # Add the bidirectional edges to the graph.
        for a, b, cost in pipes:
            graph[a].append((cost, b))
            graph[b].append((cost, a))

        # A set to maintain all the vertex that has been added to the final minimum spanning tree,
        # starting from the vertex 0.
        mst_set = set([0])

        # A heap to maitain the order of edges to be visited,
        # starting from the edges originated from the vertex 0.
        heapq.heapify(graph[0])
        edges_heap = graph[0]

        total_cost = 0
        while len(mst_set) < n + 1:
            cost, next = heapq.heappop(edges_heap)
            if next in mst_set:
                continue

            # Add the new vertex into the set.
            mst_set.add(next)
            total_cost += cost
            # Expand the candidates of edge to choose from in the next round.
            for new_cost, neighbor in graph[next]:
                if neighbor not in mst_set:
                    heapq.heappush(edges_heap, (new_cost, neighbor))

        return total_cost