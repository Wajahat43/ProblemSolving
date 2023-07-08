class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heap.append(num*-1)
            
        heapq.heapify(heap)
        
        res = 0
        for i in range(k):
            res = heapq.heappop(heap)*-1
        return res
        