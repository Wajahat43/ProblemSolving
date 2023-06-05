class Solution:
    #I made the obervation that we could switch paths when we encountered common  values between array. From ith index of common value arr1, we could swithc to jth index in common value of array2.
    #So the problem was to find indexes of common values, then intially from start
    #find the max sum till that index. And then move to next common value and find maxSum from this index to the index of second common value.
    #As our path could only have unique values,that meant we didn't actually need to swith paths, just move from one common value to next and take the max value int hat interval.
    #
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        indexes1 = {}
        indexes2 = {}
        common = []
        
        for i,num in enumerate(nums1):
            indexes1[num] = i
        for i, num in enumerate(nums2):
            indexes2[num] = i
            if num in indexes1:
                common.append(num)
                
        i = 0
        j = 0
        maxSum = 0
        
        for c in range(len(common)):
            cnum = common[c]
            endingi = indexes1[cnum]
            endingj = indexes2[cnum]
            
            firstSum = 0
            secondSum = 0
            
            for k in range(i,endingi+1):
                firstSum += nums1[k]
            for k in range(j,endingj+1):
                secondSum += nums2[k]
                
            i = endingi+1
            j = endingj+1
                
            maxSum += max(firstSum,secondSum)
        firstSum = 0
        secondSum = 0
        while i < len(nums1):
            firstSum += nums1[i]
            i += 1
        while j < len(nums2):
            secondSum += nums2[j]
            j +=1
            
        maxSum += max(firstSum,secondSum)
        mod = 10**9 + 7
        return maxSum %mod
            
        
        
        