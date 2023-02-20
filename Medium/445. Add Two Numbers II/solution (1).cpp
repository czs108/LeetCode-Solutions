// 445. Add Two Numbers II


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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        l1 = reverse(l1);
        l2 = reverse(l2);

        ListNode* prev = nullptr;
        int carry = 0;
        while (l1 || l2) {
            int n1 = l1 ? l1->val : 0;
            int n2 = l2 ? l2->val : 0;
            int sum = n1 + n2 + carry;
            int val = sum % 10;
            carry = sum / 10;

            ListNode* curr = new ListNode(val);
            curr->next = prev;
            prev = curr;

            l1 = l1 ? l1->next : nullptr;
            l2 = l2 ? l2->next : nullptr;
        }

        if (carry) {
            ListNode* head = new ListNode(1);
            head->next = prev;
            return head;
        } else {
            return prev;
        }
    }

private:
    static ListNode* reverse(ListNode* node) {
        ListNode* prev = nullptr;
        ListNode* curr = node;
        while (curr) {
            auto next = curr->next;
            curr->next = prev;

            prev = curr;
            curr = next;
        }

        return prev;
    }
};