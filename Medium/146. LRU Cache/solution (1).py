# 146. LRU Cache

# Runtime: 1020 ms, faster than 18.01% of Python3 online submissions for LRU Cache.

# Memory Usage: 75.3 MB, less than 6.09% of Python3 online submissions for LRU Cache.


class LRUCache:
    def __init__(self, capacity: int) -> None:
        self._cache: DoubleList = DoubleList()
        self._cap: int = capacity
        self._map: dict[int, Node] = {}

    def get(self, key: int) -> int:
        if key not in self._map:
            return -1
        else:
            self._make_recently(key)
            return self._map[key].val

    def put(self, key: int, value: int) -> None:
        if key in self._map:
            self._remove(key)
        elif self._cap == self._cache.size:
            self._remove_least_recently()
        self._put_recently(key, value)

    def _put_recently(self, key: int, value: int) -> None:
        x = Node(key, value)
        self._cache.push(x)
        self._map[key] = x

    def _make_recently(self, key: int) -> None:
        x = self._map[key]
        self._cache.remove(x)
        self._cache.push(x)

    def _remove(self, key: int) -> None:
        x = self._map[key]
        del self._map[key]
        self._cache.remove(x)

    def _remove_least_recently(self) -> None:
        x = self._cache.pop()
        del self._map[x.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

class Node:
    def __init__(self, key: int, val: int) -> None:
        self.key: int = key
        self.val: int = val
        self.prev: Node = None
        self.next: Node = None


class DoubleList:
    def __init__(self) -> None:
        self._head: Node = Node(0, 0)
        self._tail: Node = Node(0, 0)
        self._head.next = self._tail
        self._tail.prev = self._head
        self._size: int = 0

    def push(self, x: Node) -> None:
        x.next = self._tail
        x.prev = self._tail.prev
        self._tail.prev.next = x
        self._tail.prev = x
        self._size += 1

    def remove(self, x: Node) -> None:
        x.prev.next = x.next
        x.next.prev = x.prev
        self._size -= 1

    def pop(self) -> Node:
        if self._size != 0:
            first = self._head.next
            self.remove(first)
            return first
        else:
            return None

    @property
    def size(self) -> int:
        return self._size