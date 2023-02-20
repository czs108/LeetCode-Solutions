# 451. Sort Characters By Frequency

# Runtime: 60 ms, faster than 42.47% of Python3 online submissions for Sort Characters By Frequency.

# Memory Usage: 16.9 MB, less than 16.64% of Python3 online submissions for Sort Characters By Frequency.


class Solution:
    def frequencySort(self, s: str) -> str:
        if not s:
            return s

        # Convert `s` to a list.
        s = list(s)

        # Sort the characters in `s`.
        s.sort()

        # Make a list of strings, one for each unique char.
        all_strings = []
        cur_sb = [s[0]]
        for c in s[1:]:
            # If the last character on string builder is different...
            if cur_sb[-1] != c:
                all_strings.append("".join(cur_sb))
                cur_sb = []
            cur_sb.append(c)
        all_strings.append("".join(cur_sb))

        # Sort the strings by length from longest to shortest.
        all_strings.sort(key=lambda string : len(string), reverse=True)

        # Convert to a single string to return.
        # Converting a list of strings to a string is often done
        # using this rather strange looking python idiom.
        return "".join(all_strings)