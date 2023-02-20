// 257. Binary Tree Paths

// Runtime: 7 ms, faster than 60.53% of C++ online submissions for Binary Tree Paths.

// Memory Usage: 12.6 MB, less than 89.77% of C++ online submissions for Binary Tree Paths.


/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<string> binaryTreePaths(TreeNode* root) {
        if (root) {
            dfs(root, "");
        }

        return paths_;
    }

private:
    void dfs(TreeNode* root, string path) {
        path += to_string(root->val);
        if (isLeaf(root)) {
            paths_.push_back(std::move(path));
        } else {
            path += "->";
            if (root->left) {
                dfs(root->left, path);
            }

            if (root->right) {
                dfs(root->right, path);
            }
        }
    }

    bool isLeaf(TreeNode* node) {
        return !node->left && !node->right;
    }

    vector<string> paths_;
};