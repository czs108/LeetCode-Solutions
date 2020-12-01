// 278. First Bad Version

// Runtime: 12 ms, faster than 97.96% of Java online submissions for First Bad Version.

// Memory Usage: 35.6 MB, less than 79.60% of Java online submissions for First Bad Version.


/*
The isBadVersion API is defined in the parent class VersionControl.
    boolean isBadVersion(int version);
*/

public class Solution extends VersionControl {
    // Binary Search
    public int firstBadVersion(int n) {
        int left = 1, right = n;
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (isBadVersion(mid)) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }

        return left;
    }
}