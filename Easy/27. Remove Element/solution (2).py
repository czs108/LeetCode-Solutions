# 27. Remove Element


class Solution:
    # Two Pointers - when elements to remove are rare
    def removeElement(self, nums: list[int], val: int) -> int:
        # When encountering `nums[i]` = `val`,
        # swap the current element out with the last element and dispose the last one.
        # This essentially reduces the array's size by 1.
        i = 0
        n = len(nums)
        while i < n:
            if nums[i] == val:
                # Note that the last element that was swapped in could be the value you want to remove itself.
                # But in the next iteration we will still check this element.
                nums[i] = nums[n - 1]
                n -= 1
            else:
                i += 1
        return n