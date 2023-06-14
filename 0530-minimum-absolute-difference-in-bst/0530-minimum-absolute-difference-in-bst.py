# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        res = float("inf")
        prev = float("inf")
        def dfs(current):
            nonlocal res,prev
            if current == None:
                return
            
            dfs(current.left)
            res = min(res,math.fabs(current.val-prev))
            prev = current.val
            dfs(current.right)

        dfs(root)
        return int(res)
            