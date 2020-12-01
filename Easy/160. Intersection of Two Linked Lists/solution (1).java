// 160. Intersection of Two Linked Lists

// Runtime: 823 ms, faster than 5.00% of Java online submissions for Intersection of Two Linked Lists.

// Memory Usage: 42.3 MB, less than 5.71% of Java online submissions for Intersection of Two Linked Lists.


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
    // Brute Force
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        ListNode pA = headA;
        while (pA != null) {
            for (ListNode pB = headB; pB != null; pB = pB.next) {
                if (pA == pB) {
                    return pA;
                }
            }

            pA = pA.next;
        }

        return null;
    }
}