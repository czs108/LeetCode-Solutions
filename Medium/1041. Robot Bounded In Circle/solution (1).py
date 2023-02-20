# 1041. Robot Bounded In Circle

# Runtime: 28 ms, faster than 86.38% of Python3 online submissions for Robot Bounded In Circle.

# Memory Usage: 14.2 MB, less than 76.87% of Python3 online submissions for Robot Bounded In Circle.


class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        # North, east, south, west
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        x = y = 0
        # Facing north.
        idx = 0

        for i in instructions:
            if i == "L":
                idx = (idx + 3) % 4
            elif i == "R":
                idx = (idx + 1) % 4
            else:
                x += directions[idx][0]
                y += directions[idx][1]

        # After one cycle:
        # robot returns into initial position
        # or robot doesn't face north.
        return (x == 0 and y == 0) or idx != 0