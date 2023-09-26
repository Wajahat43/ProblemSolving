# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #For any node if we know the sum from root to that node
    #And we subtract targetSum from sum, we will know that we have made target sum. Now we need to find 
    #out how many times result of this subtractin occured in path.
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        cache = defaultdict(int)
        def dfs(current, sum):
            if not current:
                return 0
            sum += current.val
            if sum == targetSum:
                result = 1
            else:
                result = 0

            #Finding paths before it
            requiredSum = sum-targetSum
            result += cache[requiredSum]
            cache[sum] += 1
            
            result += dfs(current.left, sum)
            result += dfs(current.right, sum)
            cache[sum] -= 1
            return result

        return dfs(root,0)
        