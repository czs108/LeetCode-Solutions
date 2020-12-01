# 14. Longest Common Prefix

# Runtime: 28 ms, faster than 88.38% of Python3 online submissions for Longest Common Prefix.

# Memory Usage: 14 MB, less than 6.67% of Python3 online submissions for Longest Common Prefix.


class Solution:
    # Divide and conquer
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        else:
            return Solution._longestCommonPrefix(strs, 0, len(strs) - 1)

    @staticmethod
    def _longestCommonPrefix(strs: List[str], left: int, right: int) -> str:
        if left >= right:
            return strs[left]
        else:
            mid = left + (right - left) // 2
            lcpLeft = Solution._longestCommonPrefix(strs, left, mid)
            lcpRight = Solution._longestCommonPrefix(strs, mid + 1, right)
            return Solution._commonPrefix(lcpLeft, lcpRight)

    @staticmethod
    def _commonPrefix(left: str, right: str) -> str:
        min_len = min(len(left), len(right))
        for i in range(min_len):
            if left[i] != right[i]:
                return left[:i]
        return left[:min_len]