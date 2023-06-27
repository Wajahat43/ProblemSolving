class Solution:
    #This is another classic dp problem.
    #I started out at each position we have the choice to add that number or subtract that number. Used memoization to avoid solving same problems twice.
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        dp = {}

        def dfs(i, sum):
            if i >= len(nums) and sum == target:
                return 1
            if i >=len(nums) and sum != target:
                return 0
            if (i,sum) in dp:
                return dp[(i,sum)]
            
            dp[(i,sum)] = dfs(i+1, sum + nums[i]) + dfs(i+1,sum-nums[i])
            return dp[(i,sum)]

        return dfs(0,0)
                