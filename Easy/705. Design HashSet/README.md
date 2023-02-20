# 705. Design HashSet

> Easy

------

Design a HashSet without using any built-in hash table libraries.

To be specific, your design should include these functions:

- `add(value)` inserts a value into the HashSet.
- `contains(value)` returns whether the value exists in the HashSet or not.
- `remove(value)` removes a value in the HashSet. If the value does not exist in the HashSet, do nothing.

**Example:**

```c++
MyHashSet hashSet = new MyHashSet();
hashSet.add(1);
hashSet.add(2);
hashSet.contains(1);    // returns true
hashSet.contains(3);    // returns false (not found)
hashSet.add(2);
hashSet.contains(2);    // returns true
hashSet.remove(2);
hashSet.contains(2);    // returns false (already removed)
```