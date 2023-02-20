// 994. Rotting Oranges


class Solution {
    static constexpr auto FRESH {1};
    static constexpr auto ROTTEN {2};

public:
    int orangesRotting(vector<vector<int>>& grid) {
        grid_ = &grid;
        width_ = grid.size();
        height_ = grid[0].size();

        queue<pair<int, int>> rotten;
        int freshCount {0};
        for (auto i {0}; i != width_; ++i) {
            for (auto j {0}; j != height_; ++j) {
                const auto type {grid[i][j]};
                if (type == FRESH) {
                    ++freshCount;
                } else if (type == ROTTEN) {
                    rotten.push({i, j});
                }
            }
        }

        int time {0};
        while (freshCount && !rotten.empty()) {
            const auto size {rotten.size()};
            for (auto i {0}; i != size; ++i) {
                const auto pos {rotten.front()};
                rotten.pop();
                for (auto neighbor : getNeighbors(pos)) {
                    --freshCount;
                    const auto [x, y] {neighbor};
                    grid[x][y] = ROTTEN;
                    rotten.push(move(neighbor));
                }
            }

            ++time;
        }

        return !freshCount ? time : -1;
    }

private:
    vector<pair<int, int>> getNeighbors(const pair<int, int>& pos) const {
        static const array<pair<int, int>, 4> dirs {
            {{-1, 0}, {1, 0}, {0, 1}, {0, -1}}};

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

    bool visitablePosition(const pair<int, int>& pos) const {
        const auto [x, y] {pos};
        return (0 <= x && x < width_) && (0 <= y && y < height_)
               && (*grid_)[x][y] == FRESH;
    }

    vector<vector<int>>* grid_;
    int width_;
    int height_;
};