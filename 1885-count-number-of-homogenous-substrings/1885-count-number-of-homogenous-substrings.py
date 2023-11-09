class Solution:
    #
    def countHomogenous(self, s: str) -> int:
        result = 1
        same = 1
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                same += 1
            else:
                same = 1
            result += same
        return result %(10**9+7)


            

        