// 429. N-ary Tree Level Order Traversal

// Runtime: 26 ms, faster than 83.72% of C++ online submissions for N-ary Tree Level Order Traversal.

// Memory Usage: 11.8 MB, less than 32.74% of C++ online submissions for N-ary Tree Level Order Traversal.


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
        levelOrder(root, 0);
        return vals_;
    }

private:
    void levelOrder(Node* node, int level) {
        if (!node) {
            return;
        }

        if (vals_.size() == level) {
            vals_.push_back({});
        }

        vals_[level].push_back(node->val);
        for (const auto child : node->children) {
            levelOrder(child, level + 1);
        }
    }

    vector<vector<int>> vals_;
};