class Solution:
    #We can use two pointers to solve this problem.
    #We will sort the array and then try to convert all the number
    #before ith index to number at ith index. We will keep a difference variable
    #to keep track of number of operations required.
    def maxFrequency(self, numsArr: list[int], k: int) -> int:
        numsArr = sorted(numsArr)
        left = 0
        right = 1
        diff = 0
        ans = 1

        print(numsArr)
        while right < len(numsArr):
            #add to diff size of subarray * diff of element right - 1 and right
            diff += (numsArr[right] - numsArr[right-1])* (right-left)

            #if we have had more operations than k, remove the left most element from subarra
            #by subtracting its number of oeprations it too
            if diff > k:
                diff -= numsArr[right] - numsArr[left]
                left += 1

            ans = max(ans, (right - left)+1)
            right += 1
        return ans




    
        