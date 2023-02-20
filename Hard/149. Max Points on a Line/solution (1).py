# 149. Max Points on a Line

# Runtime: 52 ms, faster than 82.49% of Python3 online submissions for Max Points on a Line.

# Memory Usage: 14.4 MB, less than 41.33% of Python3 online submissions for Max Points on a Line.


import math

class Solution:
    # Enumeration
    def maxPoints(self, points: list[list[int]]) -> int:
        if len(points) < 3:
            return len(points)

        def slope_coprime(p1: tuple[int, int], p2: tuple[int, int]) -> tuple[int, int]:
            dx, dy = p1[0] - p2[0], p1[1] - p2[1]
            if dx == 0:
                return (0, 0)
            elif dy == 0:
                return (math.inf, math.inf)
            elif dx < 0:
                dx, dy = -dx, -dy
            gcd = math.gcd(dx, dy)
            return (dx / gcd, dy / gcd)

        def max_points_on_a_line(i: int) -> int:
            lines = {}
            count, count_on_horizontal_lines = 1, 1
            # There is no duplicates of a point `i` so far.
            duplicates = 0

            def add_line(p1: tuple[int, int], p2: tuple[int, int]) -> int:
                """
                Add a line passing through `p1` and `p2` points.
                Update max number of points on a line containing point `p1`.
                Update a number of duplicates of `p1` point.
                """
                nonlocal count, duplicates, count_on_horizontal_lines
                if p1 == p2:
                    duplicates += 1
                elif p1[1] == p2[1]:
                    count_on_horizontal_lines += 1
                    count = max(count_on_horizontal_lines, count)
                else:
                    slope = slope_coprime(p1, p2)
                    lines[slope] = lines.get(slope, 1) + 1
                    count = max(lines[slope], count)

            for j in range(i + 1, len(points)):
                add_line(points[i], points[j])
            return count + duplicates

        max_count = 1
        for i in range(len(points) - 1):
            max_count = max(max_count, max_points_on_a_line(i))
        return max_count