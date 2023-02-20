// 151. Reverse Words in a String

// Runtime: 11 ms, faster than 54.87% of C++ online submissions for Reverse Words in a String.

// Memory Usage: 7 MB, less than 91.51% of C++ online submissions for Reverse Words in a String.


class Solution {
public:
    string reverseWords(string s) {
        reverse(s.begin(), s.end());

        int newStart = 0;
        for (int i = 0; i < s.size(); ++i) {
            if (s[i] != ' ') {
                // Go to the beginning of the word.
                if (newStart != 0) {
                    s[newStart++] = ' ';
                }

                // Go to the end of the word.
                int end = i;
                while (end != s.size() && s[end] != ' ') {
                    s[newStart++] = s[end++];
                }

                // Reverse the word.
                int len = end - i;
                reverse(s.begin() + newStart - len, s.begin() + newStart);

                // Move to the next word.
                i = end;
            }
        }

        s.erase(s.begin() + newStart, s.end());
        return s;
    }
};