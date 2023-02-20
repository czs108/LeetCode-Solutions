# 733. Flood Fill

# Runtime: 72 ms, faster than 86.89% of Python3 online submissions for Flood Fill.

# Memory Usage: 14.3 MB, less than 76.43% of Python3 online submissions for Flood Fill.


class Solution:
    # Depth-First Search
    def floodFill(self, image: list[list[int]], sr: int, sc: int, newColor: int) -> list[list[int]]:
        color = image[sr][sc]
        if newColor == color:
            return image

        stack = [(sr, sc)]
        while stack:
            r, c = stack.pop(-1)
            if image[r][c] == color:
                image[r][c] = newColor

            if r >= 1 and image[r - 1][c] == color:
                stack.append((r - 1, c))
            if r + 1 < len(image) and image[r + 1][c] == color:
                stack.append((r + 1, c))
            if c >= 1 and image[r][c - 1] == color:
                stack.append((r, c - 1))
            if c + 1 < len(image[0]) and image[r][c + 1] == color:
                stack.append((r, c + 1))
        return image