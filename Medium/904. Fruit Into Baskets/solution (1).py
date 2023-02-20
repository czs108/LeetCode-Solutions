# 904. Fruit Into Baskets

# Runtime: 820 ms, faster than 66.72% of Python3 online submissions for Fruit Into Baskets.

# Memory Usage: 20.1 MB, less than 70.93% of Python3 online submissions for Fruit Into Baskets.


class Solution:
    # Sliding Window
    def totalFruit(self, fruits: list[int]) -> int:
        if len(fruits) <= 2:
            return len(fruits)

        max_count = 0
        last_occur = {}
        left = 0
        for right, type in enumerate(fruits):
            last_occur[type] = right

            # The windows can only contain up to 2 types of fruit.
            if len(last_occur) > 2:
                # Remove the earliest appearing type.
                removed = min(last_occur.items(), key = lambda x: x[1])[0]
                left = last_occur[removed] + 1
                del last_occur[removed]
            max_count = max(max_count, right - left + 1)
        return max_count