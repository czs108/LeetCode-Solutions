# 28. Implement strStr()

# Runtime: 40 ms, faster than 26.40% of Python3 online submissions for Implement strStr().

# Memory Usage: 14.3 MB, less than 43.53% of Python3 online submissions for Implement strStr().


class Solution:
    _HASH_BASE = 10**6
    _HASH_SCALE = 31

    # Rabin-Karp
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) == 0:
            return 0

        max_power = Solution._maxPower(needle)
        target = Solution._hash(needle)
        hash = 0
        for i in range(len(haystack)):
            hash = (hash * Solution._HASH_SCALE + ord(haystack[i])) % Solution._HASH_BASE
            if i < len(needle) - 1:
                continue

            if i >= len(needle):
                hash = hash - (ord(haystack[i - len(needle)]) * max_power) % Solution._HASH_BASE
                hash = hash if hash >= 0 else hash + Solution._HASH_BASE

            if hash == target and haystack[i - len(needle) + 1:i + 1] == needle:
                return i - len(needle) + 1

        return -1

    @classmethod
    def _hash(cls, needle: str) -> int:
        hash = 0
        for c in needle:
            hash = (hash * cls._HASH_SCALE + ord(c)) % cls._HASH_BASE
        return hash

    @classmethod
    def _maxPower(cls, needle: str) -> int:
        power = 1
        for _ in range(len(needle)):
            power = (power * cls._HASH_SCALE) % cls._HASH_BASE
        return power