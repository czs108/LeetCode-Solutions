// 2095. Delete the Middle Node of a Linked List

// Runtime: 2284 ms, faster than 9.54% of C++ online submissions for Delete the Middle Node of a Linked List.

// Memory Usage: 294.8 MB, less than 20.43% of C++ online submissions for Delete the Middle Node of a Linked List.


/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    // Two Pointers
    ListNode* deleteMiddle(ListNode* head) {
        ListNode *slow = head, *fast = head;
        ListNode* prev = nullptr;
        while (fast && fast->next) {
            prev = slow;
            fast = fast->next->next;
            slow = slow->next;
        }

        if (!prev) {
            return nullptr;
        } else {
            prev->next = slow->next;
            return head;
        }
    }
};