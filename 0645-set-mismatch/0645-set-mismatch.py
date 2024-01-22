class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        duplicate = -1
        missing = -1
        checked = [0]* (len(nums)+1)
        
        for num in nums:
            if checked[num] == -1:
                duplicate = num
            
            checked[num] = -1
        for i in range(1,len(checked)):
            if checked[i] != -1:
                missing = i
        return [duplicate, missing]
            
        
                
        
        