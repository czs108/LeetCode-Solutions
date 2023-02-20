// 186. Reverse Words in a String II

// Runtime: 58 ms, faster than 12.82% of C++ online submissions for Reverse Words in a String II.

// Memory Usage: 16.2 MB, less than 46.62% of C++ online submissions for Reverse Words in a String II.


class Solution {
public:
    void reverseWords(vector<char>& s) {
        reverse(s.begin(), s.end());

        for (int i = 0; i < s.size(); ++i) {
            int end = i;
            while (end != s.size() && s[end] != ' ') {
                ++end;
            }

            reverse(s.begin() + i, s.begin() + end);
            i = end;
        }
    }
};