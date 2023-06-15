class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        resultSet = []
        
        def dfs(i, currentSet,resultSet):
            if i == len(nums):
                resultSet.append(currentSet.copy())
                return
            
            #include ith value in currentSet
            currentSet.append(nums[i])
            
            dfs(i+1,currentSet,resultSet)
            
            #now don't include ith value in currentSet
            currentSet.pop()
            
            dfs(i+1,currentSet,resultSet)
         
        dfs(0,[],resultSet)
        return resultSet
        
        
        
        