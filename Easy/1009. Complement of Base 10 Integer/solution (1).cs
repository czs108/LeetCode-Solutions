// 1009. Complement of Base 10 Integer

// Runtime: 40 ms, faster than 72.25% of C# online submissions for Complement of Base 10 Integer.

// Memory Usage: 14.9 MB, less than 100.00% of C# online submissions for Complement of Base 10 Integer.


public class Solution {
    public int BitwiseComplement(int N) {
        if (N == 0) {
            return 1;
        } else if (N == 1) {
            return 0;
        }

        // Can NOT use `Convert.ToInt32`, it uses rounding rules.
        // `(int)` truncates the double to an integer.
        int exp = (int)Math.Log(N, 2);
        int mask = (int)Math.Pow(2, exp + 1) - 1;
        return N ^ mask;
    }
}