# 170. Two Sum III - Data Structure Design

# Runtime: 560 ms, faster than 49.70% of Python3 online submissions for Two Sum III - Data Structure Design.

# Memory Usage: 18.1 MB, less than 84.27% of Python3 online submissions for Two Sum III - Data Structure Design.


class TwoSum:
    # Sorted List | Two Pointers
    def __init__(self) -> None:
        self._nums: list[int] = []
        self._sorted: bool = False

    def add(self, number: int) -> None:
        self._nums.append(number)
        self._sorted = False

    def find(self, value: int) -> bool:
        if not self._sorted:
            self._nums.sort()
            self._sorted= True

        left, right = 0, len(self._nums) - 1
        while left < right:
            sum = self._nums[left] + self._nums[right]
            if sum < value:
                left += 1
            elif sum > value:
                right -= 1
            else:
                return True
        return False

# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)