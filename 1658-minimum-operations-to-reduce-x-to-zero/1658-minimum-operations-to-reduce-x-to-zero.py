class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target = sum(nums)-x

        l = 0
        r = 0
        currentSum = 0
        res = float("inf")
        while r < len(nums):
            currentSum += nums[r]

            while l <= r and currentSum > target:
                currentSum -= nums[l]
                l += 1
            if currentSum == target:
                res = min(res, len(nums)- (r-l+1))
            r += 1
        return res if res != float("inf") else -1


        
        