// 752. Open the Lock


class Solution {
public:
    // Breadth-First Search
    int openLock(vector<string>& deadends, string target) {
        initDeadendSet(deadends);

        queue<string> nodes;
        set<string> seen;
        nodes.push("0000");
        seen.insert("0000");

        int dist {0};
        while (!nodes.empty()) {
            const auto size {nodes.size()};
            for (auto i {0}; i != size; ++i) {
                const auto node {nodes.front()};
                nodes.pop();
                if (node == target) {
                    return dist;
                } else if (isDeadend(node)) {
                    continue;
                } else {
                    for (auto neighbor : getNeighbors(node)) {
                        if (!seen.count(neighbor)) {
                            seen.insert(neighbor);
                            nodes.push(move(neighbor));
                        }
                    }
                }
            }

            ++dist;
        }

        return -1;
    }

private:
    bool isDeadend(const string& lock) const {
        return deadends_.count(lock) != 0;
    }

    void initDeadendSet(const vector<string>& deadends) {
        for (auto deadend : deadends) {
            deadends_.insert(move(deadend));
        }
    }

    vector<string> getNeighbors(const string& lock) const {
        vector<string> neighbors;
        for (auto i {0}; i != lock.size(); ++i) {
            for (const auto dir : {1, -1}) {
                auto neighbor {lock};
                neighbor[i] = (neighbor[i] - '0' + dir + 10) % 10 + '0';
                if (!isDeadend(neighbor)) {
                    neighbors.push_back(move(neighbor));
                }
            }
        }

        return neighbors;
    }

    set<string> deadends_;
};