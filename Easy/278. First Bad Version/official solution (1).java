// 278. First Bad Version

/*
The isBadVersion API is defined in the parent class VersionControl.
    boolean isBadVersion(int version);
*/

public class Solution extends VersionControl {
    // Linear Scan
    public int firstBadVersion(int n) {
        for (int i = 1; i < n; i++) {
            if (isBadVersion(i)) {
                return i;
            }
        }

        return n;
    }
}