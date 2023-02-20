// 1091. Shortest Path in Binary Matrix


class Solution {
public:
    int shortestPathBinaryMatrix(vector<vector<int>>& grid) {
        grid_ = &grid;
        width_ = grid.size();
        height_ = grid[0].size();
        if (!visitablePosition({0, 0})
            || !visitablePosition({width_ - 1, height_ - 1})) {
            return -1;
        }

        int len {1};
        set<pair<int, int>> visited;
        queue<pair<int, int>> nodes;

        nodes.push({0, 0});
        visited.insert({0, 0});
        while (!nodes.empty()) {
            const auto size {nodes.size()};
            for (auto i {0}; i != size; ++i) {
                const auto pos {nodes.front()};
                nodes.pop();
                if (pos == pair<int, int> {width_ - 1, height_ - 1}) {
                    return len;
                }

                for (auto neighbor : getNeighbors(pos)) {
                    if (!visited.count(neighbor)) {
                        visited.insert(neighbor);
                        nodes.push(move(neighbor));
                    }
                }
            }

            ++len;
        }

        return -1;
    }

    vector<pair<int, int>> getNeighbors(const pair<int, int>& pos) {
        static const array<pair<int, int>, 8> dirs {{{-1, -1},
                                                     {-1, 0},
                                                     {-1, 1},
                                                     {0, -1},
                                                     {0, 1},
                                                     {1, -1},
                                                     {1, 0},
                                                     {1, 1}}};

        vector<pair<int, int>> neighbors;
        for (const auto& dir : dirs) {
            pair<int, int> neighbor {pos.first + dir.first,
                                     pos.second + dir.second};
            if (visitablePosition(neighbor)) {
                neighbors.push_back(move(neighbor));
            }
        }

        return neighbors;
    }

    bool visitablePosition(const pair<int, int>& pos) {
        const auto [x, y] {pos};
        return (0 <= x && x < width_) && (0 <= y && y < height_)
               && (*grid_)[x][y] == 0;
    }

private:
    int width_;
    int height_;
    vector<vector<int>>* grid_;
};