# 1153. String Transforms Into Another String

# Runtime: 28 ms, faster than 81.33% of Python3 online submissions for String Transforms Into Another String.

# Memory Usage: 14.3 MB, less than 83.23% of Python3 online submissions for String Transforms Into Another String.


class Solution:
    # Greedy | Hash
    def canConvert(self, str1: str, str2: str) -> bool:
        # To convert:
        #   1. No character in `str1` is mapped to multiple characters in `str2`.
        #   2. The number of unique letters in `str2` should be strictly less than 26 unless `str1` equals `str2`.
        if str1 == str2:
            return True

        conversion_map = dict()
        unique_chars_in_str2 = set()

        # Make sure that no character in `str1` is mapped to multiple characters in `str2`.
        for c1, c2 in zip(str1, str2):
            if c1 not in conversion_map:
                conversion_map[c1] = c2
                unique_chars_in_str2.add(c2)
            elif conversion_map[c1] != c2:
                return False

        return len(unique_chars_in_str2) < 26