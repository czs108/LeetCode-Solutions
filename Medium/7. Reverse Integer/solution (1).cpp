// 7. Reverse Integer

// Runtime: 4 ms, faster than 54.26% of C++ online submissions for Reverse Integer.

// Memory Usage: 6 MB, less than 100.00% of C++ online submissions for Reverse Integer.


class Solution {
public:
    int reverse(int x) {
        int rev = 0;
        while (x != 0) {
            int pop = x % 10;
            x /= 10;

            // Check overflow
            if (rev > INT_MAX / 10 || (rev == INT_MAX / 10 && pop > INT_MAX % 10)) {
                return 0;
            }

            // Check underflow
            if (rev < INT_MIN / 10 || (rev == INT_MIN / 10 && pop < INT_MIN % 10)) {
                return 0;
            }

            rev = rev * 10 + pop;
        }

        return rev;
    }
};