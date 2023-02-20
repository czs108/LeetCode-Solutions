# 733. Flood Fill

# Runtime: 80 ms, faster than 38.53% of Python3 online submissions for Flood Fill.

# Memory Usage: 14.7 MB, less than 10.35% of Python3 online submissions for Flood Fill.


class Solution:
    # Depth-First Search
    def floodFill(self, image: list[list[int]], sr: int, sc: int, newColor: int) -> list[list[int]]:
        color = image[sr][sc]
        if newColor == color:
            return image

        def dfs(r: int, c: int) -> None:
            if image[r][c] == color:
                image[r][c] = newColor
                if r >= 1:
                    dfs(r - 1, c)
                if r + 1 < len(image):
                    dfs(r + 1, c)
                if c >= 1:
                    dfs(r, c - 1)
                if c + 1 < len(image[0]):
                    dfs(r, c + 1)

        dfs(sr, sc)
        return image