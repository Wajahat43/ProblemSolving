class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        
        k = 3
        heap = []
        used = set()
        for num in nums:
            if num not in used:
                heap.append(num*-1)
                used.add(num)
            
        if len(used) < 3:
            return max(nums)
        heapq.heapify(heap)
        
        res = 0
        for i in range(k):
            res = heapq.heappop(heap)*-1
        return res
        