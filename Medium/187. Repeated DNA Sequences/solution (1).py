# 187. Repeated DNA Sequences


class Solution:
    # Substring & Hash
    def findRepeatedDnaSequences(self, s: str) -> list[str]:
        L = 10
        seen, output = set(), set()
        for start in range(len(s) - L + 1):
            tmp = s[start:start + L]
            if tmp in seen:
                output.add(tmp[:])
            seen.add(tmp)
        return output