# 49. Group Anagrams

# Runtime: 96 ms, faster than 84.18% of Python3 online submissions for Group Anagrams.

# Memory Usage: 18.2 MB, less than 34.33% of Python3 online submissions for Group Anagrams.


from collections import defaultdict

class Solution:
    # Categorize by Sorted String
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        ans = defaultdict(list)
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        return ans.values()