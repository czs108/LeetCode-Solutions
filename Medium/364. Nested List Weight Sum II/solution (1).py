# 364. Nested List Weight Sum II

# Runtime: 32 ms, faster than 69.56% of Python3 online submissions for Nested List Weight Sum II.

# Memory Usage: 14.5 MB, less than 82.51% of Python3 online submissions for Nested List Weight Sum II.


# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None) -> None:
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self) -> bool:
#        """
#        Return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def add(self, elem) -> None:
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        """
#
#    def setInteger(self, value) -> None:
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        """
#
#    def getInteger(self) -> int:
#        """
#        Return the single integer that this NestedInteger holds, if it holds a single integer.
#        Return None if this NestedInteger holds a nested list.
#        """
#
#    def getList(self) -> list[NestedInteger]:
#        """
#        Return the nested list that this NestedInteger holds, if it holds a nested list.
#        Return None if this NestedInteger holds a single integer.
#        """

class Solution:
    # Double Pass Depth-First Search
    def depthSumInverse(self, nestedList: list[NestedInteger]) -> int:

        def find_max_depth(list: list[NestedInteger]) -> int:
            depth = 1
            for nested in list:
                if not nested.isInteger():
                    depth = max(depth, find_max_depth(nested.getList()) + 1)
            return depth

        def calc_weighted_sum(list: list[NestedInteger], depth: int, max_depth: int) -> int:
            sum = 0
            for nested in list:
                if nested.isInteger():
                    sum += (max_depth - depth + 1) * nested.getInteger()
                else:
                    sum += calc_weighted_sum(nested.getList(), depth + 1, max_depth)
            return sum


        max_depth = find_max_depth(nestedList)
        return calc_weighted_sum(nestedList, 1, max_depth)