// 217. Contains Duplicate

// Runtime: 6 ms, faster than 58.16% of Java online submissions for Contains Duplicate.

// Memory Usage: 46.2 MB, less than 5.17% of Java online submissions for Contains Duplicate.


class Solution {
    // Hash Table
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> set = new HashSet<>(nums.length);
        for (int x : nums) {
            if (set.contains(x)) {
                return true;
            } else {
                set.add(x);
            }
        }

        return false;
    }
}