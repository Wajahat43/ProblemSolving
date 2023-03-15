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

    //get max level of tree
    int getMaxLevel(TreeNode* root) {
        if (!root)
            return 0;
        return max(getMaxLevel(root->left), getMaxLevel(root->right)) + 1;
    }

    bool isCompleteTree(TreeNode* root) {

        if(!root)
            return true;


        vector<int> values;
        queue<TreeNode*> q;
        q.push(root);
        
        int currentLevel = 0;
        int maxLevel = getMaxLevel(root) - 1;
        int currentLevelNodes = 0;
        //Do level order traversal of tree and store it in vector
        //if the nodes is not leaf node on last level, store both its children
        //store -1 in place of a null child
        while (q.empty() == false) {
            TreeNode* current = q.front();
            currentLevelNodes++;

   

            q.pop();
            if (current) {
                values.push_back(current->val);
            }
            else {
                values.push_back(-1);
            }
            if (current && (currentLevel != maxLevel))
            {
                q.push(current->left);
                q.push(current->right);
            }

             if(currentLevelNodes == pow(2,currentLevel)){
                currentLevel++;
                currentLevelNodes = 0;
            }

        }

        currentLevel = 0;
        currentLevelNodes = 0;
        
        //iterate over the vector representation of tree
        for (int i = 0; i < values.size(); i++) {
            //if a null node is found and it is not on max level return false
            if (values[i] == -1 && currentLevel != maxLevel) {
                return false;
            }
            
            //if a null node is found on maxLevel make sure all the nodes towards its right
            //are null as well
            else if (values[i] == -1 && currentLevel == maxLevel) {
                for (int j = i; j < values.size(); j++) {
                    if (values[j] != -1) {
                        return false;
                    }
                }
                return true;
            }
            else
                currentLevelNodes++;


            if (currentLevelNodes == pow(2, currentLevel)) {
                currentLevelNodes = 0;
                currentLevel++;
            }
        }
        return true;


    }
};