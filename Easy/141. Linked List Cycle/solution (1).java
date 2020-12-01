// 141. Linked List Cycle

// Runtime: 3 ms, faster than 19.88% of Java online submissions for Linked List Cycle.

// Memory Usage: 39.9 MB, less than 5.71% of Java online submissions for Linked List Cycle.


/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    // Hash Table
    public boolean hasCycle(ListNode head) {
        Set<ListNode> nodesSeen = new HashSet<>();
        while (head != null) {
            if (nodesSeen.contains(head)) {
                return true;
            } else {
                nodesSeen.add(head);
            }

            head = head.next;
        }

        return false;
    }
}