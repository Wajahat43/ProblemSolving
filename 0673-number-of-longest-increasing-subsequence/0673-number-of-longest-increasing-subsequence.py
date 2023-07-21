class Solution:

    def findNumberOfLIS(self, nums: List[int]) -> int:

        subSequences = []

        for i, num in enumerate(nums):
            #current subsequence [length and count]
            current = [1,1]
            for j in range(i-1,-1,-1):
                if nums[j] < num:
                    seq = subSequences[j]
                    if seq[0] >= current[0]:
                        current = [seq[0]+1,seq[1]]

                    elif seq[0] == current[0]-1:
                        current[1] += seq[1]

            subSequences.append(current)
        
        maxLen = 0
        count = 0
        
        for seq in subSequences:
            if seq[0] > maxLen:
                maxLen = seq[0]
                count = seq[1]
                
            elif seq[0] == maxLen:
                count += seq[1]
            
        return count
                

