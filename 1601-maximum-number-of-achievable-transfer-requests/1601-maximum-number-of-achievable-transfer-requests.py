class Solution:
    #Observations
    #1. At each step we have to decide whether we can fullfill this transfer request or not
    #2. If at the end all the buildings have outgoing( -1 ) and incoming (+1) in buildings value (intially 0) are 0 that means we can satisfy the requests of current subset
    #3. The problem statement has very low constraints
    #4. This seems like a bruteforce backtracking problem
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:

        bMap = {}
        for i in range(n+1):
            bMap[i] = 0

        #function to perform dfs
        def dfs(i, added):
            #if added requests are satisfied
            if i == len(requests) and all(value == 0 for value in bMap.values()):
                return added
            
            #if this is invalid state
            elif i == len(requests):
                return 0
            

            #handle current request
            bMap[requests[i][1]] += 1
            bMap[requests[i][0]] -= 1
            res = dfs(i+1, added+1)


            #If we want to skip the current request, rollover the changes of it
            bMap[requests[i][1]] -= 1
            bMap[requests[i][0]] += 1


            #don't handle current request
            res = max(res,dfs(i+1, added))

            return res
        
        return dfs(0,0)
            

            
            
