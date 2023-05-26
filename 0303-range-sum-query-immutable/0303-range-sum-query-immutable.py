class NumArray:
    #Solved using the concept of postfix sum (we can also use pre-fix sum)
    def __init__(self, nums: List[int]):
        #create a list to store postfix of each index including the value at index itself
        self.postfix = []
        sum = 0
        #calculate postfix
        for i in range(len(nums)-1,-1,-1):
            sum += nums[i]
            #append at last
            self.postfix.append(sum)
        #reverse the list because we appended sum of each value at end of list. 
        #can be avoided by creating a list of fixed size and then using a pointer to 
        #move from end to start while building postfix list.
        self.postfix.reverse()
        

    def sumRange(self, left: int, right: int) -> int:
        #return leftPostfixSum - rightPostfix sum
        leftSum = self.postfix[left]
        rightSum = self.postfix[right+1] if right+1 < len(self.postfix) else 0
        return leftSum-rightSum 

        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)