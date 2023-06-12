class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        for f, s in zip(word1,word2):
            res += f + s
        if len(word1) > len(word2):
            res += word1[len(word2):]
        elif len(word2) > len(word1):
            res += word2[len(word1):]
        return res
        
        