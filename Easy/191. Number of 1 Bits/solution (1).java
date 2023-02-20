// 191. Number of 1 Bits

// Runtime: 1 ms, faster than 26.03% of Java online submissions for Number of 1 Bits.

// Memory Usage: 38.7 MB, less than 5.08% of Java online submissions for Number of 1 Bits.


public class Solution {
    // you need to treat n as an unsigned value

    // Loop and Flip
    public int hammingWeight(int n) {
        int bits = 0;
        int mask = 1;
        for (int i = 0; i < 32; i++) {
            if ((n & mask) != 0) {
                bits++;
            }

            mask <<= 1;
        }

        return bits;
    }
}