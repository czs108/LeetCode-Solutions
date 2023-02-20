# 28. Implement strStr()

# Runtime: 40 ms, faster than 26.40% of Python3 online submissions for Implement strStr().

# Memory Usage: 14.3 MB, less than 43.53% of Python3 online submissions for Implement strStr().


class Solution:
    _BASE = 10**6
    _SCALE = 31

    # Rabin-Karp
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0

        def _hash(needle: str) -> int:
            hash = 0
            for c in needle:
                hash = (hash * self._SCALE + ord(c)) % self._BASE
            return hash

        def _max_power(needle: str) -> int:
            power = 1
            for _ in range(len(needle)):
                power = (power * self._SCALE) % self._BASE
            return power

        max_power = _max_power(needle)
        target = _hash(needle)
        hash = 0
        for i in range(len(haystack)):
            hash = (hash * self._SCALE + ord(haystack[i])) % self._BASE
            if i < len(needle) - 1:
                continue
            elif i >= len(needle):
                hash = hash - (ord(haystack[i - len(needle)]) * max_power) % self._BASE
                hash = hash if hash >= 0 else hash + self._BASE

            if hash == target and haystack[i - len(needle) + 1:i + 1] == needle:
                return i - len(needle) + 1

        return -1