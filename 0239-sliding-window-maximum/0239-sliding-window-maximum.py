class Solution:
    #A better way tto do this is to use a montonic deque that O(N)
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = defaultdict(list)
        heap = []

        #this will store result
        res = []
        for i in range(len(nums)+1):
            

            if i >= k:
                while True and heap:
                    val = heapq.heappop(heap)*-1
                    if len(window[val]):
                        heapq.heappush(heap,val*-1)
                        res.append(val)
                        break
                
                window[nums[i-k]].remove(i-k)
            if i < len(nums):
                curr = nums[i]
                #curr is in my window
                window[curr].append(i)
                #also push curr to heap
                heapq.heappush(heap, curr*-1)
            

        return res
            


            
            


