// 429. N-ary Tree Level Order Traversal

// Runtime: 51 ms, faster than 13.38% of C++ online submissions for N-ary Tree Level Order Traversal.

// Memory Usage: 11.7 MB, less than 85.92% of C++ online submissions for N-ary Tree Level Order Traversal.


/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> children;

    Node() {}

    Node(int _val) {
        val = _val;
    }

    Node(int _val, vector<Node*> _children) {
        val = _val;
        children = _children;
    }
};
*/

class Solution {
public:
    vector<vector<int>> levelOrder(Node* root) {
        if (!root) {
            return {};
        }

        vector<vector<int>> vals;
        queue<Node*> nodes;
        nodes.push(root);
        while (!nodes.empty()) {
            vector<int> curr_lvl_vals;
            const auto size {nodes.size()};
            for (auto i {0}; i != size; ++i) {
                const auto node {nodes.front()};
                nodes.pop();
                curr_lvl_vals.push_back(node->val);
                for (const auto child : node->children) {
                    nodes.push(child);
                }
            }

            vals.push_back(move(curr_lvl_vals));
        }

        return vals;
    }
};