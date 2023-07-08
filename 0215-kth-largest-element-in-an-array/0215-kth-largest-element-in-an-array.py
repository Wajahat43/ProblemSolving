class Solution:
    #Quick Select Takes O(N) time on average why?
    #Because if choose approprtiate pivot we divide the size of array in half
    # So we take N + N/2 + N/4 + N/8 which is 2N
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heap.append(num*-1)
            
        heapq.heapify(heap)
        
        res = 0
        for i in range(k):
            res = heapq.heappop(heap)*-1
        return res
        