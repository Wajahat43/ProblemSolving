class Solution:
    #We have to minimize number of steps (looks like dp? It is)
    #We also have only 2 operations at a given index
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        arr2 = sorted(arr2)

        dp = {}

        #Do a dfs
        def dfs(i,prev):
            #if we have reached end of array
            if i >= len(arr1):
                return 0
            #if we already solved this sub-problem
            if (i,prev) in dp:
                return dp[(i,prev)]
            
            #intialize result to infinity
            res = float("inf")
            #if it is in increasing order don't swap 
            if arr1[i] > prev:
                res = dfs(i+1,arr1[i])
            
            ind = bisect_right(arr2,prev)

            #if we can do a swap operation
            if ind < len(arr2):
                res = min (res, dfs(i+1, arr2[ind])+1)
            #store in dp
            dp[(i,prev)] = res
            #return result
            return dp[(i,prev)]

        res = dfs(0,-1)
        if res == float("inf"):
            return -1
        return res
            
            


                   
            
            
        