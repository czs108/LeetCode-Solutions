# 438. Find All Anagrams in a String

# Runtime: 382 ms, faster than 16.03% of Python3 online submissions for Find All Anagrams in a String.

# Memory Usage: 15.2 MB, less than 42.05% of Python3 online submissions for Find All Anagrams in a String.


from collections import Counter

class Solution:
    # Sliding Window with HashMap
    def findAnagrams(self, s: str, p: str) -> list[int]:
        if len(s) < len(p):
            return []

        count_s, count_p = Counter(), Counter(p)
        ans = []
        for i in range(len(s)):
            count_s[s[i]] += 1
            if i >= len(p):
                count_s[s[i - len(p)]] -= 1
                if count_s[s[i - len(p)]] == 0:
                    del count_s[s[i - len(p)]]

            if count_p == count_s:
                ans.append(i - len(p) + 1)

        return ans