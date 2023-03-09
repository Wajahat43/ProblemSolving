/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *detectCycle(ListNode *head) {
        
         if(head == NULL || head->next == NULL)
            return NULL;
        ListNode* turtoise= head;
        ListNode* hare= head;
        do{
            if(hare->next == NULL || hare->next->next == NULL)
                return NULL;
            else{
                hare = hare->next->next;
                turtoise = turtoise ->next;
            }
        } while(turtoise != hare);
        turtoise = head;
        while(turtoise != hare){
            turtoise = turtoise ->next;
            hare = hare->next;
        }
        return hare;
    }
};