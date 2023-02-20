// 460. LFU Cache

// Runtime: 71 ms, faster than 36.22% of Java online submissions for LFU Cache.

// Memory Usage: 122.6 MB, less than 63.03% of Java online submissions for LFU Cache.


class LFUCache {

    private int minFreq = 0;

    private int cap = 0;

    private HashMap<Integer, Integer> keyToVal = new HashMap<Integer, Integer>();

    private HashMap<Integer, Integer> keyToFreq = new HashMap<Integer, Integer>();

    private HashMap<Integer, LinkedHashSet<Integer>> freqToKeys = new HashMap<Integer, LinkedHashSet<Integer>>();

    public LFUCache(int capacity) {
        cap = capacity;
    }

    public int get(int key) {
        if (!keyToVal.containsKey(key)) {
            return -1;
        } else {
            increaseFreq(key);
            return keyToVal.get(key);
        }
    }

    public void put(int key, int value) {
        if (cap <= 0) {
            return;
        } else if (keyToVal.containsKey(key)) {
            keyToVal.put(key, value);
            increaseFreq(key);
            return;
        }

        if (cap <= keyToVal.size()) {
            removeMinFreq();
        }

        keyToVal.put(key, value);
        keyToFreq.put(key, 1);
        freqToKeys.putIfAbsent(1, new LinkedHashSet<Integer>());
        freqToKeys.get(1).add(key);
        minFreq = 1;
    }

    private void increaseFreq(int key) {
        int freq = keyToFreq.get(key);
        keyToFreq.put(key, freq + 1);

        freqToKeys.get(freq).remove(key);
        freqToKeys.putIfAbsent(freq + 1, new LinkedHashSet<Integer>());
        freqToKeys.get(freq + 1).add(key);

        if (freqToKeys.get(freq).isEmpty()) {
            freqToKeys.remove(freq);
            if (freq == minFreq) {
                minFreq++;
            }
        }
    }

    private void removeMinFreq() {
        LinkedHashSet<Integer> keys = freqToKeys.get(minFreq);
        int delKey = keys.iterator().next();
        keys.remove(delKey);
        if (keys.isEmpty()) {
            freqToKeys.remove(minFreq);
            // No need to update `minFreq` because `put` will set `minFreq` to 1.
        }

        keyToFreq.remove(delKey);
        keyToVal.remove(delKey);
    }
}

/**
 * Your LFUCache object will be instantiated and called as such:
 * LFUCache obj = new LFUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */