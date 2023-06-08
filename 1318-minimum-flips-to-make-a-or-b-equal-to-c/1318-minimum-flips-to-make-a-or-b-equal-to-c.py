class Solution:

    def minFlips(self,a: int, b: int, c: int) -> int:
        ans = 0

        while a or b or c:
            #c&1 will give its least significant bit
            if c&1 == 1 and a&1 == 0 and b&1 == 0:
                ans += 1
            elif c&1 == 0:
                ans += (a&1) + (b&1)
            
            a >>= 1
            b >>= 1
            c >>= 1
        return ans


        
        