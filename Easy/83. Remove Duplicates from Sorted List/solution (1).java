// 83. Remove Duplicates from Sorted List

// Runtime: 1 ms, faster than 15.73% of Java online submissions for Remove Duplicates from Sorted List.

// Memory Usage: 42.2 MB, less than 7.14% of Java online submissions for Remove Duplicates from Sorted List.


/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    // Straight-Forward Approach
    public ListNode deleteDuplicates(ListNode head) {
        ListNode current = head;
        // All nodes in the list up to the pointer `current` do not contain duplicate elements.
        while (current != null && current.next != null) {
            if (current.next.val == current.val) {
                current.next = current.next.next;
            } else {
                current = current.next;
            }
        }

        return head;
    }
}