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
    bool isSymmetric(TreeNode* left, TreeNode* right){
        if(!left && !right)
            return true;
        if(left && !right)
            return false;
        if(right && !left)
            return false;
        return left->val == right->val && isSymmetric(left->left,right->right) && isSymmetric(left->right, right->left);
    }
    bool isSymmetric(TreeNode* root) {
        if(!root ||( !root->left && !root->right))
            return true;
        return isSymmetric(root->left,root->right);
        //Iterative solution using queues
        // if(!root ||( !root->left && !root->right))
        //     return true;
        // queue<TreeNode*> lQueue, rQueue;
        // lQueue.push(root->left);
        // rQueue.push(root->right);
        // while(!lQueue.empty() && !rQueue.empty()){
        //     TreeNode* left = lQueue.front();
        //     lQueue.pop();
        //     TreeNode* right = rQueue.front();
        //     rQueue.pop();
        //     if(!left || !right)
        //         return false;
        //     if(left->val != right->val)
        //         return false;
        //     if(left->left && right->right){
        //         lQueue.push(left->left);
        //         rQueue.push(right->right);
        //     }
        //     else if((left->left && !right->right) || (!left->left && right->right))
        //         return false;
                
        //     if(left->right && right->left){
        //         lQueue.push(left->right);
        //         rQueue.push(right->left);
        //     }
        //     else if((left->right && !right->left) || (!left->right && right->left))
        //         return false;
                
        // }
        // return true;
        
    }
};