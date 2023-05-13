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
    int diameterHelper(TreeNode* root, int& maxDiameter){
        if(root == nullptr)
            return 0;
        if(!root->left && !root->right)
            return 1;
        int leftHeight = 0;
        int rightHeight = 0;
        if(root->left)
            leftHeight = diameterHelper(root->left,maxDiameter);
        if(root->right)
            rightHeight = diameterHelper(root->right,maxDiameter);
        int rootDiameter = leftHeight+rightHeight;
        maxDiameter = max(maxDiameter,rootDiameter);
        return (max(leftHeight,rightHeight)+1);
    }
    int diameterOfBinaryTree(TreeNode* root) {
        int num = 0;
        diameterHelper(root,num);
        return num;
        
    }
};