// 100. Same Tree

// Runtime: 0 ms, faster than 100.00% of Java online submissions for Same Tree.

// Memory Usage: 36.7 MB, less than 5.75% of Java online submissions for Same Tree.


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
    // Iteration
    public boolean isSameTree(TreeNode p, TreeNode q) {
        if (p == null && q == null) {
            return true;
        } else if (!check(p, q)) {
            return false;
        }

        // Init deques
        ArrayDeque<TreeNode> deqP = new ArrayDeque<TreeNode>();
        ArrayDeque<TreeNode> deqQ = new ArrayDeque<TreeNode>();
        deqP.addLast(p);
        deqQ.addLast(q);

        while (!deqP.isEmpty()) {
            p = deqP.removeFirst();
            q = deqQ.removeFirst();

            if (!check(p, q)) {
                return false;
            }

            if (p != null) {
                // In Java nulls are not allowed in Deque
                if (!check(p.left, q.left)) {
                    return false;
                }

                if (p.left != null) {
                    deqP.addLast(p.left);
                    deqQ.addLast(q.left);
                }

                if (!check(p.right, q.right)) {
                    return false;
                }

                if (p.right != null) {
                    deqP.addLast(p.right);
                    deqQ.addLast(q.right);
                }
            }
        }

        return true;
    }

    public static boolean check(TreeNode p, TreeNode q) {
        if (p == null && q == null) {
            return true;
        } else if (q == null || p == null) {
            return false;
        } else if (p.val != q.val) {
            return false;
        } else {
            return true;
        }
    }
}