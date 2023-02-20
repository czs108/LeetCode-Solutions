// 1328. Break a Palindrome

// Runtime: 4 ms, faster than 30.34% of C++ online submissions for Break a Palindrome.

// Memory Usage: 6.3 MB, less than 45.46% of C++ online submissions for Break a Palindrome.


class Solution {
public:
    string breakPalindrome(string palindrome) {
        if (palindrome.size() <= 1) {
            return "";
        }

        for (int i = 0; i < palindrome.size() / 2; ++i) {
            if (palindrome[i] > 'a') {
                palindrome[i] = 'a';
                return palindrome;
            }
        }

        palindrome[palindrome.size() - 1] = 'b';
        return palindrome;
    }
};