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
    vector<int> data;
    Solution(ListNode* head) {
        srand(time(NULL));
        while(head != nullptr){
            data.push_back(head->val);
            head = head->next;
        }
        
    }
    
    int getRandom() {
        int index = rand()%data.size();
        return data[index];
        
    }
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution* obj = new Solution(head);
 * int param_1 = obj->getRandom();
 */