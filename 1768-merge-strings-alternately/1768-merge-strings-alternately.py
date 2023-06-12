class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        #iterate over the stirngs and add their characters until one or both of them runout
        for f, s in zip(word1,word2):
            res += f + s
        #if first string is greater then second, add the rest of it to res
        if len(word1) > len(word2):
            res += word1[len(word2):]
        #if second string is greater than first, add the rest of it to res
        elif len(word2) > len(word1):
            res += word2[len(word1):]
        return res
        
        