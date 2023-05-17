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
    
    ListNode* reverse(ListNode* head){
        if(!head->next)
            return head;
        ListNode* prev = head;
        ListNode* next = head->next;
        while(next){
            ListNode* temp = next->next;
            next->next = prev;
            prev = next;
            next = temp;
        }
        return prev;
    }
    int pairSum(ListNode* head) {
        ListNode* slow = head;
        ListNode* fast = head->next->next;
        
        while(fast){
            slow = slow->next;
            fast = fast->next->next;
        }
        
        fast = slow->next;
        slow->next = nullptr;
        slow = reverse(head);
        
        int maxSum = 0;
        while(fast){
            maxSum = max(maxSum,slow->val+fast->val);
            slow = slow->next;
            fast = fast->next;
        }
        return maxSum;
        
    }
};