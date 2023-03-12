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
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    
    TreeNode* getTree(int low, int high, vector<ListNode*> list){
        if(low > high){
            return nullptr;
        }
        int mid = (high+low)/2;
        TreeNode* current = new TreeNode(list[mid]->val);
        current->left = getTree(low, mid-1,list);
        current->right = getTree(mid+1,high,list);
        return current;
        
    }
    TreeNode* sortedListToBST(ListNode* head) {
        ListNode* current = head;
        vector<ListNode*> list;
        while(current != nullptr){
            list.push_back(current);
            current = current->next;
        }
        return getTree(0,list.size()-1,list);
        
        
    }
};