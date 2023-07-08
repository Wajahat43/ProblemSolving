class Solution:
    #Observations
    #1. Substring is always of size 10
    #2. We need to see if a substring is repeating (have we seen this before?)
    #3. We can check every substring of size 10 and use sets to store the res as well as previous substrings.
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        
        left = 0
        right = 0
        current = ""
        res = set()
        subs = set()

        while right < len(s):
            current += s[right]

            if right >= 9:                
                if right - left + 1 > 10:
                    current = current[1:]
                
                if current not in subs:
                    subs.add(current)
                else:
                    res.add(current)

            right += 1
        
        
       
        return list(res)
