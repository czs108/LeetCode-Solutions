# 155. Min Stack

# Runtime: 60 ms, faster than 82.30% of Python3 online submissions for Min Stack.

# Memory Usage: 17.4 MB, less than 5.36% of Python3 online submissions for Min Stack.


import math

class MinStack:
    def __init__(self) -> None:
        """
        initialize your data structure here.
        """
        self._stack = []
        self._min_val = math.inf

    def push(self, x: int) -> None:
        if x <= self._min_val:
            self._stack.append(self._min_val)
            self._min_val = x
        self._stack.append(x)

    def pop(self) -> None:
        min_val = self.getMin()
        n = self._stack.pop()
        if n == min_val:
            self._min_val = self._stack.pop()

    def top(self) -> int:
        return self._stack[-1]

    def getMin(self) -> int:
        return self._min_val


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()