# 155. Min Stack

# Runtime: 60 ms, faster than 82.30% of Python3 online submissions for Min Stack.

# Memory Usage: 17.4 MB, less than 5.36% of Python3 online submissions for Min Stack.


import sys

class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.__stack = []
        self.__min_val = sys.maxsize

    def push(self, x: int) -> None:
        if x <= self.__min_val:
            self.__stack.append(self.__min_val)
            self.__min_val = x
        self.__stack.append(x)

    def pop(self) -> None:
        assert len(self.__stack) != 0
        min_val = self.getMin()
        n = self.__stack.pop()
        if n == min_val:
            self.__min_val = self.__stack.pop()

    def top(self) -> int:
        assert len(self.__stack) != 0
        return self.__stack[-1]

    def getMin(self) -> int:
        assert len(self.__stack) != 0
        return self.__min_val


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()