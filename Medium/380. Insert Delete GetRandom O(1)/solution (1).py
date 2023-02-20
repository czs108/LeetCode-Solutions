# 380. Insert Delete GetRandom O(1)


from random import choice

class RandomizedSet:
    def __init__(self) -> None:
        self._val_to_idx: dict[int, int] = {}
        self._vals: list[int] = []

    def insert(self, val: int) -> bool:
        if val in self._val_to_idx:
            return False
        else:
            self._val_to_idx[val] = len(self._vals)
            self._vals.append(val)
            return True

    def remove(self, val: int) -> bool:
        if val not in self._val_to_idx:
            return False
        else:
            idx = self._val_to_idx[val]
            last_val = self._vals[-1]
            self._vals[idx], self._val_to_idx[last_val] = last_val, idx
            self._vals.pop()
            del self._val_to_idx[val]
            return True

    def getRandom(self) -> int:
        return choice(self._vals)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()