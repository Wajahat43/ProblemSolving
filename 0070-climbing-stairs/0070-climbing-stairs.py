class Solution:
    def climbStairs(self, n: int) -> int:
        secondLast = 0 #0
        last = 1 #1
        current = last+secondLast #1
        
        #i = 0, next = 1, secondLast = 1, last = 1, current = 2
        for i in range(1,n): 
            secondLast = last
            last = current
            current = last+secondLast
        return current
        
        