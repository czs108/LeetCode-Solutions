// 160. Intersection of Two Linked Lists

// Runtime: 7 ms, faster than 25.45% of Java online submissions for Intersection of Two Linked Lists.

// Memory Usage: 43.7 MB, less than 5.71% of Java online submissions for Intersection of Two Linked Lists.


/**
 * Definition for singly-linked list.
 * public class ListNode {
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
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        if (headA == null) {
            return null;
        }

        Set<ListNode> nodes = new HashSet<>();
        ListNode pA = headA;
        while (pA != null) {
            nodes.add(pA);
            pA = pA.next;
        }

        ListNode pB = headB;
        while (pB != null) {
            if (nodes.contains(pB)) {
                return pB;
            } else {
                pB = pB.next;
            }
        }

        return null;
    }
}