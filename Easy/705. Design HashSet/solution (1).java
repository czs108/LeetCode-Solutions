// 705. Design HashSet

// Runtime: 15 ms, faster than 51.09% of Java online submissions for Design HashSet.

// Memory Usage: 48.4 MB, less than 100.00% of Java online submissions for Design HashSet.


class MyHashSet {

    private static final int MAX_SIZE = 1000000 + 1;

    private boolean[] data = new boolean[MAX_SIZE];

    /** Initialize your data structure here. */
    public MyHashSet() { }

    public void add(int key) {
        data[key] = true;
    }

    public void remove(int key) {
        data[key] = false;
    }

    /** Returns true if this set contains the specified element */
    public boolean contains(int key) {
        return data[key];
    }
}

/**
 * Your MyHashSet object will be instantiated and called as such:
 * MyHashSet obj = new MyHashSet();
 * obj.add(key);
 * obj.remove(key);
 * boolean param_3 = obj.contains(key);
 */