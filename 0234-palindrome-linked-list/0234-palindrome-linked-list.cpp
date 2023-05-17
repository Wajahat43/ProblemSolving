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
    bool isPalindrome(ListNode** first, ListNode* last){
        //if we have reached end of list return true
        if(!last)
            return true;
        //get result by moving last to next
        bool result = isPalindrome(first,last->next);
        //compare result and also the values of first and last node in current function call
        if((*first)->val == last->val && result){
            (*first) = (*first)->next;
            return true;
        }
            
        return false;
    }
    bool isPalindrome(ListNode* head) {
        return isPalindrome(&head,head);
    }
};