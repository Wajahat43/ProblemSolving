# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        res = []
        dp = {}

        def dfs(nodes):
            if nodes % 2 == 0:
                return []
            if nodes == 1:
                return [TreeNode()]
            if nodes in dp:
                return dp[nodes]
            current = []
            for i in range(nodes):
                left = dfs(i)
                right = dfs(nodes-i-1)

                for l in left:
                    for r in right:
                        current.append(TreeNode(0,l,r))
            dp[nodes] = current
            return dp[nodes]
        return dfs(n)