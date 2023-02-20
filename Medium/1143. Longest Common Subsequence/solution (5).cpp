// 1143. Longest Common Subsequence

// Runtime: 32 ms, faster than 65.70% of C++ online submissions for Longest Common Subsequence.

// Memory Usage: 12.9 MB, less than 59.21% of C++ online submissions for Longest Common Subsequence.


class Solution {
public:
    int longestCommonSubsequence(string text1, string text2) {
        vector<vector<int>> lens(text1.size() + 1,
                                 vector<int>(text2.size() + 1));

        for (int i = 1; i <= text1.size(); ++i) {
            for (int j = 1; j <= text2.size(); ++j) {
                if (text1[i - 1] == text2[j - 1]) {
                    lens[i][j] = lens[i - 1][j - 1] + 1;
                } else {
                    lens[i][j] = max(lens[i][j - 1], lens[i - 1][j]);
                }
            }
        }

        return lens.back().back();
    }
};