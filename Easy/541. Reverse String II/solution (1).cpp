// 541. Reverse String II

// Runtime: 7 ms, faster than 69.64% of C++ online submissions for Reverse String II.

// Memory Usage: 7.2 MB, less than 70.31% of C++ online submissions for Reverse String II.


class Solution {
public:
    string reverseStr(string s, int k) {
        for (int i = 0; i < s.size(); i += 2 * k) {
            reverse(s.begin() + i, min(s.begin() + i + k, s.end()));
        }

        return s;
    }
};