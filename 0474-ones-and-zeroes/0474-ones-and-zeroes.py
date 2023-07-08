class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:

        dp = {}
        def dfs(i, mleft, nleft):
            if i >= len(strs):
                return 0

            if (i,mleft,nleft) in dp:
                return dp[(i,mleft,nleft)]
            
            
            oneFreq = strs[i].count("1")
            zeroFreq = strs[i].count("0")

            res = 0

            if oneFreq <= nleft and zeroFreq <= mleft:
                res = dfs(i+1,mleft-zeroFreq, nleft-oneFreq)+1
            
            res = max(res,dfs(i+1,mleft,nleft))
            dp[(i,mleft,nleft)] = res
            return res
        
        return dfs(0,m,n)