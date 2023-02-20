// 706. Design HashMap

// Runtime: 25 ms, faster than 38.79% of Java online submissions for Design HashMap.

// Memory Usage: 52.6 MB, less than 56.76% of Java online submissions for Design HashMap.


class Slot {
    public int key;
    public int val;
    public Slot next;

    public Slot(int key, int val) {
        this.key = key;
        this.val = val;
    }
}

// List
class MyHashMap {

    private static final int MAX_SIZE = 1000;

    private Slot[] slots = new Slot[MAX_SIZE];

    /** Initialize your data structure here. */
    public MyHashMap() { }

    /** value will always be non-negative. */
    public void put(int key, int value) {
        int hash = getHash(key);
        var slot = slots[hash];
        if (slot == null) {
            slots[hash] = new Slot(key, value);
        } else {
            while (slot.key != key && slot.next != null) {
                slot = slot.next;
            }

            if (slot.key == key) {
                slot.val = value;
            } else {
                slot.next = new Slot(key, value);
            }
        }
    }

    /** Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key */
    public int get(int key) {
        var slot = slots[getHash(key)];
        while (slot != null && slot.key != key) {
            slot = slot.next;
        }

        return slot != null ? slot.val : -1;
    }

    /** Removes the mapping of the specified value key if this map contains a mapping for the key */
    public void remove(int key) {
        int hash = getHash(key);
        var slot = slots[hash];
        if (slot == null) {
            return;
        } else if (slot.key == key) {
            slots[hash] = slot.next;
        } else {
            while (slot.next != null && slot.next.key != key) {
                slot = slot.next;
            }

            if (slot.next != null) {
                slot.next = slot.next.next;
            }
        }
    }

    private int getHash(int key) {
        return key % MAX_SIZE;
    }
}

/**
 * Your MyHashMap object will be instantiated and called as such:
 * MyHashMap obj = new MyHashMap();
 * obj.put(key,value);
 * int param_2 = obj.get(key);
 * obj.remove(key);
 */