// 705. Design HashSet

// Runtime: 13 ms, faster than 71.59% of Java online submissions for Design HashSet.

// Memory Usage: 47.6 MB, less than 100.00% of Java online submissions for Design HashSet.


// Tries
class MyHashSet {

    private Trie trie = new Trie();

    /** Initialize your data structure here. */
    public MyHashSet() { }

    public void add(int key) {
        trie.add(key);
    }

    public void remove(int key) {
        trie.remove(key);
    }

    /** Returns true if this set contains the specified element */
    public boolean contains(int key) {
        return trie.contains(key);
    }
}


class Node {
    private static final int BASE = Trie.BASE;

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

    public void add(int key) {
        root = add(root, key);
    }

    public boolean contains(int key) {
        return contains(root, key);
    }

    public void remove(int key) {
        root = remove(root, key);
    }

    private Node add(Node x, int key) {
        if (x == null) {
            x = new Node();
        }

        if (key == 0) {
            x.end = true;
        } else {
            int dig = key % 10;
            x.next[dig] = add(x.next[dig], key / 10);
        }

        return x;
    }

    private boolean contains(Node x, int key) {
        if (x == null) {
            return false;
        } else if (key == 0) {
            return x.end;
        } else {
            return contains(x.next[key % 10], key / 10);
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
 * Your MyHashSet object will be instantiated and called as such:
 * MyHashSet obj = new MyHashSet();
 * obj.add(key);
 * obj.remove(key);
 * boolean param_3 = obj.contains(key);
 */