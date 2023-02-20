// 286. Walls and Gates

// Runtime: 88 ms, faster than 29.83% of C++ online submissions for Walls and Gates.

// Memory Usage: 17.4 MB, less than 36.81% of C++ online submissions for Walls and Gates.


class Solution {
    static constexpr int GATE {0};
    static constexpr int WALL {-1};
    static constexpr int INF {2147483647};

public:
    void wallsAndGates(vector<vector<int>>& rooms) {
        rooms_ = &rooms;
        width_ = rooms.size();
        height_ = rooms[0].size();

        int dist {0};
        queue<pair<int, int>> nodes {findGates()};
        while (!nodes.empty()) {
            const auto size {nodes.size()};
            for (auto i {0}; i != size; ++i) {
                const auto node {nodes.front()};
                const auto [x, y] {node};
                nodes.pop();

                if (rooms[x][y] == INF || rooms[x][y] == GATE) {
                    rooms[x][y] = dist;
                    for (auto neighbor : getNeighborRooms(node)) {
                        nodes.push(move(neighbor));
                    }
                }
            }

            ++dist;
        }
    }

private:
    queue<pair<int, int>> findGates() const {
        queue<pair<int, int>> gates;
        for (auto i {0}; i != width_; ++i) {
            for (auto j {0}; j != height_; ++j) {
                if ((*rooms_)[i][j] == GATE) {
                    gates.push({i, j});
                }
            }
        }

        return gates;
    }

    vector<pair<int, int>> getNeighborRooms(const pair<int, int>& pos) const {
        static const array<pair<int, int>, 4> dirs {
            {{-1, 0}, {1, 0}, {0, 1}, {0, -1}}};

        vector<pair<int, int>> neighbors;
        for (const auto& dir : dirs) {
            pair<int, int> neighbor {pos.first + dir.first,
                                     pos.second + dir.second};
            if (visitableRoom(neighbor)) {
                neighbors.push_back(move(neighbor));
            }
        }

        return neighbors;
    }

    bool visitableRoom(const pair<int, int>& pos) const {
        const auto [x, y] {pos};
        return (0 <= x && x < width_) && (0 <= y && y < height_)
               && (*rooms_)[x][y] == INF;
    }

    int width_;
    int height_;
    vector<vector<int>>* rooms_;
};