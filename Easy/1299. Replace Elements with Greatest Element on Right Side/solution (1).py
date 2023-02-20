# 1299. Replace Elements with Greatest Element on Right Side


class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        if len(arr) == 0:
            return arr

        prev_max = -1
        for i in range(len(arr) - 1, -1, -1):
            curr_max = max(prev_max, arr[i])
            arr[i] = prev_max
            prev_max = curr_max
        return arr