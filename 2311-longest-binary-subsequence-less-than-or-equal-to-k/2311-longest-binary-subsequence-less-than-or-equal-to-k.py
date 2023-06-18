class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        res = ""

        #Convert Binary number to integer
        def toInt(st):
            val = 0
            j = 0
            for i in range(len(st)-1,-1,-1):
                val += int(math.pow(2,j))*int(st[i])
                j += 1
            
            return val

        #for each character in s
        for c in s:
            #add current character to our result
            res += c
            #if our result > k then we need to remove the left most 1 from it
            if toInt(res) > k:
                #
                ind = res.index("1")
                res = res[0:ind] + res[ind+1:]
        return len(res)
