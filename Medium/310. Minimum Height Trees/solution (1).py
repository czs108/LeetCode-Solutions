# 310. Minimum Height Trees

# Runtime: 232 ms, faster than 79.45% of Python3 online submissions for Minimum Height Trees.

# Memory Usage: 18.9 MB, less than 46.34% of Python3 online submissions for Minimum Height Trees.


class Solution:
    # Topological Sorting
    def findMinHeightTrees(self, n: int, edges: list[list[int]]) -> list[int]:
        if n <= 2:
            return [i for i in range(n)]

        # Build the graph with the adjacency list.
        neighbors = [set() for i in range(n)]
        for start, end in edges:
            neighbors[start].add(end)
            neighbors[end].add(start)

        # Initialize the first layer of leaves.
        leaves = []
        for i in range(n):
            if len(neighbors[i]) == 1:
                leaves.append(i)

        # Trim the leaves until reaching the centroids.
        remaining = n

        # For the tree-alike graph, the number of centroids is no more than 2.
        while remaining > 2:
            remaining -= len(leaves)
            new_leaves = []
            # Remove the current leaves along with the edges.
            while leaves:
                leaf = leaves.pop()
                # The only neighbor left for the leaf node.
                neighbor = neighbors[leaf].pop()
                # Remove the only edge left.
                neighbors[neighbor].remove(leaf)
                if len(neighbors[neighbor]) == 1:
                    new_leaves.append(neighbor)

            # Prepare for the next round.
            leaves = new_leaves

        # The remaining nodes are the centroids of the graph.
        return leaves