# 642. Design Search Autocomplete System

# Runtime: 2457 ms, faster than 5.01% of Python3 online submissions for Design Search Autocomplete System.

# Memory Usage: 18.3 MB, less than 78.46% of Python3 online submissions for Design Search Autocomplete System.


from queue import PriorityQueue

class Node(tuple):
    def __lt__(self, other: Node) -> bool:
        time1, sentence1 = self
        time2, sentence2 = other
        if time1 == time2:
            return sentence1 > sentence2
        else:
            return time1 < time2


class Trie:
    _KEY = "$"

    def __init__(self, max_ret: int) -> None:
        self._max_ret: int = max_ret
        self._trie: dict = {}

    def insert(self, sentence: str, hot_increment: int) -> None:
        node = self._trie
        for c in sentence:
            node = node.setdefault(c, {})
        prev = node.get(self._KEY, (0, None))
        node[self._KEY] = (prev[0] + hot_increment, sentence)

    def collect(self, prefix: str) -> list[str]:
        node = self._trie
        for c in prefix:
            node = node.get(c)
            if not node:
                return []

        stack = [iter(node.items())]
        que = PriorityQueue()
        while stack:
            char, next_node = next(stack[-1], (None, None))
            if char is None:
                stack.pop()
            elif char == self._KEY:
                que.put(Node(next_node))
                if que.qsize() > self._max_ret:
                    que.get()
            else:
                stack.append(iter(next_node.items()))

        res = []
        while not que.empty():
            res.append(que.get()[1])
        res.reverse()
        return res


class AutocompleteSystem:
    # Trie | Priority Queue
    def __init__(self, sentences: list[str], times: list[int]) -> None:
        self._sentence: str = ""
        self._trie: Trie = Trie(3)
        for sentence, time in zip(sentences, times):
            self._trie.insert(sentence, time)

    def input(self, c: str) -> list[str]:
        if c != "#":
            self._sentence += c
            return self._trie.collect(self._sentence)
        else:
            self._trie.insert(self._sentence, 1)
            self._sentence = ""
            return []

# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)