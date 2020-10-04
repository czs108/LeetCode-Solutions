// 191. Number of 1 Bits

// Runtime: 0 ms, faster than 100.00% of Java online submissions for Number of 1 Bits.

// Memory Usage: 36.6 MB, less than 36.66% of Java online submissions for Number of 1 Bits.


public class Solution {
    // you need to treat n as an unsigned value

    // Bit Manipulation Trick
    public int hammingWeight(int n) {
        int bits = 0;
        while (n != 0) {
            bits++;
            n &= (n - 1);
        }

        return bits;
    }
}