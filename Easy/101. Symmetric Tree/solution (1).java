// 101. Symmetric Tree

// Runtime: 0 ms, faster than 100.00% of Java online submissions for Symmetric Tree.

// Memory Usage: 37.8 MB, less than 72.11% of Java online submissions for Symmetric Tree.


/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    // Recursive
    public boolean isSymmetric(TreeNode root) {
        return isMirror(root, root);
    }

    public static boolean isMirror(TreeNode t1, TreeNode t2) {
        if (t1 == null && t2 == null) {
             return true;
        } else if (t1 == null || t2 == null) {
            return false;
        } else {
            return t1.val == t2.val
                && isMirror(t1.right, t2.left)
                && isMirror(t1.left, t2.right);
        }
    }
}