// 100. Same Tree

// Runtime: 0 ms, faster than 100.00% of Java online submissions for Same Tree.

// Memory Usage: 36.5 MB, less than 5.75% of Java online submissions for Same Tree.


/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    // Recursion
    public boolean isSameTree(TreeNode p, TreeNode q) {
        // `p` and `q` are both null
        if (p == null && q == null) {
            return true;
        } else if (q == null || p == null) {
            return false;
        } else if (p.val != q.val) {
            return false;
        } else {
            return isSameTree(p.right, q.right) &&
                    isSameTree(p.left, q.left);
        }
    }
}