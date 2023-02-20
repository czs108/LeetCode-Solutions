# 2094. Finding 3-Digit Even Numbers

# Runtime: 72 ms, faster than 91.81% of Python3 online submissions for Finding 3-Digit Even Numbers.

# Memory Usage: 14.2 MB, less than 94.61% of Python3 online submissions for Finding 3-Digit Even Numbers.


from collections import Counter

class Solution:
    def findEvenNumbers(self, digits: list[int]) -> list[int]:
        count = Counter(digits)
        ans = []
        for x in range(1, 10):
            count[x] -= 1
            for y in range(10):
                count[y] -= 1
                for z in range(10):
                    num = x * 100 + y * 10 + z
                    if num % 2 != 0:
                        continue

                    count[z] -= 1
                    if count[x] >= 0 and count[y] >= 0 and count[z] >= 0:
                        ans.append(num)
                    count[z] += 1
                count[y] += 1
            count[x] += 1
        return ans