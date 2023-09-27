class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = []
        def dfs(i, current):
            if i >= len(s):
                res.append(''.join(current))
                return
            
            #Choose the ith character as is
            current.append(s[i])
            dfs(i+1, current)
            #remove ith character
            current.pop()
            #Transform smaller case letter to uppercase.
            if (s[i] >= 'a' and s[i] <= 'z'):
                current.append(s[i].upper())
                dfs(i+1, current)
                current.pop()
            #Transform the uppercase letter to smaller case
            elif (s[i] >= 'A' and s[i] <= 'Z'):
                current.append(s[i].lower())
                dfs(i+1, current)
                current.pop()
            
        dfs(0,[])
        return res

        