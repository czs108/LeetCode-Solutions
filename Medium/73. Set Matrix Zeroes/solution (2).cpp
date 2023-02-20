// 73. Set Matrix Zeroes

// Runtime: 24 ms, faster than 64.16% of C++ online submissions for Set Matrix Zeroes.

// Memory Usage: 13.2 MB, less than 54.78% of C++ online submissions for Set Matrix Zeroes.


class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        unordered_set<int> cols, rows;
        for (int row = 0; row != matrix.size(); ++row) {
            for (int col = 0; col != matrix[0].size(); ++col) {
                if (matrix[row][col] == 0) {
                    rows.insert(row);
                    cols.insert(col);
                }
            }
        }

        for (int row = 0; row != matrix.size(); ++row) {
            for (int col = 0; col != matrix[0].size(); ++col) {
                if (rows.find(row) != rows.end()
                    || cols.find(col) != cols.end()) {
                    matrix[row][col] = 0;
                }
            }
        }
    }
};