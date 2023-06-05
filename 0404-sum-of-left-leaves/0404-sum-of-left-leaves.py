# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self,current,parent):
        if current == None:
            return 0
        if current.left == None and current.right == None:
            if parent and parent.left == current:
                return current.val
            return 0
        return self.dfs(current.left,current) + self.dfs(current.right,current)
            
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root,None)
        