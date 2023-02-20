// 279. Perfect Squares

// Runtime: 267 ms, faster than 57.02% of C++ online submissions for Perfect Squares.

// Memory Usage: 33.7 MB, less than 14.65% of C++ online submissions for Perfect Squares.


class Solution {
public:
    // Breadth-First Search
    int numSquares(int n) {
        const auto squareNums {getSquareNums(n)};
        set<int> nodes;
        nodes.insert(n);

        int count {1};
        while (!nodes.empty()) {
            set<int> nextNodes;
            for (const auto remain : nodes) {
                for (const auto square : squareNums) {
                    if (remain == square) {
                        return count;
                    } else if (remain >= square) {
                        nextNodes.insert(remain - square);
                    }
                }
            }

            ++count;
            nodes = nextNodes;
        }

        return count;
    }

private:
    static vector<int> getSquareNums(const int n) {
        vector<int> nums;
        for (int i {1}; i < (int)pow(n, 0.5) + 1; ++i) {
            nums.push_back(i * i);
        }

        return nums;
    }
};