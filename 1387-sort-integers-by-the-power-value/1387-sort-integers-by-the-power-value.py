class Solution(object):
    def getKth(self, lo, hi, k):


        dic = {}
        dic[1] = 0
   
        #Function will convert a number to 1 given the rules.
        #It will also save the calculation results in a dictionary to
        #avoid recalculating the numbers
        def makeOne(num):
            if num in dic:
                return dic[num]
            if num%2 == 0:
                dic[num] = 1 + makeOne(num/2)
            else:
                dic[num] = 1 + makeOne(3*num+1)
            return dic[num]
            
        sortedList= []
        #create a list of numbers and thier steps of power
        for i in range(lo,hi+1):
            sortedList.append((makeOne(i),i))
        #sort the result
        sortedList = sorted(sortedList)
        #return kth value
        res = sortedList[k-1]
        
        return res[1]