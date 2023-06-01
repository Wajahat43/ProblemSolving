# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def dfs(self,currentNode,maxVal):
        if currentNode == None:
            return 0
        
        maxVal = max(maxVal, currentNode.val)
        
        count = 0
        if currentNode.val >= maxVal:
            count = 1
        
        count += self.dfs(currentNode.left,maxVal) 
        count += self.dfs(currentNode.right,maxVal) 
        
        return count 
        
    
    def goodNodes(self, root: TreeNode) -> int:
        return self.dfs(root,root.val)
        
        