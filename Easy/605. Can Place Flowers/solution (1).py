# 605. Can Place Flowers

# Runtime: 227 ms, faster than 27.46% of Python3 online submissions for Can Place Flowers.

# Memory Usage: 14.4 MB, less than 95.37% of Python3 online submissions for Can Place Flowers.


class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        if n == 0:
            return True

        count = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0 and \
                (i == 0 or flowerbed[i - 1] == 0) and \
                    (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0):
                count += 1
                flowerbed[i] = 1
                if count == n:
                    return True
        return False