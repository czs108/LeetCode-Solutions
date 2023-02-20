# 27. Remove Element

# Runtime: 36 ms, faster than 18.84% of Python3 online submissions for Remove Element.

# Memory Usage: 14 MB, less than 6.06% of Python3 online submissions for Remove Element.


class Solution:
    # Two Pointers
    def removeElement(self, nums: list[int], val: int) -> int:
        n = 0
        for c in nums:
            if c != val:
                nums[n] = c
                n += 1
        return n

# When `nums` = [1,2,3,5,4], `val` = 4, or `nums` = [4,1,2,3,5], `val` = 4
# the algorithm will do unnecessary copy.