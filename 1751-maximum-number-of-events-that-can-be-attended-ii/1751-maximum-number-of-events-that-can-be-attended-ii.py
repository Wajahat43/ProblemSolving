class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort()
        
        dp = {}
        def dfs(i, k, endTime):
            #if we can't consider more events
            if i >= len(events) or k == 0:
                return 0

            #if we already reached this state
            if (i,k,endTime) in dp:
                return dp[(i,k,endTime)]

            res = 0
            #if we can attend current event attend it
            if events[i][0] > endTime:
                res = dfs(i+1, k-1, events[i][1]) + events[i][2]
            
            #skip current event
            res = max(res, dfs(i+1,k, endTime))
            #store result for future use.
            dp[(i,k,endTime)] = res
            return res
        
        return dfs(0,k, -1)