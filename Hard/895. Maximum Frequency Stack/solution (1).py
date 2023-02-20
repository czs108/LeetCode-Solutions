# 895. Maximum Frequency Stack


from collections import Counter, defaultdict

class FreqStack:
    # Stack of Stacks
    def __init__(self) -> None:
        self._freq: Counter = Counter()
        self._group: dict = defaultdict(list)
        self._max_freq: int = 0

    def push(self, val: int) -> None:
        self._freq[val] += 1
        freq = self._freq[val]
        self._group[freq].append(val)
        if freq > self._max_freq:
            self._max_freq = freq

    def pop(self) -> int:
        val = self._group[self._max_freq].pop()
        self._freq[val] -= 1
        if not self._group[self._max_freq]:
            self._max_freq -= 1
        return val

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()