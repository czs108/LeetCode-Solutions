# 139. Word Break

# Runtime: 28 ms, faster than 98.53% of Python3 online submissions for Word Break.

# Memory Usage: 14.3 MB, less than 87.71% of Python3 online submissions for Word Break.


class Solution:
    # Breadth-First Search
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        words = frozenset(wordDict)
        que = [0]
        visited = set()
        while que:
            start = que.pop()
            if start in visited:
                continue
            for end in range(start + 1, len(s) + 1):
                if s[start:end] in words:
                    if end == len(s):
                        return True
                    else:
                        que.append(end)
                visited.add(start)
        return False