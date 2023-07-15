class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        #sort events on start day
        events.sort()
        
        pq = []

        day,i, res = 0,0,0
        while i < len(events) or pq:
            while i < len(events) and events[i][0] == day:
                #push in form [end-start] so that min heap is formed on lowest end time
                heapq.heappush(pq,events[i][-1:])
                i += 1
            
            #pop all entries that cannot be part of our solution now
            while pq and pq[0][0] < day:
                heapq.heappop(pq)

            if pq:
                res += 1
                heapq.heappop(pq)

            day += 1
        return res
            

        