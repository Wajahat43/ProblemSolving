import queue
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        pq = queue.PriorityQueue()
        for stone in stones:
            pq.put(stone*-1)
        while pq.qsize() > 1:
            first = pq.get()*-1
            second = pq.get()*-1

            heavier = max(first,second)
            lighter = min(first,second)

            if heavier != lighter:
                pq.put((heavier-lighter)*-1)
                
        if pq.qsize() == 1:
            return pq.get()*-1
        return 0