# 251. Flatten 2D Vector

# Runtime: 80 ms, faster than 76.24% of Python3 online submissions for Flatten 2D Vector.

# Memory Usage: 19.4 MB, less than 35.97% of Python3 online submissions for Flatten 2D Vector.


class Vector2D:
    # Two Pointers
    def __init__(self, vec: list[list[int]]) -> None:
        self._vec: list[list[int]] = vec
        self._inner: int = 0
        self._outer: int = 0

    def next(self) -> int:
        self._advance_to_next()
        num = self._vec[self._outer][self._inner]
        self._inner += 1
        return num

    def hasNext(self) -> bool:
        self._advance_to_next()
        return self._outer < len(self._vec)

    def _advance_to_next(self) -> None:
        while self._outer < len(self._vec) and self._inner == len(self._vec[self._outer]):
            self._outer += 1
            self._inner = 0

# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()