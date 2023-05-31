class Solution:
    def customSortString(self, order: str, s: str) -> str:
        smap = {}
        #store s in a set
        for c in s:
            if c not in smap:
                smap[c] = 0
            
            smap[c] += 1
            
        
        res = ""
        #iterate over order and all the characters that are in s in the result
        for c in order:
            if c in smap:
                #if a character is repeated add it multiple times
                freq = smap[c]
                for i in range(freq):
                    res += c
        #set for order
        orderset = set(order)
        #for each character in map, if it is not in order append it to result.
        for c in smap.keys():
            if c not in orderset:
                freq = smap[c]
                for i in range(freq):
                    res += c
        return res