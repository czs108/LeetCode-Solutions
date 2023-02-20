// 2095. Delete the Middle Node of a Linked List

// Runtime: 2296 ms, faster than 8.52% of C++ online submissions for Delete the Middle Node of a Linked List.

// Memory Usage: 294.7 MB, less than 88.03% of C++ online submissions for Delete the Middle Node of a Linked List.


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
        if (!head->next) {
            return nullptr;
        }

        ListNode *slow = head, *fast = head->next->next;
        while (fast && fast->next) {
            fast = fast->next->next;
            slow = slow->next;
        }

        slow->next = slow->next->next;
        return head;
    }
};