# 706. Design HashMap

> Easy

------

Design a HashMap without using any built-in hash table libraries.

To be specific, your design should include these functions:

- `put(key, value)` inserts a `(key, value)` pair into the HashMap. If the value already exists in the HashMap, update the value.
- `get(key)` returns the value to which the specified key is mapped, or `-1` if this map contains no mapping for the key.
- `remove(key)` removes the mapping for the value key if this map contains the mapping for the key.

**Example:**

```c++
MyHashMap hashMap = new MyHashMap();
hashMap.put(1, 1);
hashMap.put(2, 2);
hashMap.get(1);         // returns 1
hashMap.get(3);         // returns -1 (not found)
hashMap.put(2, 1);      // update the existing value
hashMap.get(2);         // returns 1
hashMap.remove(2);      // remove the mapping for 2
hashMap.get(2);         // returns -1 (not found)
```