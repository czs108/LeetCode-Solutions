// 706. Design HashMap

// Runtime: 48 ms, faster than 18.18% of Java online submissions for Design HashMap.

// Memory Usage: 46.6 MB, less than 100.00% of Java online submissions for Design HashMap.


class MyHashMap {

    private static final int MAX_SIZE = 1000000 + 1;

    private int[] data = new int[MAX_SIZE];

    /** Initialize your data structure here. */
    public MyHashMap() {
        Arrays.fill(data, -1);
    }

    /** value will always be non-negative. */
    public void put(int key, int value) {
        data[key] = value;
    }

    /** Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key */
    public int get(int key) {
        return data[key];
    }

    /** Removes the mapping of the specified value key if this map contains a mapping for the key */
    public void remove(int key) {
        data[key] = -1;
    }
}

/**
 * Your MyHashMap object will be instantiated and called as such:
 * MyHashMap obj = new MyHashMap();
 * obj.put(key,value);
 * int param_2 = obj.get(key);
 * obj.remove(key);
 */