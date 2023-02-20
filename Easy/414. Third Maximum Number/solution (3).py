# 414. Third Maximum Number

# Runtime: 52 ms, faster than 62.62% of Python3 online submissions for Third Maximum Number.

# Memory Usage: 15.3 MB, less than 54.18% of Python3 online submissions for Third Maximum Number.


class Solution:
    # Seen-Maximums Set
    def thirdMax(self, nums: list[int]) -> int:
        seen_maxs = set()

        def max_ignoring_seen() -> int:
            max_num = None
            for num in nums:
                if num in seen_maxs:
                    continue
                elif max_num == None or num > max_num:
                    max_num = num
            return max_num

        for _ in range(3):
            curr_max = max_ignoring_seen()
            if curr_max == None:
                return max(seen_maxs)
            seen_maxs.add(curr_max)
        return min(seen_maxs)