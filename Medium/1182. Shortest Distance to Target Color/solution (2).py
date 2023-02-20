# 1182. Shortest Distance to Target Color

# Runtime: 3768 ms, faster than 6.63% of Python3 online submissions for Shortest Distance to Target Color.

# Memory Usage: 38.2 MB, less than 24.70% of Python3 online submissions for Shortest Distance to Target Color.


class Solution:
    # Dynamic Programming
    def shortestDistanceColor(self, colors: list[int], queries: list[list[int]]) -> list[int]:
        dist = [[-1] * len(colors) for _ in range(3)]
        right_most = [0, 0, 0]
        left_most = [len(colors) - 1, len(colors) - 1, len(colors) - 1]

        # Iterating from left to right,
        # and looking forwards to find the nearest target color on the left.
        for i in range(len(colors)):
            color = colors[i] - 1
            for j in range(right_most[color], i + 1):
                dist[color][j] = i - j
            right_most[color] = i + 1

        # Iterating from right to left,
        # and looking backwards to find the nearest target color on the right.
        for i in range(len(colors) - 1, -1, -1):
            color = colors[i] - 1
            for j in range(left_most[color], i - 1, -1):
                if dist[color][j] == -1 or dist[color][j] > j - i:
                    dist[color][j] = j - i
            left_most[color] = i - 1

        return [dist[color - 1][index] for index, color in queries]