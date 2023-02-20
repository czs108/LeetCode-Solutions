// 173. Binary Search Tree Iterator


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
class BSTIterator {
public:
    BSTIterator(TreeNode* root) {
        getLeftmost(root);
    }

    int next() {
        auto node = vals_.top();
        vals_.pop();
        getLeftmost(node->right);
        return node->val;
    }

    bool hasNext() {
        return !vals_.empty();
    }

private:
    stack<TreeNode*> vals_;

    void getLeftmost(TreeNode* node) {
        while (node) {
            vals_.push(node);
            node = node->left;
        }
    }
};

/**
 * Your BSTIterator object will be instantiated and called as such:
 * BSTIterator* obj = new BSTIterator(root);
 * int param_1 = obj->next();
 * bool param_2 = obj->hasNext();
 */