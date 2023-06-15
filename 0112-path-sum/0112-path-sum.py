# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        
        def dfs(current, currentSum):
            if current == None:
                return False
            
            currentSum += current.val;
            if current.left == None and current.right == None:
                return currentSum == targetSum
            
            if dfs(current.left, currentSum) == True:
                return True
            elif dfs(current.right,currentSum) == True:
                return True
        
        return dfs(root,0)
            
            
        