# 489. Robot Room Cleaner


# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self) -> bool:
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        """
#
#    def turnLeft(self) -> None:
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        """
#
#    def turnRight(self) -> None:
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        """
#
#    def clean(self) -> None:
#        """
#        Clean the current cell.
#        """

from enum import IntEnum

# Going clockwise:
# 0: "up", 1: "right", 2: "down", 3: "left".
class Direction(IntEnum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

class Solution:
    # Backtracking
    def cleanRoom(self, robot: Robot) -> None:
        visited = set()
        dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        def go_back() -> None:
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()

        def backtrack(cell: tuple[int, int], dir: Direction) -> None:
            visited.add(cell)
            robot.clean()
            for i in range(len(dirs)):
                new_dir = (dir + i) % len(Direction)
                new_cell = (cell[0] + dirs[new_dir][0], cell[1] + dirs[new_dir][1])
                if new_cell not in visited and robot.move():
                    backtrack(new_cell, new_dir)
                    go_back()
                # Turn the robot following chosen direction: clockwise.
                robot.turnRight()

        backtrack((0, 0), Direction.UP)