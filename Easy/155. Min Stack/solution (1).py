# 155. Min Stack

# Runtime: 60 ms, faster than 82.31% of Python3 online submissions for Min Stack.

# Memory Usage: 17.5 MB, less than 5.36% of Python3 online submissions for Min Stack.


class MinStack:
    def __init__(self) -> None:
        """
        initialize your data structure here.
        """
        self._stack = []
        self._min_stack = []

    def push(self, x: int) -> None:
        self._stack.append(x)
        if len(self._min_stack) == 0 or x <= self.getMin():
            self._min_stack.append(x)

    def pop(self) -> None:
        min_val = self.getMin()
        n = self._stack.pop()
        if n == min_val:
            self._min_stack.pop()

    def top(self) -> int:
        return self._stack[-1]

    def getMin(self) -> int:
        return self._min_stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()