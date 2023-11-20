class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        while i < len(s) and s[i] == ' ':
            i += 1
        isPositive = True
        if i < len(s) and (s[i] == '+' or s[i] == '-'):
            if s[i] == '-':
                isPositive = False
            i += 1
        while i < len(s) and s[i] == '0':
            i += 1
        num = ""

        while i < len(s) and s[i] >= "0" and s[i] <= "9":
            num += s[i]
            i += 1
        if not num:
            return 0
        num = int(num)
        
        if not isPositive:
            num = num*-1
        if num < -(2**31):
            return -(2**31)
        if num > 2**31-1:
            return (2**31)-1
        return num
        