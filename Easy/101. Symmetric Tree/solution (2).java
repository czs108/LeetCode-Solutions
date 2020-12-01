// 101. Symmetric Tree

// Runtime: 1 ms, faster than 24.80% of Java online submissions for Symmetric Tree.

// Memory Usage: 39.2 MB, less than 33.33% of Java online submissions for Symmetric Tree.


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
    // Iterative
    public boolean isSymmetric(TreeNode root) {
        // Each two consecutive nodes in the queue should be equal.
        Queue<TreeNode> q = new LinkedList<>();
        q.add(root);
        q.add(root);

        // The algorithm works similarly to BFS, with some key differences.
        while (!q.isEmpty()) {
            // Each time, two nodes are extracted and their values compared.
            // Then, the right and left children of the two nodes are inserted in the queue in opposite order.
            TreeNode t1 = q.poll();
            TreeNode t2 = q.poll();

            if (t1 == null && t2 == null) {
                continue;
            } else if (t1 == null || t2 == null) {
                return false;
            } else if (t1.val != t2.val) {
                return false;
            } else {
                q.add(t1.left);
                q.add(t2.right);
                q.add(t1.right);
                q.add(t2.left);
            }
        }

        return true;
    }
}