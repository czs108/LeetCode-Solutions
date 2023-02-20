# 451. Sort Characters By Frequency

# Runtime: 36 ms, faster than 92.48% of Python3 online submissions for Sort Characters By Frequency.

# Memory Usage: 15.5 MB, less than 40.28% of Python3 online submissions for Sort Characters By Frequency.


from collections import Counter

class Solution:
    # HashMap and Sort
    def frequencySort(self, s: str) -> str:
        # Count up the occurances.
        counts = Counter(s)

        # Build up the string builder.
        string_builder = []
        for letter, freq in counts.most_common():
            string_builder.append(letter * freq)
        return "".join(string_builder)