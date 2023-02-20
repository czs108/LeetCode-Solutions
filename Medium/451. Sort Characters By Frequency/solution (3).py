# 451. Sort Characters By Frequency

# Runtime: 48 ms, faster than 65.90% of Python3 online submissions for Sort Characters By Frequency.

# Memory Usage: 19.1 MB, less than 12.36% of Python3 online submissions for Sort Characters By Frequency.


from collections import Counter

class Solution:
    # Multiset and Bucket Sort
    def frequencySort(self, s: str) -> str:
        # Determine the frequency of each character.
        counts = Counter(s)
        max_freq = max(counts.values())

        # Bucket sort the characters by frequency.
        buckets = [[] for _ in range(max_freq + 1)]
        for c, i in counts.items():
            buckets[i].append(c)

        # Build up the string.
        string_builder = []
        for i in range(len(buckets) - 1, 0, -1):
            for c in buckets[i]:
                string_builder.append(c * i)

        return "".join(string_builder)