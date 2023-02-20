# 264. Ugly Number II

# Runtime: 173 ms, faster than 54.94% of Python3 online submissions for Ugly Number II.

# Memory Usage: 14.2 MB, less than 73.79% of Python3 online submissions for Ugly Number II.


class Solution:
    # Three Pointers
    def nthUglyNumber(self, n: int) -> int:
        nums = [1]
        p2, p3, p5 = 0, 0, 0
        for _ in range(1, n):
            n2 = 2 * nums[p2]
            n3 = 3 * nums[p3]
            n5 = 5 * nums[p5]
            nums.append(min(n2, n3, n5))
            if nums[-1] == n2:
                p2 += 1
            if nums[-1] == n3:
                p3 += 1
            if nums[-1] == n5:
                p5 += 1
        return nums[-1]