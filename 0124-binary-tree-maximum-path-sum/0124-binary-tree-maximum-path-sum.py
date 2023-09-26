# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        result = [float("-infinity")]

        def dfs(current):
            if not current:
                return 0
            
            leftSum = dfs(current.left)
            rightSum = dfs(current.right)

            localMax = max(current.val, leftSum+rightSum+current.val, leftSum+current.val, rightSum+current.val)
            result[0] = max(result[0], localMax)

            return max(leftSum+current.val, rightSum+current.val, current.val)
        dfs(root)
        return result[0]
        
        