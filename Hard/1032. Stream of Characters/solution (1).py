# 1032. Stream of Characters

# Runtime: 616 ms, faster than 77.84% of Python3 online submissions for Stream of Characters.

# Memory Usage: 38.1 MB, less than 71.11% of Python3 online submissions for Stream of Characters.


from collections import deque

class StreamChecker:
    # Trie
    _KEY: str = "$"

    def __init__(self, words: list[str]) -> None:
        self._trie: dict = {}
        self._stream: deque = deque([])

        # Build a trie.
        for word in words:
            node = self._trie
            for c in word[::-1]:
                node = node.setdefault(c, {})
            node[self._KEY] = word

    def query(self, letter: str) -> bool:
        self._stream.appendleft(letter)

        node = self._trie
        for c in self._stream:
            if self._KEY in node:
                return True
            elif c not in node:
                return False
            else:
                node = node[c]
        return self._KEY in node

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)