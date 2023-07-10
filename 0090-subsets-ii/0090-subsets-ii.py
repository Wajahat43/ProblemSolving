class Solution:
    #Observations
    #1. Each element can be part of our current subset, or we skip it
    #2. Since there are duplicates, we want to skip all consecutive duplicates
    #because in case of [1,2,2] so we don't want [1,2] and we skip at index 1 but index 2 will again make [1,2]

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        res = []
        nums.sort()

        def dfs(i, subset):
            if i >= len(nums):
                res.append(subset.copy())
                return
            
            subset.append(nums[i])
            #Choose the ith as part of current subset.
            dfs(i+1,subset)

            
            #skip the ith, and all the same 
            subset.pop()
            current = nums[i]
            while i+1 < len(nums) and nums[i+1] == current:
                i += 1
            
            dfs(i+1, subset)

            
        dfs(0,[])
        return sorted(res,key = len)