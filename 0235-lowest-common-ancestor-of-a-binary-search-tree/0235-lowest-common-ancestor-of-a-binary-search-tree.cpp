/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

class Solution {
public:
    void LCAHelper(TreeNode* root, TreeNode* p, TreeNode* q, TreeNode**ans){
        if(!root)
            return ;
        //if root's value is less than both p's value and q's value, our answer will be in right subtree
        if(root->val < p->val && root->val < q->val){
            LCAHelper(root->right,p,q,ans);
        }
       
        //if root's value is greater than both p's value and q's value, our answer will be in left subtree
        if(root->val > p->val && root->val > q->val){
            LCAHelper(root->left,p,q,ans);
        }
        
        //if p is in left subtree of root and q is right subtree or q is in left subtree and p is in right subtree return make answer to be root
        if( (p->val <= root->val && q->val >= root->val) || (q->val <= root->val && p->val >= root->val) ){
            *ans = root;
        }
    }
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        TreeNode* ans = root;
        LCAHelper(root,p,q,&ans);
        return ans;
        
    }
};