# 14. Longest Common Prefix

# Runtime: 28 ms, faster than 88.38% of Python3 online submissions for Longest Common Prefix.

# Memory Usage: 14 MB, less than 6.67% of Python3 online submissions for Longest Common Prefix.


class Solution:
    # Divide and conquer
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if len(strs) == 0:
            return ""
        else:
            def common_prefix(left: str, right: str) -> str:
                min_len = min(len(left), len(right))
                for i in range(min_len):
                    if left[i] != right[i]:
                        return left[:i]
                return left[:min_len]

            def longest_common_prefix(left: int, right: int) -> str:
                if left >= right:
                    return strs[left]
                else:
                    mid = left + (right - left) // 2
                    left_lcp = longest_common_prefix(left, mid)
                    right_lcp = longest_common_prefix(mid + 1, right)
                    return common_prefix(left_lcp, right_lcp)

            return longest_common_prefix(0, len(strs) - 1)