# 251. Flatten 2D Vector


class Vector2D:
    # Flatten List
    def __init__(self, vec: list[list[int]]) -> None:
        self._nums: list[int] = []
        self._idx: int = 0
        for list in vec:
            for n in list:
                self._nums.append(n)

    def next(self) -> int:
        num = self._nums[self._idx]
        self._idx += 1
        return num

    def hasNext(self) -> bool:
        return self._idx < len(self._nums)

# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()