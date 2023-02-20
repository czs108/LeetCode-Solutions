// 160. Intersection of Two Linked Lists

// Runtime: 1 ms, faster than 98.82% of Java online submissions for Intersection of Two Linked Lists.

// Memory Usage: 42.4 MB, less than 5.71% of Java online submissions for Intersection of Two Linked Lists.


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
    // Two Pointers
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        // When `pA` reaches the end of a list, then redirect it to the head of B.
        // Similarly when `pB` reaches the end of a list, redirect it the head of A.
        // If at any point `pA` meets `pB`, then `pA` / `pB` is the intersection node.
        ListNode pA = headA, pB = headB;
        while (pA != pB) {
            // If two lists have intersection,
            // in the second iteration, `pA` and `pB` are guaranteed to reach the intersection node at the same time.
            pA = (pA != null) ? pA.next : headB;
            pB = (pB != null) ? pB.next : headA;
        }

        return pA;
    }
}