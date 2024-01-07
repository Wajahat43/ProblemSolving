class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        iterations = 0
        result = 0

        diff = float("-infinity")

        for i in  range(0,len(nums)-1):
            currentdiff = nums[i+1]-nums[i]
            if currentdiff == diff:
                iterations += 1
            else:
                diff = currentdiff
                iterations = 1

            if iterations >= 2:
                result += iterations - 1
        return result
        
            

        