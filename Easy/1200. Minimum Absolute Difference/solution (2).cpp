// 1200. Minimum Absolute Difference

// Runtime: 86 ms, faster than 82.79% of C++ online submissions for Minimum Absolute Difference.

// Memory Usage: 32.3 MB, less than 28.96% of C++ online submissions for Minimum Absolute Difference.


class Solution {
public:
    vector<vector<int>> minimumAbsDifference(vector<int>& arr) {
        sort(arr.begin(), arr.end());
        vector<vector<int>> res;

        int minDiff {numeric_limits<int>::max()};
        for (auto i {0}; i != arr.size() - 1; ++i) {
            const auto x {arr[i]}, y {arr[i + 1]};
            if (minDiff > y - x) {
                res.clear();
                minDiff = y - x;
            }

            if (minDiff == y - x) {
                res.push_back({x, y});
            }
        }

        return res;
    }
};