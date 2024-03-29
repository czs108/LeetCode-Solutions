// 147. Insertion Sort List


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
    ListNode* insertionSortList(ListNode* head) {
        ListNode dummy {};
        auto curr {head};
        while (curr) {
            auto prev {&dummy};
            while (prev->next && prev->next->val < curr->val) {
                prev = prev->next;
            }

            const auto next {curr->next};
            curr->next = prev->next;
            prev->next = curr;
            curr = next;
        }

        return dummy.next;
    }
};