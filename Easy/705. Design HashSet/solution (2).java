// 705. Design HashSet

// Runtime: 27 ms, faster than 29.47% of Java online submissions for Design HashSet.

// Memory Usage: 45.7 MB, less than 100.00% of Java online submissions for Design HashSet.


class Slot {
    public int val;
    public Slot next;

    public Slot(int val) {
        this.val = val;
    }
}

// List
class MyHashSet {

    private static final int MAX_SIZE = 1000;

    private Slot[] slots = new Slot[MAX_SIZE];

    /** Initialize your data structure here. */
    public MyHashSet() { }

    public void add(int key) {
        int hash = getHash(key);
        var slot = slots[hash];
        if (slot == null) {
            slots[hash] = new Slot(key);
        } else {
            while (slot.val != key && slot.next != null) {
                slot = slot.next;
            }

            if (slot.val != key && slot.next == null) {
                slot.next = new Slot(key);
            }
        }
    }

    public void remove(int key) {
        int hash = getHash(key);
        var slot = slots[hash];
        if (slot == null) {
            return;
        } else if (slot.val == key) {
            slots[hash] = slot.next;
        } else {
            while (slot.next != null && slot.next.val != key) {
                slot = slot.next;
            }

            if (slot.next != null) {
                slot.next = slot.next.next;
            }
        }
    }

    /** Returns true if this set contains the specified element */
    public boolean contains(int key) {
        var slot = slots[getHash(key)];
        while (slot != null && slot.val != key) {
            slot = slot.next;
        }

        return slot != null;
    }

    private int getHash(int key) {
        return key % MAX_SIZE;
    }
}

/**
 * Your MyHashSet object will be instantiated and called as such:
 * MyHashSet obj = new MyHashSet();
 * obj.add(key);
 * obj.remove(key);
 * boolean param_3 = obj.contains(key);
 */