// 706. Design HashMap

// Runtime: 19 ms, faster than 52.45% of Java online submissions for Design HashMap.

// Memory Usage: 45.7 MB, less than 100.00% of Java online submissions for Design HashMap.


// Tries
class MyHashMap {

    private Trie trie = new Trie();

    /** Initialize your data structure here. */
    public MyHashMap() { }

    /** value will always be non-negative. */
    public void put(int key, int value) {
        trie.put(key, value);
    }

    /** Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key */
    public int get(int key) {
        return trie.get(key);
    }

    /** Removes the mapping of the specified value key if this map contains a mapping for the key */
    public void remove(int key) {
        trie.remove(key);
    }
}


class Node {
    private static final int BASE = Trie.BASE;

    public int val;
    public boolean end;
    public Node[] next = new Node[BASE];

    public boolean hasNext() {
        for (Node x : next) {
            if (x != null) {
                return true;
            }
        }

        return false;
    }
}


class Trie {

    public static final int BASE = 10;

    private Node root = null;

    public void put(int key, int val) {
        root = put(root, key, val);
    }

    public void remove(int key) {
        root = remove(root, key);
    }

    public int get(int key) {
        return get(root, key);
    }

    private Node put(Node x, int key, int val) {
        if (x == null) {
            x = new Node();
        }

        if (key == 0) {
            x.end = true;
            x.val = val;
        } else {
            int dig = key % 10;
            x.next[dig] = put(x.next[dig], key / 10, val);
        }

        return x;
    }

    private int get(Node x, int key) {
        if (x == null) {
            return -1;
        } else if (key == 0) {
            return x.end ? x.val : -1;
        } else {
            return get(x.next[key % 10], key / 10);
        }
    }

    private Node remove(Node x, int key) {
        if (x == null) {
            return null;
        }

        if (key == 0) {
            x.end = false;
        } else {
            int dig = key % 10;
            x.next[dig] = remove(x.next[dig], key / 10);
        }

        if (x.end || x.hasNext()) {
            return x;
        } else {
            return null;
        }
    }
}

/**
 * Your MyHashMap object will be instantiated and called as such:
 * MyHashMap obj = new MyHashMap();
 * obj.put(key,value);
 * int param_2 = obj.get(key);
 * obj.remove(key);
 */