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
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        bool merged = false;
        ListNode* newHead = new ListNode(-1);
        ListNode* currentNew = newHead;
        do{
            merged = false;
            ListNode* current = nullptr;
            int index = -1;
            
            for(int i=0;i<lists.size();i++){
                if(lists[i] != nullptr && (current == nullptr || lists[i]->val < current->val) ){
                    current = lists[i];
                    index = i;
                    merged = true;
                }
            }
            
            if(current != nullptr){
                currentNew->next = new ListNode(current->val);
                currentNew = currentNew->next;
                lists[index] = current->next;
            }
            
        }while(merged != false);
            
        return newHead->next;
        
        
    }
};