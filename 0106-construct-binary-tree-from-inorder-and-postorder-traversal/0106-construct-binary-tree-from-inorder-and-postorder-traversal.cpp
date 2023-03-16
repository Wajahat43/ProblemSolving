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
    TreeNode* helper(vector<int>& inorder, vector<int>& postorder, map<int,int>& m,
                     int l, int r){
        if(l>r){
            return nullptr;
        }
        TreeNode* root = new TreeNode(postorder.back());
        postorder.pop_back();
        int ind = m[root->val];
        root->right = helper(inorder,postorder,m,ind+1,r);
        root->left = helper(inorder,postorder,m,l,ind-1);
        return root;
        
        
    }
    TreeNode* buildTree(vector<int>& inorder, vector<int>& postorder) {
        map<int,int> m;
        for(int i=0;i<inorder.size();i++){
            m.insert({inorder[i],i});
        }
        return helper(inorder,postorder,m,0,inorder.size()-1);
        
    }
};