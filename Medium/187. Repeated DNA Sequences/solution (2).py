# 187. Repeated DNA Sequences

# Runtime: 174 ms, faster than 5.02% of Python3 online submissions for Repeated DNA Sequences.

# Memory Usage: 24.5 MB, less than 93.98% of Python3 online submissions for Repeated DNA Sequences.


class Solution:
    # Rabin-Karp
    def findRepeatedDnaSequences(self, s: str) -> list[str]:
        L = 10
        if len(s) <= L:
            return []

        # Convert string to array of integers.
        base = 4
        max_digt = pow(base, L)
        to_int = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
        nums = [to_int[c] for c in s]

        hash = 0
        seen, output = set(), set()
        for start in range(len(s) - L + 1):
            if start != 0:
                hash = hash * base - nums[start - 1] * max_digt + nums[start + L - 1]
            else:
                for i in range(L):
                    hash = hash * base + nums[i]

            if hash in seen:
                output.add(s[start:start + L])
            seen.add(hash)
        return output