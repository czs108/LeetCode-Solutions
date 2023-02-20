# 136. Single Number

# Runtime: 2116 ms, faster than 9.40% of Python3 online submissions for Single Number.

# Memory Usage: 16.2 MB, less than 6.56% of Python3 online submissions for Single Number.


class Solution:
    # List operation
    def singleNumber(self, nums: list[int]) -> int:
        # Iterate over all the elements in `nums`
        no_duplicate_list = []
        for i in nums:
            # If some number in `nums` is new to array, append it
            # If some number is already in the array, remove it
            if i not in no_duplicate_list:
                no_duplicate_list.append(i)
            else:
                no_duplicate_list.remove(i)
        return no_duplicate_list.pop()