# 170. Two Sum III - Data Structure Design

# Runtime: 428 ms, faster than 65.04% of Python3 online submissions for Two Sum III - Data Structure Design.

# Memory Usage: 18.5 MB, less than 19.16% of Python3 online submissions for Two Sum III - Data Structure Design.


from collections import Counter

class TwoSum:
    # HashTable
    def __init__(self) -> None:
        self._count: Counter = Counter()

    def add(self, number: int) -> None:
        self._count[number] += 1

    def find(self, value: int) -> bool:
        for num in self._count.keys():
            comple = value - num
            if comple != num:
                if comple in self._count:
                    return True
            elif self._count[num] > 1:
                return True
        return False

# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)