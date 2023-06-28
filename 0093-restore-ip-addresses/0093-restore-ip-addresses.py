class Solution:
    #Observations
    #1. We have to add dots. WE cannot modify the string otherwise
    #2. At each index we can choose to add a . or skip adding a dot at that index
    #3. Since we have to find all valid combinations, using dp will not be useful.
    #4. Also there will not be repeating subproblems.
    def restoreIpAddresses(self, s: str) -> List[str]:


        def isValid(ip):
            tokens = ip.split(".")
            if len(tokens) != 4:
                return False
            for token in tokens:
                if token == "":
                    return False
                if str(int(token)) != token:
                    return False
                if int(token) < 0 or int(token) > 255:
                    return False
            return True

        result = []
        def dfs(i, current):
            if i >= len(s):
                if isValid(current) == True:
                    result.append(current)
                return
            
            current += s[i]

            dfs(i+1, current + ".")
            dfs(i+1, current)
        dfs(0, "")
        return result
