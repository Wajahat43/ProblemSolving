# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #for any node we need to have all values of path from root
    #to that node smaller than or equal to value of this node.
    #if we keep track of maximum value in the path so far, we can see if 
    #that node is  part of our solution or not.
    def dfs(self,root,maxVal):
        if root == None:
            return 0
        #update max value
        maxVal =max(root.val,maxVal)
        count = 0
        #if root should be part of our solution
        if root.val >= maxVal:
            count += 1
        #get solution of left and right subtree
        count += self.dfs(root.left,maxVal)
        count += self.dfs(root.right,maxVal)
        return count
        
    def goodNodes(self, root: TreeNode) -> int:
        return self.dfs(root,float("-inf"))
        